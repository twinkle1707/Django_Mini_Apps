# Generated by Django 5.0.4 on 2024-04-07 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_student_file_remove_student_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='file',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
