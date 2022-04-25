# Generated by Django 3.2.8 on 2022-03-24 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.IntegerField()),
                ('order_list', models.CharField(max_length=50)),
                ('payment_statue', models.BooleanField(default=False)),
                ('send_mail', models.BooleanField(default=False)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.member')),
                ('member_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_member_name', to='home.member')),
                ('phone_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_phone_number', to='home.member')),
                ('reserver_date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_reserver_date', to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('quantity', models.IntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='order.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='product.product')),
            ],
        ),
    ]
