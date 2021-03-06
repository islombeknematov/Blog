# Generated by Django 3.2.12 on 2022-03-17 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Blog', '0004_delete_blogmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('body', models.TextField()),
                ('cover', models.ImageField(blank=True, null=True, upload_to='media')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'blog',
                'verbose_name_plural': 'blogs',
            },
        ),
    ]
