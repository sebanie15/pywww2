from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _


# Create your models here.
STATUS =(
    (0, _('Draft')),
    (1, _('Publish')),
)


class Post(models.Model):
    """
    A class to represent post.
    """
    title = models.CharField(max_length=200, unique=True, verbose_name=_("Post's title"))
    slug = models.SlugField(max_length=200, unique=True, verbose_name=_('Slug'))
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', verbose_name=_('Author'))
    update_on = models.DateTimeField(auto_now=True, verbose_name=_('Updated on'))
    content = models.TextField(verbose_name=_('Content'))
    created_on = models.DateTimeField(auto_now_add=True,verbose_name=_('Created on'))
    status = models.IntegerField(choices=STATUS, default=0, verbose_name=_('Status'))
    sponsored = models.BooleanField(default=False, verbose_name=_('Sponsored'))

    class Meta:
        ordering = ['-created_on']
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')

    def __str__(self) -> str:
        return self.title
