from django.db import models
from django.contrib.auth.models import User
from authentication.models import Subject, Profile


# class Test(models.Model):
#     title = models.CharField(max_length=30, verbose_name="Название")
#     subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
#     questions = models.ArrayField()
    
#     def __str__(self):
#         return self.title

#     class Meta:
#         verbose_name = "Тест"
#         verbose_name_plural = "Тесты"
    

# class Lab(models.Model):
#     title = models.CharField(max_length=30, verbose_name="Название")
#     read_file = models.FileField(upload_to="materials/", verbose_name="Методичка")

#     def __str__(self):
#         return self.title

#     class Meta:
#         verbose_name = "Лабораторная работа"
#         verbose_name_plural = "Лабораторные работы"


class Report(models.Model):
    STATUSES = (
        ('Зачёт','Зачёт'),
        ('На проверке', 'На проверке'),
        ('Незачёт', 'Незачёт')
    )
    
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, blank=True, null=True)
    name_executor = models.CharField(max_length=100, verbose_name="Исполнитель")
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    group = models.CharField(max_length=10, verbose_name="Группа")
    title = models.CharField(max_length=30, verbose_name="Название")
    file = models.FileField(upload_to="reports/", verbose_name="Отчёт")
    status = models.CharField(max_length=100, default='Незачёт', choices=STATUSES)

    def __str__(self):
        return self.name_executor + '---' + self.group + '---' + self.title

    class Meta:
        verbose_name = "Отчёт"
        verbose_name_plural = "Отчёты"


