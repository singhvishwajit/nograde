# Generated by Django 2.2.6 on 2019-11-26 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_books'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='amazon_url',
            field=models.URLField(default='google.com'),
        ),
    ]