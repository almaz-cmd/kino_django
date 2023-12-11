# Generated by Django 4.2.7 on 2023-12-10 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_movie_website_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
        migrations.AddField(
            model_name='movie',
            name='session',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
