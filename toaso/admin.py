from django.contrib import admin
from .models import ElectiveSubject, UserProfile, Program, School, Interest

# Register your models here.
admin.site.register(ElectiveSubject)
admin.site.register(UserProfile)
admin.site.register(Program)
admin.site.register(School)
admin.site.register(Interest)

