# Generated by Django 5.1.2 on 2024-10-31 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoginUsers',
            fields=[
                ('userid', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('user', models.CharField(max_length=10, unique=True)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
