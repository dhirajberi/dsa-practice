# Generated by Django 4.0.4 on 2022-04-18 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sde_sheet', '0005_remove_question_notes_dsa_notes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dsa',
            name='notes',
        ),
    ]
