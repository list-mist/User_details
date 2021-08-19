from django.db import models

# Create your models here.


# Create your models here.
class AddUser(models.Model):
    username=models.CharField(max_length=100,default=None)
    email=models.EmailField(max_length=200,unique=True)
    password=models.CharField(max_length=100,default=None)
    confirm_password=models.CharField(max_length=100,default=None)
    address=models.CharField(max_length=100,default=None)

    class Meta:
        ordering=['email']
    def __str__(self):
        return self.username
