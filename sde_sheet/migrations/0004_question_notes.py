# Generated by Django 4.0.4 on 2022-04-18 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sde_sheet', '0003_rename_tags_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='notes',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
