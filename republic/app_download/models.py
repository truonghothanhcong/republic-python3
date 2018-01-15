from django.db import models


class Video(models.Model):
    name = models.CharField(max_length=256)
    url = models.CharField(max_length=256)
    long_seconds = models.IntegerField()
    source = models.CharField(max_length=128)
    description = models.CharField(max_length=500)
    url_image = models.CharField(max_length=300)

    class Meta:
        db_table = 'video'
