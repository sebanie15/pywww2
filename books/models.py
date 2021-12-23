from django.db import models
from django.utils.translation import gettext as  _
from django.db.models.expressions import OrderBy
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Author(models.Model):
    """
    A class to represent Author
    """
    first_name = models.CharField(max_length=50, verbose_name=_('First name'))
    last_name = models.CharField(max_length=50, verbose_name=_('Last name'))

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Publisher(models.Model):
    """
    A class to represent Publishers
    """
    class Meta:
        ordering = ['name']
        verbose_name = _('Publisher')
        verbose_name_plural = _('Publishers')

    name = models.CharField(max_length=255, verbose_name=_('Publisher name'))
    short_name = models.CharField(max_length=50, verbose_name=_('Short name'))

    def __str__(self) -> str:
        return f"{self.name} ({self.short_name})"


class Book(models.Model):
    """
    A class to represent book model.
    """
    class Meta:
        ordering = ['title']
        verbose_name = _('Book')
        verbose_name_plural = _('Books')

    title = models.CharField(max_length=200, verbose_name=_("Book's title"))
    description = models.TextField(verbose_name=_('Description'))
    available = models.BooleanField(default=True, verbose_name=_('Available'))
    publication_year = models.IntegerField(verbose_name=_('Publication year'))
    author = ForeignKey(Author, on_delete=models.CASCADE, verbose_name=_('Author'))
    isbn_no = models.CharField(max_length=13, null=True, blank=True, verbose_name=_('ISBN no.'))
    publisher = ForeignKey(Publisher, on_delete=models.CASCADE, verbose_name=_('Publisher'))

    def __str__(self) -> str:
        return f"{self.title}"

