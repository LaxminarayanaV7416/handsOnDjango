from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('pdfDownload', views.pdf_download, name = 'pdf_download'),
]