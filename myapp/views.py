from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


# Class Based View -> CBV
# post_list = ListView.as_view(model=Post)

# Function Based View -> FBV
def post_list(request):
    qs = Post.objects.all()
    return render(request, 'myapp/post_list.html', {
        'post_list': qs,
    })
