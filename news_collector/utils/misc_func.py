from itertools import zip_longest
from news_collector.models import *
from news_collector.utils.crawlers import news_collector
import datetime


def grouper(n, iterable, padvalue=None):
    "grouper(3, 'abcdefg', 'x') --> ('a','b','c'), ('d','e','f'), ('g','x','x')"
    return list(zip_longest(*[iter(iterable)]*n, fillvalue=padvalue))



def get_date(date_time):
    month = date_time.month
    day = date_time.day
    year = date_time.year
    months=["January","February","March","April","May","June","July",
            "August", "September", "October", "November","December"]
    month_str = months[month-1]
    date_string = "{} {}, {}".format(month_str, day, year)
    date_url = "/{}/{}/{}/".format(month, day, year)
    return date_string, date_url



class NewsStory: # defines a single stroy from a link
    def __init__(self, **kwargs):
        # id = set automatically by python
        self.title = kwargs.get("title", "default title")
        self.text = kwargs.get("text", "blah blah blah")
        self.score = kwargs.get("score", 0)
        self.url = kwargs.get("url", "fake_news.com/click_bait_title")
        self.key_topics = kwargs.get("topics", [])
        self.id_num = id(self)
    
    
class SiteStory:
    def __init__(self, **kwargs):
        self.news_story_list = kwargs.get("stories", [])
        self.comments = kwargs.get("comments", [])
       
    
    
    

def fill_database_for_date( **kwargs):
    now = datetime.datetime.now()
    month = kwargs.get("month", now.month) #make default to today
    day = kwargs.get("day", now.day)
    year = kwargs.get("year", now.year)
    list_of_topics = {}
    
    crawler = news_collector()
    print("collecting data from kqed")
    list_of_topics["kqed"] = crawler.extract_kqed_info()
    print("adding data to database")
    fill_database_from_info(list_of_topics["kqed"],
                            month=month,
                            day=day,
                            year=year)

    print("collecting data from fox")
    list_of_topics["fox"] = crawler.extract_fox_info()
    print("adding data to database")
    fill_database_from_info(list_of_topics["fox"],
                            month=month,
                            day=day,
                            year=year)

    print("collecting data from msnbc")
    list_of_topics["msnbc"] = crawler.extract_msnbc_info()
    print("adding data to database")
    fill_database_from_info(list_of_topics["msnbc"],
                            month=month,
                            day=day,
                            year=year)

    print("collecting data from nyt")
    list_of_topics["NYT"] = crawler.extract_NYT_info()
    print("adding data to database")
    fill_database_from_info(list_of_topics["NYT"], 
                            month=month, 
                            day=day, 
                            year=year)
    
    return list_of_topics

def fill_database_from_info(info, **kwargs):
    month = kwargs.get("month")
    day = kwargs.get("day", None)
    year = kwargs.get("year", None)
    
    new_articles = []
    for key, item in info.items():
        if item["status_code"] != 200:
            info[key]["created"] = False
            continue
#        author = Author.objects.get_or_create(
#            name=item["author"],
#            defaults={
#                'affiliation':item["source"]
#            },
#        )
        print("getting/creating new article: \n {}: {}, {}, {} \n".format(item["title"], item["source"], item["date"], key))
        title_string = item["title"]
        if len(title_string) > 100:
            title_string = title_string[:97] + "..."
        article = Article.objects.get_or_create(
            url=key,
            defaults={
                'affiliation':item["source"],
                'date':item["date"],
                'title':title_string,
#                'media_url':item["media"],
#                'author':author[0],
                'source_url':item["source_url"],
            }
        )
        
        info[key]["created"] = article[1]
        if article[1] is False:
            new_articles.append(article[0])
            print("article already found")
            continue
        print("making labels for article {}".format(item["title"]))
        for key2, item2 in item["labels"].items():
            MIN_LABEL_SCORE = 5
            if item2["total"] > MIN_LABEL_SCORE:
                label_word = key2[:47] + '...'
                new_label = Label(
                    word=key2,
                    score=item2["total"],
                    article=article[0],
                )
                new_label.save()
        print("saving article")
        article[0].save()
        new_articles.append(article[0])
#        author[0].save()

        
        # TODO: make this better
    # create topics
    print("making topics")
    topic_list = {}
    today = datetime.date(year, month, day)
    old_topics = Topic.objects.filter(date=today)
    matched_articles = set()
    for article in new_articles:
        #if article.topic.count() == 0:
        labels = list(Label.objects.filter(article=article))
        topic_list[article.url] = []
        for label in labels:
            matched_topics_1 = old_topics.filter(label1__word=label.word)
            for top in matched_topics_1:
                if top not in article.topic.all():
                    article.topic.add(top)
                    top.articles.add(article)
                    top.save()
                    topic_list[article.url].append({str(top):"added"})
                    
            matched_topics_2 = old_topics.filter(label2__word=label.word)
                    
            for top in matched_topics_2:
                if top not in article.topic.all():
                    article.topic.add(top)
                    top.articles.add(article)
                    top.save()
                    topic_list[article.url].append({str(top):"added"})
                    
            matched_topics_3 = old_topics.filter(label3__word=label.word)
            for top in matched_topics_3:
                if top not in article.topic.all():
                    article.topic.add(top)
                    top.articles.add(article)
                    top.save()
                    topic_list[article.url].append({str(top):"added"})
                    
        if article.topic.count() == 0:
            if 0 == len(labels):
                null_topic = Topic.objects.get_or_create(date=today, label1=None, label2=None, label3=None)
                
            #topic_list[article.url].append({str(null_topic):"added"})
                null_topic[0].articles.add(article)
                article.topic.add(null_topic[0])
                null_topic[0].save()
                article.save()
                if null_topic[1]:
                    topic_list[article.url].append({str(null_topic):"created"})
                else:
                    topic_list[article.url].append({str(null_topic):"added"})
            else:                                     
                new_topic = Topic(
                    date=today,
                    label1=labels[0] if 0 < len(labels) else None,
                    label2=labels[1] if 1 < len(labels) else None,
                    label3=labels[2] if 2 < len(labels) else None,
                )
                new_topic.save()
                new_topic.articles.add(article)
                article.topic.add(new_topic)
                new_topic.save()
                topic_list[article.url].append({str(new_topic):"create"})
        article.save()
    return {"info": info,
            "topics": topic_list,}




    
    
    
    
    
    
