from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import index, about, services, contact
from .views import user_recommendations, all_programs, program_detail, view_recommendations, careers, career_detail
from config.views import SignUpView

urlpatterns = [
    path('', SignUpView.as_view(), name='signup'),
    # path('logout/', LogoutView.as_view(next_page='signup'), name='logout'),
    path('home/',index, name='home'),
    path('about/', about, name='about'),
    path('services/',services, name='services'),
    path('contact/',contact, name='contact'),
    path('recommendations/', user_recommendations, name='user_recommendations'),
    path('view-recommendations/', view_recommendations, name='view_recommendations'),
    path('programs/', all_programs, name='programs'),
    path('programs/<int:pk>/', program_detail, name='program_detail'),
    path('careers/', careers, name='careers'),
    path('careers/<int:pk>/', career_detail, name='career_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
