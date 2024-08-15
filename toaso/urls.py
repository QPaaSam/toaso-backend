from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth.views import LoginView
from .views import index, about, services, contact
from .views import user_recommendations, all_programs, program_detail, view_recommendations
from config.views import SignUpView


urlpatterns = [
    path('', SignUpView.as_view(), name='signup'),
    path('home/',index, name='home'),
    path('about/', about, name='about'),
    path('services/',services, name='services'),
    path('contact/',contact, name='contact'),
    path('recommendations/', user_recommendations, name='user_recommendations'),
    path('view-recommendations/', view_recommendations, name='view_recommendations'),
    path('programs/', all_programs, name='programs'),
    path('programs/<int:pk>/', program_detail, name='program_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
