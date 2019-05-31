from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Application(models.Model):
    name  = models.CharField(max_length=20)
    category = models.ForeignKey('Category', related_name='category', on_delete=models.CASCADE)


    def __str__(self):
        return self.name