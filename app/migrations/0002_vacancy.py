# Generated by Django 3.2.9 on 2021-11-28 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('summary', models.CharField(max_length=500)),
                ('salary', models.IntegerField()),
            ],
        ),
    ]
