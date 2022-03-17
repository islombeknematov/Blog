# Generated by Django 3.2.12 on 2022-03-15 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=150)),
                ('message', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
    ]
