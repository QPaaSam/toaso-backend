from django.shortcuts import render,HttpResponse
from .models import UserProfile, Program, ElectiveSubject


# Create your views here.
def index(request):
    return HttpResponse('hello world')

def recommend_programs(user_profile):
    recommendations = []
    for program in Program.objects.all():
        if user_profile.aggregate <= program.cutt_off_point:
            if any(subject in user_profile.elective_subjects.all() for subject in program.elective_subject.all()):
                recommendations.append(program)
    return recommendations

def user_recommendations(request, user_id):
    user_profile = UserProfile.objects.get(id=user_id)
    recommended_programs = recommend_programs(user_profile)
    all_programs = Program.objects.all()
    return render(request, 'toaso/user_recommendations.html', {'user':user_profile, 'recommended_programs':recommended_programs, 'all_programs': all_programs})

