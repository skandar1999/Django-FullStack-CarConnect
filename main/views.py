from django.http import HttpResponse
from django.shortcuts import render

def main_view(request):
    return render(request, "views/main.html")
 

def contact_view(request):
    return render(request, "views/contact.html")

def blog_view(request):
    return render(request, "views/blog.html")