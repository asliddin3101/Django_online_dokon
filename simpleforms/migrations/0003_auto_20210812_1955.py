# Generated by Django 3.2.5 on 2021-08-12 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpleforms', '0002_director_filial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255)),
                ('age', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='director',
            name='age',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('release_data', models.DateTimeField()),
                ('actors', models.ManyToManyField(to='simpleforms.Actor')),
            ],
        ),
    ]
