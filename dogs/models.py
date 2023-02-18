from django.db import models

class Dog(models.Model):
    name = models.CharField(max_length=200)
    species = models.CharField(max_length=200)
    age = models.IntegerField()
    sex = models.CharField(max_length=20)
    intake_date = models.DateTimeField(auto_now_add=True)
    fertile = models.BooleanField()
    picture = models.URLField(null=True)
    status = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} {self.age}"

class AdoptionForm(models.Model):
    name = models.CharField(max_length=200)
    dog_id = models.IntegerField()
    application_status = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} application status for dog: {self.dog_id} is: {self.application_status}"
