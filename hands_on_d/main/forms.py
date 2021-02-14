from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget

# from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE

from .models import Post

class TinyMCEWidget(TinyMCE): 
    def use_required_attribute(self, *args): 
        return False

class PostAdminForm(forms.ModelForm): 
    content = forms.CharField( 
        widget=TinyMCEWidget( 
            attrs={'required': False, 'cols': 30, 'rows': 10} 
        ) 
    ) 
    class Meta: 
        model = Post 
        fields = '__all__'

# class PostAdminForm(forms.ModelForm):
#     content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30})) #widget=TinyMCE(attrs={'cols': 80, 'rows': 30})
#     class Meta:
#         model = Post
#         fields = '__all__'
