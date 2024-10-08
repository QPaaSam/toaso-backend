# Generated by Django 5.0.7 on 2024-07-27 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toaso', '0006_universities'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='core_subjects',
        ),
        migrations.RemoveField(
            model_name='electivesubject',
            name='group',
        ),
        migrations.RemoveField(
            model_name='student',
            name='elective_subjects',
        ),
        migrations.RemoveField(
            model_name='student',
            name='program',
        ),
        migrations.DeleteModel(
            name='Universities',
        ),
        migrations.AddField(
            model_name='course',
            name='note',
            field=models.TextField(null=True),
        ),
        migrations.DeleteModel(
            name='CoreSubject',
        ),
        migrations.DeleteModel(
            name='ElectiveSubject',
        ),
        migrations.AddField(
            model_name='student',
            name='elective_subjects',
            field=models.TextField(null=True),
        ),
        migrations.DeleteModel(
            name='Programs',
        ),
    ]
