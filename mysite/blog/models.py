from django.db import models
from django.urls import reverse
class Post(models.Model):
    baslik = models.CharField(max_length=200)
    icerik = models.TextField()
    tarih = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('icerik', kwargs={'id': self.id})

    def __str__(self):
        return self.baslik
# Create your models here.
