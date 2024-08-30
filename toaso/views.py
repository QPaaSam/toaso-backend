from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import UserProfile, Program
from .forms import UserProfileForm



# Create your views here.
def index(request):
    return render(request, 'toaso/home.html')

def about(request):
    return render(request, 'toaso/about.html')

def services(request):
    return render(request, 'toaso/services.html')

def contact(request):
    return render(request, 'toaso/contact.html')


def recommend_programs(user_profile):
    recommendations = []
    user_interests = set(user_profile.interests.all())
    user_elective_subjects = set(user_profile.elective_subjects.all())

    programs_with_interest_matches = []
    programs_without_interest_matches = []

    for program in Program.objects.all():
        program_electives = set(program.elective_requirements.all())
        constant_course = program.constant_elective

        if user_profile.aggregate is not None and program.cut_off_point is not None:
            if user_profile.aggregate <= program.cut_off_point:
                if program.elective_requirement_logic == 'ANY':
                    if user_elective_subjects & program_electives:
                        recommendations.append(program)
                elif program.elective_requirement_logic == 'ALL':
                    if program_electives.issubset(user_elective_subjects):
                        recommendations.append(program)
                elif program.elective_requirement_logic == 'CONSTANT_PLUS_TWO':
                    if constant_course in user_elective_subjects:
                        remaining_subjects = user_elective_subjects - {constant_course}
                        if len(remaining_subjects & program_electives) >= 2:
                            programs_with_interest_matches.append(program)
    
    programs_with_interest_matches.sort(key=lambda p: len(user_interests & set(p.required_interests.all())), reverse=True)
    
    for program in Program.objects.all():
        if program not in programs_with_interest_matches:
            programs_without_interest_matches.append(program)

    return programs_with_interest_matches + programs_without_interest_matches

def user_recommendations(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user_profile = form.save()
            request.session['user_profile_id'] = user_profile.id
            return redirect('view_recommendations')
    else:
        form = UserProfileForm()
    return render(request, 'toaso/user_form.html', {'form':form})

def view_recommendations(request):
    user_profile_id = request.session.get('user_profile_id')
    if user_profile_id:
        user_profile = UserProfile.objects.get(id = user_profile_id)
        recommended_programs = recommend_programs(user_profile)
        query = request.GET.get('q') #search fuction
        if query:
            recommended_programs = [program for program in recommended_programs if query.lower() in program.name.lower()]
        return render(request, 'toaso/user_recommendations.html', {'user':user_profile, 'recommended_programs':recommended_programs, 'all_programs': all_programs, 'query': query})
    else:
        return redirect('user_recommendations')
    
def all_programs(request):
    programs = Program.objects.select_related('school').all()
    query = request.GET.get('q')
    if query:
        programs = Program.objects.filter(name__icontains=query)
        page_obj = programs
    else:
        programs = Program.objects.all()
        page = request.GET.get('page')

        if page == 'all':
            page_obj = programs
        else:
            paginator = Paginator(programs, 10)
            page_obj = paginator.get_page(page)
    return render(request, 'toaso/all_programs.html', {'page_obj':page_obj})    

def program_detail(request, pk):
    program = get_object_or_404(Program, pk=pk)
    return render(request, 'toaso/program_detail.html', {'program':program})