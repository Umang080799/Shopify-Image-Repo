from django.db import models

class imageRepo(models.Model):
    # Sets the colums of the database
    title = models.CharField(max_length=100)
    upload = models.ImageField(upload_to='images/')
