# Generated by Django 4.2.2 on 2023-06-29 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_job_categroy_job_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categroy',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='job',
            name='image',
            field=models.ImageField(upload_to='image_jobs'),
        ),
    ]
