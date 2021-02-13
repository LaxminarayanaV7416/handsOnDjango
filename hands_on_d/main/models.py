from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Post(models.Model):
    content = RichTextUploadingField(blank=True, null = True)