from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,  # As the foriegn key, ie author is deleted this model also gets deleted
    )

    def __str__(self):
        return self.title[0:50]

    def get_absolute_url(self):
        return reverse("article_detail", args=[str(self.id)])
