from django.urls import path
from .views import index, base
from .views import user_recommendations, all_programs, program_detail, view_recommendations

urlpatterns = [
    path('',index, name='home'),
    path('base/',base, name='base'),
    path('recommendations/', user_recommendations, name='user_recommendations'),
    path('view-recommendations/', view_recommendations, name='view_recommendations'),
    path('programs/', all_programs, name='programs'),
    path('programs/<int:pk>/', program_detail, name='program_detail'),
]
