
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
class Category(models.Model):
    name = models.CharField(unique=True, max_length=150)


class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    subject = models.CharField(max_length=264)
    message = models.TextField()

class Story(models.Model):
    name = models.CharField(unique=True, max_length=250)
    author = models.CharField(max_length=250)
    url = models.CharField(max_length=200, blank=True, null=True)
    # content = models.TextField()
    content = RichTextUploadingField()
    public_day = models.DateField()
    category = models.ForeignKey(Category, models.DO_NOTHING)
    image = models.ImageField(upload_to='images')

class Subcribe(models.Model):
    email = models.CharField(max_length=254)
    subcribe_day = models.DateField()
