from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse
import logging
from .models import Post

# static demo data
# posts = [
#     {"id": 1, "title": "Post 1",  "content": "Content of Post 1"},
#     {"id": 2, "title": "Post 2",  "content": "Content of Post 2"},
#     {"id": 3, "title": "Post 3",  "content": "Content of Post 3"},
#     {"id": 4, "title": "Post 4",  "content": "Content of Post 4"},
#     {"id": 5, "title": "Post 5",  "content": "Content of Post 5"},
#     {"id": 6, "title": "Post 6",  "content": "Content of Post 6"}
# ]


posts = Post.objects.all()
# logger = logging.getLogger("TESTING")
# logger.debug(f"post variable is {posts}")

# Create your views here.
def index(request):
    blog_title = "Latest Posts"
    return render(request, "index.html",  {'blog_title': blog_title, 'posts': posts})

def detials(request, slug):
    # getting static data
    # post = next((item for item in posts if item["id"] == int(post_id)), None)

    try:
        # getting data from model by id
        post = Post.objects.get(slug=slug)
        related_posts = Post.objects.filter(category=post.category).exclude(pk=post.id)

    except Post.DoesNotExist:
        raise Http404("Post does not exist!")

    # logger = logging.getLogger("TESTING")
    # logger.debug(f"post variable is {post}")
    return render(request, "detail.html", {"post": post, "related_posts": related_posts})

def old_url_redirect(request):
    return redirect(reverse("blog:new_page_url"))

def new_url(request):
    return HttpResponse("This is new URL")