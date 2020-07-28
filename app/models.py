from django.db import models

class User(models.Model):
    username = models.CharField(max_length=60,unique=True)
    password = models.CharField(max_length=1000)

    @classmethod
    def create(cls, username,password):
        user = cls(username=username, password=password)
        return user

    class Meta:
        db_table = "user"

class Websites(models.Model):
    userId = models.ManyToManyField(User)
    websiteName = models.CharField(max_length=250,unique=True)
    websiteUsername = models.CharField(max_length=60)
    websitePassword = models.CharField(max_length=1000)

    @classmethod
    def create(cls,websiteName, websiteUsername,websitePassword):
        website = cls(websiteName=websiteName, websiteUsername=websiteUsername, websitePassword=websitePassword)
        return website

    class Meta:
        db_table = "websites"

