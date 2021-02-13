from django.contrib import admin
from .forms import PostAdminForm
from .models import Post, Header , Footer
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm

admin.site.register(Post, PostAdmin)
admin.site.register(Header)
admin.site.register(Footer)