# Generated by Django 4.1.3 on 2022-12-17 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0003_rename_tasl_review_task'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
