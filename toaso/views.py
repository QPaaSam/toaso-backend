from django.shortcuts import render, get_object_or_404
from .models import UserProfile, Program
from .forms import UserProfileForm



# Create your views here.
def index(request):
    return render(request, 'toaso/home.html')

def recommend_programs(user_profile):
    recommendations = []
    user_elective_subjects = set(user_profile.elective_subjects.all())

    for program in Program.objects.all():
        program_electives = set(program.elective_requirements.all())
        constant_course = program.constant_course

        if user_profile.aggregate <= program.cutt_off_point:
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
                        recommendations.append(program)
    return recommendations

def user_recommendations(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user_profile = form.save()
            recommended_programs = recommend_programs(user_profile)
            all_programs = Program.objects.all()
            return render(request, 'toaso/user_recommendations.html', {'user':user_profile, 'recommended_programs':recommended_programs, 'all_programs': all_programs})
    else:
        form = UserProfileForm()
    return render(request, 'toaso/user_form.html', {'form':form})

def all_programs(request):
    programs = Program.objects.all()
    return render(request, 'toaso/all_programs.html', {'programs':programs})

def program_detail(request, pk):
    program = get_object_or_404(Program, pk=pk)
    return render(request, 'toaso/program_detail.html', {'program':program})