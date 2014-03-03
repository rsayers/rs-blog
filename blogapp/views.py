from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from blogapp.models import Post
import datetime      
import PyRSS2Gen

def index(request):
    # get the blog posts that are published
    page = request.GET.get('page')
    posts = Post.objects.filter(published=True)
    paginator = Paginator(posts, 10)

    
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)


    # now return the rendered template
    return render(request, 'blog/index.html', {'posts': posts})


def date_index(request,month,year):
    # get the blog posts that are published
    page = request.GET.get('page')
    posts = Post.objects.filter(published=True, created__year=year, created__month=month)
    paginator = Paginator(posts, 10)

    date = datetime.date(int(year),int(month),1)

    extra = "Viewing posts for %s" % date.strftime("%B %Y")
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)


    # now return the rendered template
    return render(request, 'blog/index.html', {'posts': posts,'extra':extra})

def category_index(request,category):
    # get the blog posts that are published
    page = request.GET.get('page')
    posts = Post.objects.filter(published=True, category__contains=category)
    paginator = Paginator(posts, 10)

    
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)


    # now return the rendered template
    return render(request, 'blog/index.html', {'posts': posts,'extra':"Viewing Category: %s" % category.title()})

    
def post(request, slug,  month, year):
    # get the Post object
    post = get_object_or_404(Post, slug=slug)
    # now return the rendered template
    return render(request, 'blog/post.html', {'post': post})

