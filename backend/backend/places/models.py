from django.db import models
from users.models import User
from django.core.exceptions import ObjectDoesNotExist

class Place(models.Model):
    # primary key `id` is specified explicitly
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=64)
    category = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    opening_hours = models.TextField(blank=True, null=True)
    score_navermap = models.TextField(db_column='score.navermap', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    score_kakaomap = models.TextField(db_column='score.kakaomap', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    score_googlemap = models.TextField(db_column='score.googlemap', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    menu = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    reviews_navermap = models.TextField(db_column='reviews.navermap', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    reviews_kakaomap = models.TextField(db_column='reviews.kakaomap', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    reviews_googlemap = models.TextField(db_column='reviews.googlemap', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    thumbnails = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    coordinates_latitude = models.FloatField(db_column='coordinates.latitude')  # Field renamed to remove unsuitable characters.
    coordinates_longitude = models.FloatField(db_column='coordinates.longitude')  # Field renamed to remove unsuitable characters.
    
    def get_total_likes(self):
        try:
            return self.likes.users.count()
        except ObjectDoesNotExist:
            return 0

    def get_total_dislikes(self):
        try:
            return self.dislikes.users.count()
        except ObjectDoesNotExist:
            return 0

    def get_overall_likes(self):
        return self.get_total_likes() - self.get_total_dislikes()

    class Meta:
        managed = False
        db_table = 'seoul'
        unique_together = (('name', 'coordinates_latitude', 'coordinates_longitude'),)

