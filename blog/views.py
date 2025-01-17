from django.shortcuts import render, get_object_or_404
from .models import Post


def rende_post(request):
    post_blog = Post.objects.all()
    return render(request, "post.html", {"post": post_blog})


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "post_detail.html", {"post": post})
