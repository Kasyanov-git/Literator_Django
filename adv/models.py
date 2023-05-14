from django.db import models

class Articles(models.Model):
    title = models.CharField('Название статьи', max_length=200)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Полный текст')
    date = models.DateField('Дата публикации')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Статья от рекламодателя'
        verbose_name_plural = 'Статьи от рекламодателя'