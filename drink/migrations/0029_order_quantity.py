# Generated by Django 3.1.7 on 2021-03-28 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drink', '0028_auto_20210322_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]