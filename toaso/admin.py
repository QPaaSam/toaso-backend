from django.contrib import admin
from .models import Student,Course,CoreSubject,ElectiveSubject, Programs

# Register your models here.
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(CoreSubject)
admin.site.register(ElectiveSubject)
admin.site.register(Programs)
