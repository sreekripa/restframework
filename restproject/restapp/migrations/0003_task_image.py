# Generated by Django 3.2.2 on 2021-05-10 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0002_task_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='image',
            field=models.ImageField(default='Image/None/No_img.jpg', upload_to='Image/'),
        ),
    ]
