from django.db import models

# The below is our models here.

class grade(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):  # This function makes grade field to show titles
        return self.title

# Student class
class Student(models.Model):
    name        = models.CharField(max_length=50)
    surname     = models.CharField(max_length=50)
    address     = models.CharField(max_length=200)
    mobile      = models.CharField(max_length=10)
    grade       = models.ForeignKey(grade,on_delete=models.CASCADE)