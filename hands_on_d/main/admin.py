from django.contrib import admin
from .forms import PostAdminForm
from .models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm

admin.site.register(Post, PostAdmin)