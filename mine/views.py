# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as dt
from .models import Image,Category,Location
# Create your views here.




def welcome(request):
    title = 'Welcome'
    test = 'Testing'
    date = dt.date.today
    photos = Image.get_all()
    return render(request, 'welcome.html',
                  {"title": title,
                   "test": test,
                   "date": date,
                   "photos": photos})


def image(request, image_id):
    image = Image.get_image(image_id)
    return render(request, 'post.html', {"image": image})



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
    


def image_details(request, post_id):
    photo = Image.objects.get(id=post_id)
    return render(request,"imagedetails.html",{'photo':photo})

def post(request,post_id):
    try:
        post = Image.objects.get(id = post_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"post.html", {"post":post})
