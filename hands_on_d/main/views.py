from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import PostAdminForm


# Create your views here.
def home(request):
    if request.method == 'POST':
        myform = PostAdminForm(request.POST)
        if myform.is_valid():
            content = myform.cleaned_data.get('content')
            print(content)
            return redirect('blog-home')
    myform = PostAdminForm()
    return render(request, 'main/index.html',{'myform' : myform})
