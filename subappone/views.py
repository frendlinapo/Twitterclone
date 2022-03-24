from django import forms
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm


def index(request):
    # If the method is POST
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        # If the form is valid
        if form.is_valid():
            # Yes, Save
            form.save()

            # Redirect to Home
            return HttpResponseRedirect('/')

        else:
            # No, Show Error
            return HttpResponseRedirect(form.errors.as_json())

    # Get all posts, limit = 20
    posts = Post.objects.all().order_by('-created_at')[:20]
    form = PostForm()
    return render(request, 'posts.html', {'posts': posts})

    # Show
    return render(request, 'posts.html',
                  {'posts': posts})


def likes(request, post_id):
    likedtweet = Post.objects.get(id = post_id)
    likedtweet.like += 1
    likedtweet.save()
    return HttpResponseRedirect("/")


def delete(request, post_id):
    # Find post
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')


def edit(request, post_id):
    if request.method == "GET":
        posts = Post.objects.get(id=post_id)
        return render(request, "edit.html", {"posts": posts})
    if request.method == "POST":
        editposts = Post.objects.get(id=post_id)
        form = PostForm(request.POST, request.FILES, instance=editposts)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
        else:
            return HttpResponse("not valid")
