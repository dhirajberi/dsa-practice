# Generated by Django 4.0.4 on 2022-04-17 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sde_sheet', '0002_tags_question'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tags',
            new_name='Tag',
        ),
    ]