# Generated by Django 5.0.4 on 2024-04-09 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0002_receipe_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipe',
            name='receipe_view_count',
            field=models.ImageField(default=1, upload_to=''),
        ),
    ]