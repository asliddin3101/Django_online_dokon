# Generated by Django 3.2.5 on 2021-11-01 15:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shopping', '0010_auto_20211101_1755'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wishlist',
            old_name='created_at',
            new_name='added_date',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='color',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='reduced_price',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='size',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='wishlist',
            name='slug',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='wishlist',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
