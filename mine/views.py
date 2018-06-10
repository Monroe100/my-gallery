# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as dt
# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')



def index(request):
    title = 'Welcome'
    test = 'Testing'
    date = dt.date.today
    photos = Image.get_all()
    return render(request, 'index.html',
                  {"title": title,
                   "test": test,
                   "date": date,
                   "photos": photos})


def image(request, image_id):
    image = Image.get_image(image_id)
    return render(request, 'image.html', {"image": image})



def search_results(request):

    

    if 'image' in request.GET and request.GET["image"]:
        query = request.GET.get("image")
        results = Image.searched(query)
        message = f"{query}"

        return render(request, 'search.html',
                      {"message": message, "results": results})
    else:
        message = "What images do you want to search for?"
        return render(request, 'search.html',
                      {"message": message})
    


def all_images(request):
    images = Post.all_images()
    return render(request, 'all_images.html', {"images":images})


def image_details(request, post_id):
    photo = Post.objects.get(id=post_id)
    return render(request,"imagedetails.html",{'photo':photo})

def post(request,post_id):
    try:
        post = Post.objects.get(id = post_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"post.html", {"post":post})
