from django.db import models
from django.conf import settings
from django.utils import timezone

class noticias(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class profissionais(models.Model):
    name = models.CharField(max_length = 200)
    interesse = models.CharField(max_length = 200)
    habilidade = models.TextField()

    def __str__(self):
        return self.title
# Create your models here.
