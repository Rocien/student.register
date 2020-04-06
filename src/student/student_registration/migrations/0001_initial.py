# Generated by Django 3.0.4 on 2020-03-27 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('grade', models.CharField(max_length=12)),
                ('address', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=10)),
            ],
        ),
    ]