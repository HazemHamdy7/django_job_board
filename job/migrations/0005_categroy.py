# Generated by Django 4.2.2 on 2023-06-16 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_job_experience_job_published_at_job_salary_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categroy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
    ]