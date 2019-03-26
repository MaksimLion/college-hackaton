from django.db import models
from authentification import Subject

# Create your models here.
class BenefitLink(models.Model):
    title = models.CharField(max_length=300, verbose_name="Название")
    text = models.TextField(verbose_name="Описание ресурса")
    url = models.URLField(max_length=250, verbose_name="Ссылка")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="Предмет")
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Полезная ссылка"
        verbose_name_plural = "Полезные ссылки"

       
class Book(models.Model):
    title = models.CharField(max_length=300, verbose_name="Название")
    text = models.TextField(verbose_name="Описание")
    file = models.FileField(upload_to="books/")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="Предмет")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги" 


