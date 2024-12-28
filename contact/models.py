from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=24, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    descripition = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(upload_to='pictures/%Y/%m', blank=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True, blank=True
        )

    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name
