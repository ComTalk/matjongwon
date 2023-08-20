from django.db import models
from places.models import Place
from users.models import User

class Like(models.Model):
    '''Liked Places'''
    place = models.OneToOneField(Place, related_name='likes', on_delete=models.CASCADE, to_field='id', db_constraint=False)
    users = models.ManyToManyField(User, related_name='liked_places')

    def __str__(self):
        return str(self.place.name)

class DisLike(models.Model):
    '''Disliked Places'''
    place = models.OneToOneField(Place, related_name='dislikes', on_delete=models.CASCADE, to_field='id', db_constraint=False)
    users = models.ManyToManyField(User, related_name='disliked_places')

    def __str__(self):
        return str(self.place.name)
