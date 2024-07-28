from django.urls import path
from .views import index
from .views import user_recommendations

urlpatterns = [
    path('',index, name='home'),
    path('recommendations/', user_recommendations, name='user_recommendations'),
]
