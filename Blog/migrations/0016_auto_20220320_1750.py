# Generated by Django 3.2.12 on 2022-03-20 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0015_rename_category_blogmodel_categories'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogmodel',
            old_name='categories',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='categorymodel',
            old_name='cat_name',
            new_name='title',
        ),
    ]