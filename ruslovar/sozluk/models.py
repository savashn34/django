from django.db import models
from django.utils.text import slugify
from unidecode import unidecode

# Create your models here.

class Sesler(models.Model):
    ses = models.CharField(max_length=50)
    slug = models.SlugField(null=True, blank=True, unique=True, db_index=True)

    def __str__(self):
        return self.ses
    
class Diller(models.Model):
    dil = models.CharField(max_length=50)
    slug = models.SlugField(null=True, blank=True, unique=True, db_index=True)

    def __str__(self):
        return self.dil
    
class Sozcukler(models.Model):
    sozcuk = models.CharField(max_length=50)
    koken = models.CharField(max_length=50)
    anlam = models.TextField()
    karsilik = models.CharField(null=False, max_length=200)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True)
    ses = models.ForeignKey(Sesler, null=True, on_delete=models.CASCADE, related_name='sozcukler_ses')
    dil = models.ForeignKey(Diller, null=True, on_delete=models.CASCADE, related_name='sozcukler_dil')

    def __str__(self):
        return f"{self.sozcuk}"

    def save(self, *args, **kwargs):
        slug_text = unidecode(self.sozcuk)
        self.slug = slugify(slug_text)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['sozcuk']