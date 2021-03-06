from django.db import models
from django.contrib.auth.models import User as AdminUser


class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.top_name


class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE,)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name


class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE,)
    date = models.DateField()

    def __str__(self):
        return str(self.date)


class User(models.Model):
    first_name = models.CharField(max_length=264)
    last_name = models.CharField(max_length=264)
    email = models.CharField(max_length=264)
    
    def __str__(self):
        return "{} {} ({})".format(self.first_name, self.last_name, self.email)


class UserProfileInfo(models.Model):
    user = models.OneToOneField(AdminUser, on_delete=models.CASCADE,)

    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.username
    