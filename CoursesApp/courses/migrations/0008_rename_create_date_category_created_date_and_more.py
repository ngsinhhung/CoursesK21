# Generated by Django 4.2.6 on 2023-12-24 07:59

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_rename_tag_course_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='create_date',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='update_date',
            new_name='updated_date',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='create_date',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='update_date',
            new_name='updated_date',
        ),
        migrations.RenameField(
            model_name='lesson',
            old_name='create_date',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='lesson',
            old_name='update_date',
            new_name='updated_date',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='create_date',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='update_date',
            new_name='updated_date',
        ),
        migrations.AddField(
            model_name='user',
            name='avatar_user',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='avatar'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_lesson', to='courses.course'),
        ),
    ]