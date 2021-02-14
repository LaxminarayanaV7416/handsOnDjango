from django.contrib import admin
from .forms import PostAdminForm
from .models import Post, Header , Footer
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField : {'widget':TinyMCE()}
    }

admin.site.register(Post, PostAdmin)
admin.site.register(Header)
admin.site.register(Footer)