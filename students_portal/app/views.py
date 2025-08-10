from django.shortcuts import render

# Create your views here.
def posts_list(request):
    return render(request,'app/posts_list.html')