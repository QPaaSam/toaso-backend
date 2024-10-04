from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import UserProfile, Program, Career
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
    
    # Get the user's elective subjects and interests
    user_elective_subjects = set(user_profile.elective_subjects.all())
    user_interests = set(user_profile.interests.all())

    for program in Program.objects.all():
        program_electives = set(program.elective_requirements.all())
        constant_course = program.constant_elective
        program_interests = set(program.required_interests.all())

        # Check if the user meets the aggregate requirement
        if user_profile.aggregate is not None and program.cut_off_point is not None:
            if user_profile.aggregate <= program.cut_off_point:

                # Check the elective requirement logic for the program
                if program.elective_requirement_logic == 'ANY':
                    # Ensure the user has at least 3 matching elective subjects
                    if len(user_elective_subjects & program_electives) >= 3:
                        # Check if any user interests match the program's interests
                        if user_interests & program_interests:
                            recommendations.append(program)

                elif program.elective_requirement_logic == 'ALL':
                    # Check if all required electives match the user's subjects
                    if program_electives.issubset(user_elective_subjects):
                        if user_interests & program_interests:
                            recommendations.append(program)

                elif program.elective_requirement_logic == 'CONSTANT_PLUS_TWO':
                    # Ensure the user has the constant elective and two others
                    if constant_course in user_elective_subjects:
                        remaining_subjects = user_elective_subjects - {constant_course}
                        if len(remaining_subjects & program_electives) >= 2:
                            if user_interests & program_interests:
                                recommendations.append(program)

    return recommendations

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

def careers(request):
    careers = Career.objects.all()
    query = request.GET.get('q')
    if query:
        careers = Career.objects.filter(name__icontains=query)
        page_obj = careers
    else:
        careers = Career.objects.all()
        page = request.GET.get('page')

        if page == 'all':
            page_obj = careers
        else:
            paginator = Paginator(careers, 10)
            page_obj = paginator.get_page(page)
    return render(request, 'toaso/career.html', {'page_obj':page_obj})    

def career_detail(request, pk):
    career = get_object_or_404(Career, pk=pk)
    return render(request, 'toaso/career_detail.html', {'career':career})