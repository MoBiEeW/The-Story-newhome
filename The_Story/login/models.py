from django.db import models

# Create your models here.


class Post(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()


class Story(models.Model):
    namechat1 = models.TextField()
    namechat2 = models.TextField()
    title = models.TextField()
    text1 = models.TextField()
    text2 = models.TextField()
    desc = models.TextField()
    user = models.TextField()
    catergory = models.TextField()


class Test(models.Model):
    name = models.TextField()
