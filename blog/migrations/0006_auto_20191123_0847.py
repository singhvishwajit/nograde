# Generated by Django 2.2.6 on 2019-11-23 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0006_course_syllabus'),
        ('blog', '0005_post_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(blank=True, to='learn.Path'),
        ),
    ]
