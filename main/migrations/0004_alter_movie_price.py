# Generated by Django 4.2.7 on 2023-12-10 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_movie_price_movie_session'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]