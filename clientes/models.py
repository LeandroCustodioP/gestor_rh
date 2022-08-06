from tokenize import blank_re
from django.db import models
from sqlalchemy import null, true

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    bio = models.TextField()
    photo = models.ImageField(upload_to = 'clientes_photos', null=true , blank = true)

    def __str__(self):
        return self.first_name + ' ' + self.last_name