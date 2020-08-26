from django.db import models
from django.contrib.auth.models import User


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Post(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='post/photos')

    def __str__(self):
        return '{} by @{}'.format(self.title, self.user.username)