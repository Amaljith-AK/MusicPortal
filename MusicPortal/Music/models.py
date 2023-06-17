from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class SongsModel(models.Model):
    title=models.CharField(max_length=100)
    singers=models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='album_image')
    song=models.FileField(upload_to='uploaded_songs')
    options=[
        ('public','public'),
        ('private','private'),
        ('protected','protected'),
    ]
    upload_type=models.CharField(max_length=50,choices=options,default='public')
    share_to=models.EmailField(max_length=100,null=True)