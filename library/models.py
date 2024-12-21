from django.db import models

# Create your models here.
class Author(models.Model):
    first_name= models.CharField(max_length=20)
    last_name= models.CharField(max_length=20)
    birthday= models.DateField()
    description= models.TextField()
    
    def __str__(self):
        return self.first_name
    

class Book(models.Model):
    title= models.CharField(max_length=100)
    genre= models.CharField(max_length=40)
    version= models.SmallIntegerField()
    section= models.CharField(max_length=40)
    description= models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE,default=None)
    def __str__(self):
        return self.title
    




