from django.db import models
from django.db.models.expressions import OrderBy
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Author(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Publisher(models.Model):

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Publishers'

    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.name} ({self.short_name})"


class Book(models.Model):

    class Meta:
        ordering = ['title']
        verbose_name_plural = 'Books'

    title = models.CharField(max_length=50)
    description = models.TextField()
    available = models.BooleanField(default=True)
    publication_year = models.IntegerField()
    author = ForeignKey(Author, on_delete=models.CASCADE)
    isbn_no = models.CharField(max_length=13, null=True, blank=True)
    publisher = ForeignKey(Publisher, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.title}"

