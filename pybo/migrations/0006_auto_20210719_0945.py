# Generated by Django 3.2.5 on 2021-07-19 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0005_answer_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='modify_data',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='modify_data',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
