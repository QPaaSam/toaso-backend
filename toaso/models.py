from django.db import models

# Create your models here.

class ElectiveSubject(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    elective_subjects = models.ManyToManyField(ElectiveSubject)
    aggregate = models.IntegerField()
    career_aspiration = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Program(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    elective_subject = models.ManyToManyField(ElectiveSubject)
    cutt_off_point = models.IntegerField()
    career = models.CharField(max_length=100)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


