from django.db import models

class User(models.Model):
    _id = models.CharField(max_length=24, primary_key=True)
