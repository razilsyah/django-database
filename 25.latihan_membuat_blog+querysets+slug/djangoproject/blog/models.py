from django.db import models

from django.utils.text import slugify
# Create your models here.


# membuat tabel pada database
class Post(models.Model):
    judul = models.CharField(max_length=200)
    body = models.TextField()
    category = models.CharField(max_length=200)
    publish = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, editable=False)

    # method slugify
    def save(self):
        self.slug = slugify(self.judul)
        super(Post, self).save()

    def __str__(self):
        return '{}. {}'.format(self.id, self.judul)
