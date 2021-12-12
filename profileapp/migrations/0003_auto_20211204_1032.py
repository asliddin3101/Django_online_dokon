# Generated by Django 3.2.5 on 2021-12-04 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0002_auto_20211204_1022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientprofile',
            name='first_name',
        ),
        migrations.AddField(
            model_name='clientprofile',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]