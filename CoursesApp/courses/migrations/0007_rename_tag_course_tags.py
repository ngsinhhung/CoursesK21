# Generated by Django 4.2.6 on 2023-11-03 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_alter_course_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='tag',
            new_name='tags',
        ),
    ]
