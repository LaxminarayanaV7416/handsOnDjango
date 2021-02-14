from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
import datetime
# Create your models here.

class Post(models.Model):
    content = RichTextUploadingField(blank=True, null = True)

    def __str__(self):
        return f'post_id-{self.id} - {datetime.datetime.now()}'

class Header(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(null = True, blank = True)
    name = models.CharField(max_length = 50)

    def __str__(self):
        return f'{self.name}_{self.email}'

class Footer(models.Model):
    page = models.IntegerField(null=True, blank = True)
    text = models.TextField(null=True, blank = True)

    def __str__(self):
        return f'{self.page}_{self.text}'

def get_latest_header():
    try:
        header = list(Header.objects.all())[-1]
        return {'date':header.date, 'email': header.email, 'name':header.name}
    except Exception:
        return {'date':'', 'email': '', 'name':''}

def get_latest_footer():
    try:
        header = list(Footer.objects.all())[-1]
        return {'page':header.page, 'text':header.text }
    except Exception:
        return {'page':'', 'text':'' }

def get_latest_post():
    try:
        header = list(Post.objects.all())[-1]
        return header.content
    except Exception:
        return 'No Post was created so displaying DEFAULT TEXT as content'