# Generated by Django 2.2.6 on 2020-01-29 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0009_guide_guide_snippet'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_content',
            field=models.TextField(default='hello'),
        ),
    ]
