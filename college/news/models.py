from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    text = models.TextField(verbose_name="Описание")
    image = models.ImageField(verbose_name="Изображение", upload_to="news")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


        