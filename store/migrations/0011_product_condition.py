# Generated by Django 3.2.5 on 2021-10-29 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_product_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='condition',
            field=models.CharField(choices=[('1', 'yangi'), ('2', 'ishlatilgan'), ('3', 'bepul')], default='1', max_length=10),
        ),
    ]
