from django.db import models

from .choises import STATUS, TYPE
from ase_site.auth_core.models import User


class Company(models.Model):
    id = models.AutoField('ИД организации', primary_key=True, editable=False)
    name = models.CharField('Название организации', max_length=100)

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
        ordering = ('name',)

    def __str__(self):
        return str(self.name)


class GPS(models.Model):
    id = models.IntegerField('ИД Датчика', primary_key=True, editable=True)

    class Meta:
        verbose_name = 'ИД Датчика'
        verbose_name_plural = 'ИД Датчиков'

    def __str__(self):
        return str(self.id)


class Car(models.Model):
    id = models.AutoField('ИД Машины', primary_key=True, editable=False)
    car_type = models.CharField('Тип Машиы', max_length=120)
    gps = models.ForeignKey(GPS, on_delete=models.DO_NOTHING, verbose_name='ИД Датчика')

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'

    def __str__(self):
        return str(self.id)


class GPSdata(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    id_gps = models.ForeignKey(GPS, on_delete=models.DO_NOTHING)
    date = models.DateTimeField('Дата/время', editable=False, auto_now_add=True)
    latitude = models.CharField('Широта', editable=False, blank=False, max_length=50)
    longitude = models.CharField('Долгота', editable=False, blank=False, max_length=50)

    class Meta:
        verbose_name = 'Данные Датчика'
        verbose_name_plural = 'Данные Датчиков'

    def __str__(self):
        return str(self.id)


class ApplicationForm(models.Model):
    status = models.IntegerField('На Какой Стадии Находится Заявка', choices=STATUS)
    application_type = models.CharField('Тип Заявки', choices=TYPE)
    density = models.FloatField('Плотность материала')
    volume = models.FloatField('Объем')
    delivery_date = models.DateField('Дата Поставки')
    delivery_time = models.TimeField('Время Поставки')
    car = models.ForeignKey(Car, on_delete=models.DO_NOTHING, verbose_name='Машина')
    manufacturer_org = models.ForeignKey(Company, on_delete=models.DO_NOTHING, verbose_name='Организация Изготовитель')
    performing_org = models.ForeignKey(Company, on_delete=models.DO_NOTHING, verbose_name='Организация Исполнитель')
    application_sender = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Заявитель')
    application_receiver = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Заявку Принял')
    ocr_specialist = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Специалист ОСР')

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
