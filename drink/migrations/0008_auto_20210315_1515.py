# Generated by Django 3.1.7 on 2021-03-15 12:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('drink', '0007_auto_20210315_1437'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(help_text='Choose a town or city you live in: *Do not fill this filed*', max_length=150)),
                ('area', models.CharField(help_text='Choose correct location you live in that town: *Do not fill this filed*', max_length=150)),
                ('delivery_method', models.CharField(choices=[('Door delivery', 'Door delivery'), ('Pick up station', 'Pick up station')], help_text='Do not fill this field', max_length=150)),
            ],
            options={
                'verbose_name_plural': 'Order, location and delivery',
            },
        ),
        migrations.AlterField(
            model_name='drink',
            name='delivered',
            field=models.BooleanField(blank=True, help_text='*Do not fill this field*', null=True),
        ),
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.AddField(
            model_name='order',
            name='drink',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='drink.drink'),
        ),
        migrations.AddField(
            model_name='order',
            name='ordered_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]