# Generated by Django 3.1.2 on 2020-10-09 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('author', models.CharField(max_length=30)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]
