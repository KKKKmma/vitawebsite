# Generated by Django 3.1.7 on 2021-11-11 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Merchandise',
            fields=[
                ('merchandise_number', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('reservation_date', models.DateField()),
                ('reservation_time', models.DateTimeField()),
                ('stock', models.BooleanField(default=True)),
            ],
        ),
    ]
