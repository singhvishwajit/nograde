# Generated by Django 2.2.6 on 2020-03-10 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0011_auto_20200309_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='alt_text',
            field=models.TextField(default='some-string'),
        ),
    ]
