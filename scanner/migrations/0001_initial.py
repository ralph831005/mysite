# Generated by Django 5.1.3 on 2024-11-19 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt_id', models.IntegerField()),
                ('item', models.CharField(max_length=200)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store', models.CharField(max_length=200)),
                ('total_price', models.FloatField(default=0)),
                ('tax', models.FloatField(default=0)),
                ('tax_rate', models.FloatField(default=0)),
            ],
        ),
    ]