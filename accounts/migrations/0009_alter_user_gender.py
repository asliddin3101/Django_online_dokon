# Generated by Django 3.2.5 on 2021-12-02 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_user_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('f', 'female'), ('m', 'male')], default='m', max_length=10, null=True),
        ),
    ]
