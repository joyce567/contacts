from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
from django.contrib.auth.models import User


# Create your models here.
class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=45)
    email = models.EmailField()
    telephone = models.CharField(max_length=15)
    relation = models.CharField(max_length=45)
    residence = models.CharField(max_length=45)
    cover = models.FileField()
    is_male = models.BooleanField(default=True)
    created = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('contacts:contact-index')

