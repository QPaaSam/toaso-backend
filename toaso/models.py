from django.db import models

# Create your models here.
class CoreSubject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Programs(models.Model):
    PROGRAM_CHOICES = [
        ('SCIENCE', 'GENERAL SCIENCE'),
        ('BUSINESS', 'BUSINESS'),
        ('G.ARTS', 'GENERAL ARTS'),
        ('V.ARTS', 'VISUAL ARTS'),
        ('HOME_ECONS', 'HOME ECONOMICS')
    ]
    name = models.CharField(max_length=50, choices=PROGRAM_CHOICES, unique=True)

    def __str__(self):
        return self.get_name_display()

class ElectiveSubject(models.Model):
    name = models.CharField(max_length=100)
    group = models.ForeignKey(Programs, on_delete=models.CASCADE, related_name='elective_subjects', null=True)

    def __str__(self):
        return self.name
    

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    high_school_courses = models.TextField()
    interests = models.TextField()
    core_subjects = models.ManyToManyField(CoreSubject)
    program = models.ForeignKey(Programs, on_delete=models.SET_NULL, null=True)
    elective_subjects = models.ManyToManyField(ElectiveSubject)

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    requirements = models.TextField()
    cutt_off_point = models.SmallIntegerField()
    career = models.CharField(max_length=100)

    def __str__(self):
        return self.title


