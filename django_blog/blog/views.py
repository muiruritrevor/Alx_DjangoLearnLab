from django.shortcuts import render

def home(request):
    return render(request, 'blog/home.html')

# def posts(request):
#     return render(request, 'blog/posts.html')
# # Create your views here.
