# Generated by Django 2.2.6 on 2020-04-06 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20200406_0955'),
        ('learn', '0013_auto_20200406_0955'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='categories',
            field=models.ManyToManyField(blank=True, to='learn.Category'),
        ),
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(blank=True, to='learn.Category'),
        ),
    ]
