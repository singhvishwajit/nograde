# Generated by Django 2.2.6 on 2019-11-12 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]
