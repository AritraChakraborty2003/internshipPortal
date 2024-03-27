# Generated by Django 4.2.7 on 2024-03-27 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='intern',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('internId', models.IntegerField()),
                ('pid', models.IntegerField()),
                ('project', models.TextField()),
                ('domain', models.TextField()),
                ('duration', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.IntegerField()),
                ('project', models.TextField()),
                ('domain', models.TextField()),
                ('duration', models.IntegerField()),
            ],
        ),
    ]