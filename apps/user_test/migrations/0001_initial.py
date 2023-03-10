# Generated by Django 4.1.7 on 2023-03-12 13:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id_user', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя пользователя')),
                ('last_name', models.CharField(max_length=100, verbose_name='Фамилиия пользователя')),
                ('user_email', models.CharField(max_length=200, verbose_name='Электронная почта')),
                ('user_password', models.CharField(max_length=100, verbose_name='Пароль')),
                ('delivery_address', models.CharField(max_length=100, verbose_name='адрес доставки')),
                ('phone_number', models.CharField(max_length=100, verbose_name='Номер телефона')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
