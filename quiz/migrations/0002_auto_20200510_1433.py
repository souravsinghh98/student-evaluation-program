# Generated by Django 3.0.5 on 2020-05-10 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='category',
            new_name='subject',
        ),
    ]
