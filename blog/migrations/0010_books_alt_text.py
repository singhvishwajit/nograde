# Generated by Django 2.2.6 on 2020-03-10 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_newsletter'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='alt_text',
            field=models.TextField(default='some-string'),
        ),
    ]
