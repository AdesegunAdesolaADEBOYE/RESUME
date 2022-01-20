# Generated by Django 4.0 on 2022-01-17 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Please enter your own given name', max_length=100)),
                ('last_name', models.CharField(help_text='Please enter your  surname', max_length=100)),
                ('summary', models.TextField(help_text='Tell us about yourself', null=True)),
                ('date_of_birth', models.DateField()),
                ('date_created', models.DateField(auto_now=True)),
                ('date_updated', models.DateField(auto_now_add=True)),
                ('state_of_origin', models.CharField(help_text='Please tell us your state of origin', max_length=20)),
            ],
        ),
    ]
