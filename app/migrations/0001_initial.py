# Generated by Django 4.2.6 on 2023-12-30 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='shop',
            fields=[
                ('product_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=100)),
                ('price', models.BigIntegerField()),
                ('mobile_no', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.BigIntegerField()),
                ('amount', models.BigIntegerField()),
                ('mfg', models.DateField()),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.shop')),
            ],
        ),
    ]
