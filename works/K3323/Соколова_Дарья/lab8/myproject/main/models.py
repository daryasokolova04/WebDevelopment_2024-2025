from django.db import models

# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.CharField(max_length=100, verbose_name='Email')
    message = models.TextField(verbose_name='Сообщение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')

    def __str__(self):
        return f'Сообщение от {self.name}'

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'