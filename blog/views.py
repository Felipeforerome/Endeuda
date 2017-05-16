from blog.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

def listing(request):
    post_list = Post.objects.all().order_by("-date")
    paginator = Paginator(post_list, 12)
    freqs = Post.objects.filter(promoted='True').order_by("-date")[:3]

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/list.html', {'posts': posts, 'freqs': freqs})

def filter(request, name):
    post_list = Post.objects.all().filter(tag__icontains=name)
    paginator = Paginator(post_list, 10) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/list.html', {'posts': posts})