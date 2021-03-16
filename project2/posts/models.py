from django.db import models

# Create your models here.
class Post(models.Model):
    text = models.TextField()
    # this will define content in post object.
    def __str__(self):
        return self.text[:50]