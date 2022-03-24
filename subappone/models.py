from django.db import models
from datetime import datetime
from cloudinary.models import CloudinaryField


class Picture(models.Model):
    image = CloudinaryField('image')


class Post(models.Model):
    class Meta(object):
        db_table = 'post'

    name = models.CharField(
        'Name', blank=False, null=False, max_length=14, db_index=True, default='Anonymous'
    )

    body = models.CharField(
        'Body', blank=True, null=True, max_length=140, db_index=True
    )

    image = CloudinaryField(
        'Image', blank=True
    )
                                            
    like = models.IntegerField (
        'like_count', default = 0, blank = True
    )
    created_at = models.DateTimeField(
        'Created DateTime', blank=True, auto_now_add=True
    )
