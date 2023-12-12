from django.db import models

# Create your models here.

class Enroller(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=60)
    number = models.IntegerField(max_length=10)
    age = models.IntegerField(max_length=10)
    msg = models.CharField(max_length=500)
    confirm = models.BooleanField(default=False)
    wait = models.BooleanField(default=False)
    date = models.DateField(("Date"), auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

    
    def __str__(self):
        return self.name