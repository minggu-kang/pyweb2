# Generated by Django 3.2.5 on 2021-07-27 01:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0011_question_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='image',
        ),
    ]
