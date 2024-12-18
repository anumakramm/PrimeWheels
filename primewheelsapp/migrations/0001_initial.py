# Generated by Django 5.1.4 on 2024-12-18 02:21

import django.contrib.auth.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='LabMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('semester', models.PositiveIntegerField()),
                ('personal_page', models.URLField()),
            ],
            options={
                'ordering': ['first_name'],
            },
        ),
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('shipping_address', models.CharField(blank=True, max_length=300, null=True)),
                ('area', models.CharField(choices=[('W', 'Windsor'), ('LS', 'LaSalle'), ('A', 'Amherstburg'), ('L', 'Lakeshore'), ('LE', 'Leamington'), ('C', 'Chatham-Kent'), ('T', 'Toronto'), ('WL', 'Waterloo')], default='C', max_length=2)),
                ('phone_number', models.CharField(blank=True, max_length=10, null=True)),
                ('interested_in', models.ManyToManyField(to='primewheelsapp.cartype')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=200)),
                ('car_description', models.TextField(blank=True, null=True)),
                ('car_price', models.DecimalField(decimal_places=4, max_digits=10)),
                ('inventory', models.PositiveIntegerField(default=10)),
                ('instock', models.BooleanField(default=True)),
                ('car_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicles', to='primewheelsapp.cartype')),
            ],
        ),
        migrations.CreateModel(
            name='OrderVehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('order_status', models.PositiveIntegerField(choices=[(0, 'Successful'), (1, 'Placed'), (2, 'Shipped'), (3, 'Delivered'), (4, 'Cancelled')], default=1)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='primewheelsapp.buyer')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='primewheelsapp.vehicle')),
            ],
        ),
    ]
