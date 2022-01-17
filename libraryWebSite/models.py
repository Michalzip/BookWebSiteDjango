from django.db import models

# Create your models here.

class Book(models.Model):
    title=models.CharField(max_length=40)
    price=models.FloatField()
    isAvailable=models.BooleanField(default=True)
    #jesli nie bedzie zadnego autor powiazanego z ksiazką ustaw mu null
    author=models.ForeignKey('Author',on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return f'{self.title} ,{self.price},{self.author},{self.isAvailable}'


class Author(models.Model):
    first_name=models.CharField(max_length=40)
    last_name=models.CharField(max_length=50)
    date_of_birth=models.DateField(null=True,blank=True)
    date_of_death=models.DateField('Died',null=True,blank=True)
    def __str__(self):
        return f'{self.first_name},{self.last_name}'