# Generated by Django 3.0.8 on 2020-08-27 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20200827_1831'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='img_url',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='listing',
            name='description',
            field=models.CharField(blank=True, max_length=2000),
        ),
    ]