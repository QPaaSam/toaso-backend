# Generated by Django 5.0.7 on 2024-08-02 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toaso', '0016_rename_cutt_off_point_program_cut_off_point'),
    ]

    operations = [
        migrations.RenameField(
            model_name='program',
            old_name='constant_course',
            new_name='constant_elective',
        ),
    ]
