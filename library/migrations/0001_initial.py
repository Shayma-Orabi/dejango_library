# Generated by Django 5.1.3 on 2024-12-17 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='outher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frist_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('birthday', models.DateField()),
                ('descrbtion', models.TextField()),
            ],
        ),
    ]
