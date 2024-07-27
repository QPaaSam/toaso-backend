from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    interests = models.TextField()
    elective_subjects = models.TextField(null=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    requirements = models.TextField()
    cutt_off_point = models.SmallIntegerField()
    career = models.CharField(max_length=100)
    note = models.TextField(null=True)

    def __str__(self):
        return self.title


