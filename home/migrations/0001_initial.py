# Generated by Django 3.1.4 on 2020-12-02 11:17

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddedVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=home.models.generate_unique_code, max_length=10, null=True, unique=True)),
                ('title', models.CharField(max_length=100)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(upload_to='video')),
            ],
        ),
    ]