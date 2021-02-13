from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import PostAdminForm
from .pdf_utils import render_to_pdf 
from .models import get_latest_header, get_latest_footer, get_latest_post, Post

# Create your views here.
def home(request):
    header = get_latest_header()
    footer= get_latest_footer()
    if request.method == 'POST':
        myform = PostAdminForm(request.POST)
        if myform.is_valid():
            content = myform.cleaned_data.get('content')
            data = Post(content=content)
            data.save()
            print(content)
            if request.POST.get('download',None) is not None:
                pdf = render_to_pdf('main/pdf_template.html',{'header':header, 'footer':footer, 'content': content})
                return HttpResponse(pdf, content_type='application/pdf')
            return redirect('blog-home')
    if request.method == 'GET':
        myform = PostAdminForm()
    return render(request, 'main/index.html',{'myform' : myform , 'header':header, 'footer':footer})

def pdf_download(request):
    header = get_latest_header()
    footer= get_latest_footer()
    content = get_latest_post()
    pdf = render_to_pdf('main/pdf_template.html',{'header':header, 'footer':footer, 'content': content})
    return HttpResponse(pdf, content_type='application/pdf')