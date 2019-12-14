# Generated by Django 2.2.6 on 2019-11-26 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0006_course_syllabus'),
        ('blog', '0006_auto_20191123_0847'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('thumbnail', models.ImageField(blank=True, default='default.png', upload_to='')),
                ('details', models.TextField()),
                ('category', models.ManyToManyField(blank=True, to='learn.Path')),
            ],
        ),
    ]
