# Generated by Django 5.0.7 on 2024-07-27 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toaso', '0004_programs_alter_student_core_subjects_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='high_school_courses',
        ),
    ]
