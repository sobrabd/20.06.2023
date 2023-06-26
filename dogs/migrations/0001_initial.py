# Generated by Django 4.2.2 on 2023-06-24 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Spice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='название породы')),
                ('description', models.TextField(null=True, verbose_name='описание')),
            ],
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='кличка собаки')),
                ('image', models.ImageField(null=True, upload_to='dogs', verbose_name='фото')),
                ('birthdate', models.DateField(null=True, verbose_name='дата рождения')),
                ('specie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dogs.spice')),
            ],
        ),
    ]
