# Generated by Django 2.2.6 on 2020-03-09 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0010_course_course_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='syllabus',
            name='course_name',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='courses',
        ),
        migrations.RemoveField(
            model_name='course',
            name='prerequisites',
        ),
        migrations.RemoveField(
            model_name='course',
            name='skills_covered',
        ),
        migrations.DeleteModel(
            name='Guide',
        ),
        migrations.DeleteModel(
            name='Syllabus',
        ),
        migrations.DeleteModel(
            name='Tutorial',
        ),
    ]
