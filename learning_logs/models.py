from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    """Тема которую изучает пользователь"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Возращаем строковое предст модели"""
        return self.text


class Entry(models.Model):
    """инфо изученая польльзователем по теме"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Возращает строковое представление модели"""
        if self.text > str(200):
            return f'{self.text[:50]}...'
        else:
            self.text < str(200)
            return self.text
