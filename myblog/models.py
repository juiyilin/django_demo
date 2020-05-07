from django.db import models

# Create your models here.
from django.utils import timezone


class Post(models.Model):
    text = models.TextField(default='')
    name = models.CharField(default='no name', max_length=20)
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.text

