# Generated by Django 2.2.6 on 2019-11-17 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0004_course_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='prerequisites',
            field=models.CharField(default='some-string', max_length=100),
        ),
    ]