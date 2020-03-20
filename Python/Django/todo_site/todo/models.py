from django.db import models
from django.utils import timezone
# Create your models here.
class Todo(models.Model):
    title = models.CharField(=100)
    details = models.TextField()
    date = models.DateTimeField(default=timezone.now())
    def __str__(self):
        return self.titlemax_length

