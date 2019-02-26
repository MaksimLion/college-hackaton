from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Subject(models.Model):
    name = models.CharField(max_length=10, verbose_name="Название")


class Achievement(models.Model):
    
    WINNER = 'winner'
    PARTICIPANT = 'participant'
    OPTIONS = (
        (WINNER,'Призёр'),
        (PARTICIPANT, 'участник')
    )

    name = models.CharField(max_length=20)
    text = models.TextField()
    option = models.CharField(max_length=20, choices=OPTIONS)


class Technology(models.Model):
    
    LANGUAGE = 'lang'
    CMS = 'cms'
    TOOL = 'tool'
    ENGINE = 'engine'
    DB = 'database'

    OPTIONS = (
        (LANGUAGE, 'Язык программирования'),
        (CMS, 'CMS Система'),
        (TOOL, 'Инструмент'),
        (ENGINE, 'Движок'),
        (DB, 'База данных')
    )

    name = models.CharField(max_length=10, verbose_name="Название")
    logo = models.ImageField(blank=True, upload_to="technologies/logo", verbose_name="Логотип")
    option = models.CharField(max_length=10, choices=OPTIONS, verbose_name="Тип")


class ItCompany(models.Model):

    name = models.CharField(max_length=20)
    logo = models.ImageField(blank=True, verbose_name="Логотип", upload_to="companies/logo")


class Profile(models.Model):

    SEX = (
        ('m', "Мужской"),
        ('g', "Женский")
    )

    sex = models.CharField(max_length=1, choices=SEX, verbose_name="Пол")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.CharField(max_length=10, verbose_name="Группа")
    skills = models.ManyToManyField(Technology, verbose_name="Стек технологий")
    career = models.ManyToManyField(ItCompany, verbose_name="Карьера")
    achievements = models.ManyToManyField(Achievement, verbose_name="Достижения")
    favorite_subject = models.ManyToManyField(Subject, verbose_name="Любимые предметы")
    mark = models.CharField(max_length=3, default='0.0', verbose_name="Средний балл")


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()







