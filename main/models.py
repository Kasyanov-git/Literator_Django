from django.db import models


class Feedback(models.Model):
    title = models.CharField('Как к тебе обращаться?', max_length=200)
    anons = models.CharField('Тема послания...', max_length=250)
    full_text = models.TextField('Отзывы, предложения о сотрудничестве и конструктивную критику приветствуем!')
    email = models.EmailField('Если ждёшь ответ, оставляй почту', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'
