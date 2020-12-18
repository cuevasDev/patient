from django.db import models

# Create your models here.
class Base(models.Model):
    id = models.CharField(max_length=13, primary_key=True)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    password = models.CharField(max_length=999)

    def __str__(self):
        return f'{self.firstName} {self.lastName}'


class Patient(Base):
    trustedContact =  models.ForeignKey("Patient", null=True, blank=True, on_delete=models.CASCADE)
    age = models.IntegerField(null=True)
    phone = models.CharField(max_length=11, null=True)
    address = models.CharField(max_length=999, null=True)
    email = models.CharField(max_length=100, null=True)
    photo = models.ImageField(default="image.jpeg", null=True, blank=True)
    verification = models.BooleanField(default=False)

