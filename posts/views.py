from django.shortcuts import render
from .models import Post
from django.views.generic import ListView



#def post_list(request):
#    posts = Post.objects.all()
#    context = {
#        "posts":posts,
#    }
#    return render(request, "posts/list.html", context)


class PostlistView(ListView):
    model = Post
    template_name = "posts/list.html"
    context_object_name = "posts"
