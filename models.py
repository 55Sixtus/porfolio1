from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    content = models.TextField(max_length=180)
    number = models.CharField(max_length=13)

    def __self__(self):
        return(self.name)
