# Generated by Django 3.1.7 on 2021-11-12 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
