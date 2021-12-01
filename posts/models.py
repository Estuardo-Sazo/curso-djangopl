from django.db import models
from django.contrib.auth.models import User

from users.models import Profile

# Create your models here.
class User(models.Model):
    id=models.AutoField(primary_key=True)
    email=models.EmailField(max_length=100, verbose_name='Email', unique=True)
    password=models.CharField(max_length=100, verbose_name='Password', null=True)

    first_name=models.CharField(max_length=100, verbose_name='First Name', null=True)
    last_name=models.CharField(max_length=100, verbose_name='Last Name', null=True)

    bio = models.TextField()
    is_admin=models.BooleanField(default=False)
    birth_date = models.DateField(blank=True, null=True)

    created= models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Post(models.Model):
    id=models.AutoField(primary_key=True)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    profile= models.ForeignKey('users.Profile', on_delete=models.CASCADE)
    title= models.CharField(max_length=255)
    photo= models.ImageField(upload_to='posts/photos')
    created= models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} by @{}'.format(self.title, self.user.usarname)