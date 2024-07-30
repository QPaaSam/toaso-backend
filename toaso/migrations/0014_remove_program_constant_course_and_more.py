# Generated by Django 5.0.7 on 2024-07-30 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toaso', '0013_program_constant_course_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='program',
            name='constant_course',
        ),
        migrations.RemoveField(
            model_name='program',
            name='elective_requirement_logic',
        ),
        migrations.AlterField(
            model_name='program',
            name='elective_subject',
            field=models.ManyToManyField(to='toaso.electivesubject'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='elective_subjects',
            field=models.ManyToManyField(to='toaso.electivesubject'),
        ),
    ]
