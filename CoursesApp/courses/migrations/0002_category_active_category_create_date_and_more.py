# Generated by Django 4.2.6 on 2023-10-22 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='category',
            name='create_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='update_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateField(auto_now_add=True, null=True)),
                ('update_date', models.DateField(auto_now_add=True, null=True)),
                ('active', models.BooleanField(default=False)),
                ('subject', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
