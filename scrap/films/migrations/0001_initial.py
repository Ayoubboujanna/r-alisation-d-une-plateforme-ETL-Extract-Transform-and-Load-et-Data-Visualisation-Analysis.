# Generated by Django 4.0.3 on 2022-05-20 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Films',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rang', models.IntegerField(null=True)),
                ('movie_name', models.CharField(max_length=80, null=True)),
                ('year', models.PositiveIntegerField(null=True)),
                ('time', models.PositiveIntegerField(null=True)),
                ('rating', models.PositiveIntegerField(null=True)),
                ('votes', models.BigIntegerField(null=True)),
                ('gross', models.CharField(max_length=80, null=True)),
                ('director', models.CharField(max_length=100, null=True)),
                ('stars', models.TextField(null=True)),
            ],
        ),
    ]
