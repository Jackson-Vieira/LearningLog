from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    """Um assunto sobre o qual o usuário está aprendendo."""

    title = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=200)
    thumbnail = models.ImageField(upload_to='thumbnails/', null=True, blank=True)

    def __str__(self):
        return self.title

class Entry(models.Model):
    """ Algo específico aprendido sobre um assunto. """

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    header = models.CharField('header', blank=True, null=False, max_length=50)
    text = models.TextField('text', blank=False, null=False, default="text entry")
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.text