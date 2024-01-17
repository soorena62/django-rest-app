from django.db import models
from django.db.models.base import Model
# Create your models here:


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    id_code = models.CharField(max_length=50)

    def __str__(self):
        return {self.first_name}, {self.last_name}
