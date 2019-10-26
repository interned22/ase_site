# Generated by Django 2.1.7 on 2019-10-26 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Электронная почта')),
                ('first_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Фамилия')),
                ('fathers_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Отчетсво')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')),
                ('is_active', models.BooleanField(default=False, verbose_name='Активирован')),
                ('firm_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название фирмы')),
                ('level', models.IntegerField(blank=True, choices=[(1, 'Прораб'), (2, 'Суб подрядчик'), (3, 'Ген подрядчик'), (0, 'Завод')], null=True, verbose_name='Статус сотрудника')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Стаф')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Админ')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
