from django.db import models

# Create your models here.
from .validators import validate_author


class PostModel(models.Model):
    author = models.CharField(
        max_length=20,
        null=False,
        validators=[validate_author])

    judul = models.CharField(max_length=20)
    body = models.TextField()

    LIST_CATEGORY = (
        ('jurnal', 'jurnal'),
        ('berita', 'berita'),
        ('blog', 'blog')
    )
    category = models.CharField(
        max_length=20,
        choices=LIST_CATEGORY,
        default='blog'
    )

    publish = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}.{}'.format(self.id, self.judul)
