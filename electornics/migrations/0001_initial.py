# Generated by Django 2.2.3 on 2019-07-12 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('barcode', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('qty', models.IntegerField()),
                ('active', models.BooleanField()),
            ],
            options={
                'db_table': 'product_info',
            },
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('products', models.ManyToManyField(to='electornics.Product')),
            ],
            options={
                'db_table': 'vendor_info',
            },
        ),
    ]