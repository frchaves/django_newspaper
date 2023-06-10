from django.db import models

from techtest.author.models import Author
# from .author.models import Author


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    regions = models.ManyToManyField(
        'regions.Region', related_name='articles', blank=True
    )
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True)

    # class Meta:
    #     app_label = 'articles'

