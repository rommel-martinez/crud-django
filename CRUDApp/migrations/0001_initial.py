# Generated by Django 4.1.7 on 2023-03-10 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(blank=True, max_length=20)),
                ('Last_Name', models.CharField(blank=True, max_length=20)),
                ('DOB', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]