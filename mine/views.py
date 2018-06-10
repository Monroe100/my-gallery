# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as dt
# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')


# def image_of_day(request):
#     date = dt.date.today()
#     day = convert_dates(date)
#     # html = f'''
#     #     <html>
#     #         <body>
#     #             <h1> Images for {day} {date.day}-{date.month}-{date.year}</h1>
#     #         </body>
#     #     </html>
#     #       ''''
#     return HttpResponse(html)


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

        return render(request, 'results.html',
                      {"message": message, "results": results})
    else:
        message = "What images do you want to search for?"
        return render(request, 'results.html',
                      {"message": message})


def image_today(request):
    date = dt.date.today()
    return render(request, 'all-images/today-images.html', {"date": date,})

def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day

def past_days_image(request,past_date):
    try:

        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False
        if date == dt.date.today():
            return redirect (image_today)

    return render(request, 'all-images/past-images.html', {"date": date})

    day = convert_dates(date)

    # html = f'''
    #     <html>
    #         <body>
    #             <h1>Images For {day} {date.day}-{date.month}-{date.year}</h1>
    #         </body>
    #     </html>
    #         '''
    return HttpResponse(html)