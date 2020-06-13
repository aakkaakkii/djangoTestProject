from django.db import models


class Post(models.Model):
    title = models.TextField()
    content = models.TextField()
    thumbnail = models.ImageField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

