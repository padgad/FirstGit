# Generated by Django 2.1.2 on 2018-11-12 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('sex', models.CharField(max_length=200)),
                ('survived', models.BooleanField()),
                ('age', models.FloatField()),
                ('ticket_class', models.PositiveSmallIntegerField()),
                ('embarked', models.CharField(max_length=200)),
            ],
        ),
    ]
