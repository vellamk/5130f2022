from django.db import models


# Create your models here.

class LogIn(models.Model):
    user_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.user_name


class OverAll(models.Model):
    total_score = models.IntegerField(default=0)


class decision(models.Model):
    purpose = models.CharField(max_length=100)
    primary = models.CharField(max_length=100)
    millage = models.IntegerField
    price = models.IntegerField
    location = models.CharField(max_length=100)
