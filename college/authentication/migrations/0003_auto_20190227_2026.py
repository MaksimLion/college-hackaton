# Generated by Django 2.1.7 on 2019-02-27 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_profile_phone'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='achievement',
            options={'verbose_name': 'Достижение', 'verbose_name_plural': 'Достижения'},
        ),
        migrations.AlterModelOptions(
            name='itcompany',
            options={'verbose_name': 'Компания', 'verbose_name_plural': 'Компании'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Личные данные', 'verbose_name_plural': 'Личные данные'},
        ),
        migrations.AlterModelOptions(
            name='subject',
            options={'verbose_name': 'Предмет', 'verbose_name_plural': 'Предметы'},
        ),
        migrations.AlterModelOptions(
            name='technology',
            options={'verbose_name': 'Технология', 'verbose_name_plural': 'Технологии'},
        ),
        migrations.AlterField(
            model_name='achievement',
            name='option',
            field=models.CharField(choices=[('Призер', 'Призёр'), ('Участник', 'Участник')], max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='sex',
            field=models.CharField(choices=[('Мужской', 'Мужской'), ('Женский', 'Женский')], max_length=10, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='technology',
            name='option',
            field=models.CharField(choices=[('Язык программирования', 'Язык программирования'), ('CMS', 'CMS Система'), ('Инструмент', 'Инструмент'), ('Движок', 'Движок'), ('База данных', 'База данных')], max_length=10, verbose_name='Тип'),
        ),
    ]
