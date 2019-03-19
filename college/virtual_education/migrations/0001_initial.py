# Generated by Django 2.1.5 on 2019-03-19 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_executor', models.CharField(max_length=100, verbose_name='Исполнитель')),
                ('group', models.CharField(max_length=10, verbose_name='Группа')),
                ('title', models.CharField(max_length=30, verbose_name='Название')),
                ('file', models.FileField(upload_to='reports/', verbose_name='Отчёт')),
            ],
            options={
                'verbose_name': 'Отчёт',
                'verbose_name_plural': 'Отчёты',
            },
        ),
    ]
