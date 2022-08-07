from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    """Um assunto sobre o qual o usuário está aprendendo."""
    title = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=200)
    image = models.ImageField(upload_to='')

    def __str__(self):
        return self.title

class Entry(models.Model):
    """ Algo específico aprendido sobre um assunto.
        Relacionamento (many-to-one relationship) """

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField(blank=False)
    date_added = models.DateTimeField(auto_now_add=True)

    """Meta armazena informações extras para administrar um modelo"""
    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        if len(self.text) <= 50:
            return self.text
        return self.text[:50] + "..."

