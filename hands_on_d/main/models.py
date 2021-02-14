from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
import datetime
from django.conf import settings
from tinymce import models as tinymce_models

from tinymce.models import HTMLField
# Create your models here.

class Post(models.Model):
    content = tinymce_models.HTMLField()

    def __str__(self):
        return f'post_id-{self.id} - {datetime.datetime.now()}'

class Header(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(null = True, blank = True)
    name = models.CharField(max_length = 50)
    image = models.ImageField(default='default.png', upload_to='uploads')

    def __str__(self):
        return f'{self.name}_{self.email}'

class Footer(models.Model):
    page = models.IntegerField(null=True, blank = True)
    text = models.TextField(null=True, blank = True)
    image = models.ImageField(default='default_footer.png', upload_to='uploads')

    def __str__(self):
        return f'{self.page}_{self.text}'

def get_latest_header():
    try:
        header = list(Header.objects.all())[-1]
        image = f'{settings.BASE_DIR}/{header.image.url}'
        return {'date':header.date, 'email': header.email, 'name':header.name, 'image':image,'image_path':header.image}
    except Exception as err:
        print(err)
        return {'date':'', 'email': '', 'name':'', 'image':'','image_path':''}

def get_latest_footer():
    try:
        header = list(Footer.objects.all())[-1]
        image = f'{settings.BASE_DIR}/{header.image.url}'
        return {'page':header.page, 'text':header.text, 'image':image,'image_path':header.image}
    except Exception:
        return {'page':'', 'text':'', 'image':'','image_path':''}

def get_latest_post():
    try:
        header = list(Post.objects.all())[-1]
        return header.content
    except Exception:
        return 'No Post was created so displaying DEFAULT TEXT as content'