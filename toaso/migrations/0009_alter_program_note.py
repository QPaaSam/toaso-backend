# Generated by Django 5.0.7 on 2024-07-28 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toaso', '0008_electivesubject_program_userprofile_delete_course_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='note',
            field=models.TextField(),
        ),
    ]
