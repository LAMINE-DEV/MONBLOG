from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telephone = models.IntegerField()
    photo=models.ImageField(upload_to='profile_image/',default='profile_image/default.webp',null=True,blank=True)
    choix=(('Etudiant','Etudiant'),('Professeur','Professeur'),)
    profession=models.CharField(max_length=100,choices=choix,default='')
    datetime=models.DateTimeField(auto_now_add=True)





