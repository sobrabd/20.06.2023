from django.db import models

# - Описать модель “Собака” с полями: кличка собаки, порода, фотография, дата рождения
# - Добавить модель “Порода” с полями: название, описание


class Dog(models.Model):
    name = models.CharField(max_length=100, verbose_name='кличка собаки')
    specie = models.ForeignKey('Spice', on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to="dogs", verbose_name="фото", null=True, blank=True)
    birthdate = models.DateField(null=True, verbose_name='дата рождения')

    def __str__(self):
        return self.name


class Spice(models.Model):
    title = models.CharField(max_length=100, verbose_name='название породы')
    description = models.TextField(null=True, blank=True, verbose_name='описание')

    def __repr__(self):
        return self.title
    
    def __str__(self):
        return self.title

