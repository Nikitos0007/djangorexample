from django.contrib.auth.models import User
from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
from django.db.models import ForeignKey, CASCADE, CharField


class Garage(models.Model):
    address = CharField(max_length= 200)
    def __str__(self):
        return f'{self.address}'

class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)

    name = models.CharField(max_length=500)
    reg_num = models.CharField(
        max_length=8, validators=[RegexValidator(regex=r"\d{4}\w{2}-\d")])
    user = ForeignKey(User, on_delete=CASCADE)
    garage = ForeignKey(Garage, on_delete=CASCADE)

