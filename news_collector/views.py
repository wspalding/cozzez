from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.db.models import Count
from news_collector.utils.crawlers import *
from news_collector.utils.misc_func import *
# Create your views here.
from django.utils import timezone
from news_collector.models import *
from news_collector.utils.text_reader import *
import datetime

def home(request):
    now = timezone.now()
    # today = [now.month, now.day, now.year]
    url = "{month}/{day}/{year}/".format(month=now.month,
                                         day=now.day,
                                         year=now.year,)
    return redirect(url)


def date(request, **kwargs):
    month = kwargs.get("month")
    day = kwargs.get("day", None)
    year = kwargs.get("year", None)
    valid_date = False
    try:
        #valid date
        today = datetime.datetime(year, month, day)
        tomarrow = today + datetime.timedelta(days=1)
        yesterday = today + datetime.timedelta(days=-1)
        
        today_str, today_url = get_date(today)
        tomarrow_str, tomarrow_url = get_date(tomarrow)
        yesterday_str, yesterday_url = get_date(yesterday)
        valid_date = True
    except:
        #invalid date
        today_str = "{}/{}/{}".format(month, day, year)
        tomarrow_str = "{}/{}/{}".format(month, day+1, year)
        yesterday_str = "{}/{}/{}".format(month, day-1, year)
        tomarrow_url = "/" + tomarrow_str + "/"
        yesterday_url = "/" + yesterday_str + "/"
    
    topics = []
    articles = []
    if valid_date:
        #load real story
        # get all articles for the day
        #articles = Article.objects.filter(date=today)
        # get already made topics for the day
        topics = Topic.objects.annotate(num_art=Count('articles')).order_by('-num_art').filter(date=today)
        # create new topics with unused articles
        image_file = None
        if topics.count() == 0:
            # no topics in past:
            if today < datetime.datetime.now():
                image_file = "arceologisst image.jpg"
            # no topics in present:
            if today == datetime.datetime.now():
                image_file = "waiting image.jpg"
            # no topics in future:
            if today > datetime.datetime.now():
                image_file = "psycic image.jpg"
    else:
        #load fake story
        image_file = None
        pass
    
    context = {"date": today_str,
        "previous_date_string": yesterday_str,
            "previous_date": yesterday_url,
            "next_date_string": tomarrow_str,
            "next_date": tomarrow_url,
            "news_stories": topics,
            #"articles": articles,
            #"image": image_file,
        }
    return render(request,'home.html', context)


def login(request, **kwargs):
    return render(request, 'login.html')


def test(request, **kwargs):
    articles = Article.objects.all()
    titles = [x.title for x in articles]
    return JsonResponse({"titles": titles})



def fill_database(request, **kwargs):
    month = kwargs.get("month")
    day = kwargs.get("day", None)
    year = kwargs.get("year", None)
    
    dic = fill_database_for_date(month=month,day=day,year=year)
    
    
    return JsonResponse(dic)





