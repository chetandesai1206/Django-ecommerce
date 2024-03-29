# Generated by Django 4.2.7 on 2023-11-19 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.IntegerField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=55)),
                ('category', models.CharField(choices=[('Surf', 'S'), ('Bar', 'B'), ('Toothpaste', 'T')], default='', max_length=100)),
                ('desc', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='pics')),
            ],
        ),
    ]
