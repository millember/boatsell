# Generated by Django 5.1.1 on 2024-09-24 10:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('boat', '0002_boat_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Имя')),
                ('email', models.EmailField(max_length=150, verbose_name='Почта')),
                ('message', models.TextField()),
                ('closed', models.BooleanField(default=False, verbose_name='Закрыт заказ')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('boat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boat.boat', verbose_name='Лодка')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]
