from django.db import models
import datetime
# Create your models here.
#title, content, publication date, and author

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content =models.TextField(max_length=500)
    publication_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('Author', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

class Author(models.Model):
    author_name = models.CharField(max_length=20)

    def __str__(self):
        return self.author_name