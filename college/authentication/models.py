from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# from virtual_education.models import Report


class Subject(models.Model):
    name = models.CharField(max_length=10, verbose_name="Название")
    
    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"

    def __str__(self):
        return self.name
     


class Achievement(models.Model):
    
    WINNER = 'Призер'
    PARTICIPANT = 'Участник'
    OPTIONS = (
        (WINNER,'Призёр'),
        (PARTICIPANT, 'Участник')
    )

    name = models.CharField(max_length=20)
    text = models.TextField()
    option = models.CharField(max_length=20, choices=OPTIONS)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Достижение"
        verbose_name_plural = "Достижения"


class Technology(models.Model):
    
    LANGUAGE = 'Язык программирования'
    CMS = 'CMS'
    TOOL = 'Инструмент'
    ENGINE = 'Движок'
    DB = 'База данных'

    OPTIONS = (
        (LANGUAGE, 'Язык программирования'),
        (CMS, 'CMS Система'),
        (TOOL, 'Инструмент'),
        (ENGINE, 'Движок'),
        (DB, 'База данных')
    )

    name = models.CharField(max_length=10, verbose_name="Название")
    logo = models.ImageField(blank=True, upload_to="technologies/logo", verbose_name="Логотип")
    option = models.CharField(max_length=30, choices=OPTIONS, verbose_name="Тип")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Технология"
        verbose_name_plural = "Технологии"

    


class ItCompany(models.Model):

    name = models.CharField(max_length=20)
    logo = models.ImageField(blank=True, verbose_name="Логотип", upload_to="companies/logo")

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"

    def __str__(self):
        return self.name


class Profile(models.Model):

    SEX = (
        ('Мужской', "Мужской"),
        ('Женский', "Женский")
    )

    
    phone = models.CharField(max_length=15, verbose_name="Мобильный телефон")
    sex = models.CharField(max_length=10, choices=SEX, verbose_name="Пол")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.CharField(max_length=10, verbose_name="Группа")
    skills = models.ManyToManyField(Technology, verbose_name="Стек технологий")
    career = models.ManyToManyField(ItCompany, verbose_name="Карьера")
    achievements = models.ManyToManyField(Achievement, verbose_name="Достижения")
    favorite_subject = models.ManyToManyField(Subject, verbose_name="Любимые предметы")
    mark = models.CharField(max_length=3, default='0.0', verbose_name="Средний балл")
    photo = models.ImageField(blank=True, upload_to='photos', verbose_name="Аватар")
    # reports = models.ForeignKey(Report, verbose_name="Отчёты", on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "Личные данные"
        verbose_name_plural = "Личные данные"

    def __str__(self):
        return self.user.username

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()







