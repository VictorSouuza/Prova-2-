# Generated by Django 4.2.2 on 2023-06-22 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DatalheDisciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso', models.CharField(max_length=100)),
                ('disciplina', models.CharField(max_length=100)),
            ],
        ),
    ]
