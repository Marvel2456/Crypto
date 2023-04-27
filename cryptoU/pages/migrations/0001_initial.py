# Generated by Django 4.2 on 2023-04-27 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('symbol', models.CharField(max_length=20, unique=True)),
                ('price', models.DecimalField(decimal_places=4, max_digits=20)),
                ('change', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
