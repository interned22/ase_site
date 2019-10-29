# Generated by Django 2.2.6 on 2019-10-28 20:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, verbose_name='ИД организации')),
                ('name', models.CharField(max_length=100, verbose_name='Название организации')),
            ],
            options={
                'verbose_name': 'Организация',
                'verbose_name_plural': 'Организации',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='GPS',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='ИД Датчика')),
            ],
            options={
                'verbose_name': 'ИД Датчика',
                'verbose_name_plural': 'ИД Датчиков',
            },
        ),
        migrations.CreateModel(
            name='GPSdata',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата/время')),
                ('latitude', models.CharField(editable=False, max_length=50, verbose_name='Широта')),
                ('longitude', models.CharField(editable=False, max_length=50, verbose_name='Долгота')),
                ('id_gps', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='data.GPS')),
            ],
            options={
                'verbose_name': 'Данные Датчика',
                'verbose_name_plural': 'Данные Датчиков',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, verbose_name='ИД Машины')),
                ('car_type', models.CharField(max_length=120, verbose_name='Тип Машиы')),
                ('gps', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='data.GPS', verbose_name='ИД Датчика')),
            ],
            options={
                'verbose_name': 'Машина',
                'verbose_name_plural': 'Машины',
            },
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'Отклонено'), (2, 'На рассмотрении'), (3, 'Одобрено')], verbose_name='На Какой Стадии Находится Заявка')),
                ('application_type', models.IntegerField(choices=[(1, 'Бетон'), (2, 'Песок'), (3, 'ПГС')], verbose_name='Тип Заявки')),
                ('density', models.FloatField(verbose_name='Плотность материала')),
                ('delivery_date', models.DateField(verbose_name='Дата Поставки')),
                ('delivery_time', models.TimeField(verbose_name='Время Поставки')),
                ('volume', models.FloatField(verbose_name='Объем')),
                ('ocr_specialist', models.CharField(max_length=120, verbose_name='Специалист ОСР')),
                ('application_receiver', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='application_receiver', to=settings.AUTH_USER_MODEL, verbose_name='Заявку Принял')),
                ('application_sender', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='application_sender', to=settings.AUTH_USER_MODEL, verbose_name='Заявитель')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='data.Car', verbose_name='Машина')),
                ('manufacturer_org', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='manufacturer_org', to='data.Company', verbose_name='Организация Изготовитель')),
                ('performing_org', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='performing_org', to='data.Company', verbose_name='Организация Исполнитель')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
    ]
