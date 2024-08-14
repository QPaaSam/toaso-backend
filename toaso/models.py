from django.db import models

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='school_logos/')

    def __str__(self):
        return self.name

class ElectiveSubject(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    elective_subjects = models.ManyToManyField(ElectiveSubject, related_name='users')
    aggregate = models.IntegerField()
    career_aspiration = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Program(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='programs', null=True, blank=True)
    cut_off_point = models.IntegerField()
    elective_requirements = models.ManyToManyField(ElectiveSubject, related_name='required_for_programs', blank=True)
    constant_elective = models.ForeignKey(ElectiveSubject, related_name='constant_for_programs', null=True, blank=True, on_delete=models.SET_NULL)
    elective_requirement_logic = models.CharField(
        max_length=50,
        choices=[('ANY', 'Any'), ('ALL', 'All'), ('CONSTANT_PLUS_TWO', 'Constat plus Two')],
        default='ANY'
    )
    career = models.CharField(max_length=100)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


