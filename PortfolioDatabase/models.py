from django.db import models

# Create your models here.
class Hobby(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField(max_length = 400)
    image = models.CharField(max_length = 500, default = 'https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg?20200913095930')

    def __str__(self):
        return self.name
    
class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=400)
    image = models.CharField(max_length = 500, default = 'https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg?20200913095930')

    def __str__(self):
        return self.name