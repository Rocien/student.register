# Generated by Django 3.0.4 on 2020-04-02 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_registration', '0002_auto_20200401_1120'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='contact',
            new_name='mobile',
        ),
    ]