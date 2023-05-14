from django.db import models
from django.db import models

class SearchingBooks(models.Model):
    title_ru = models.CharField('Название_ru', max_length=150)
    title_ru_low = models.CharField('Название_ru', max_length=150)
    title_en = models.CharField('Название_en', max_length=150)
    title_en_low = models.CharField('Название_en', max_length=150)
    book_author = models.CharField('Автор', max_length=150)
    anons = models.CharField('Превью', max_length=250)
    icon = models.ImageField(upload_to='try/Textonator/media/', blank=True)


    def get_absolute_url(self):
        return f'/try/{self.id}'

    def __str__(self):
        return self.title_ru

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    @property

    def photo_url(self):
        if self.icon and hasattr(self.icon, 'url'):
            return self.icon.url