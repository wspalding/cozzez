from __future__ import absolute_import, unicode_literals
import random
from celery.decorators import task
from news_collector.models import Test
from news_collector.utils.misc_func import fill_database_for_date

@task(name="sum_two_numbers")
def add(x, y):
    return x + y

@task(name="multiply_two_numbers")
def mul(x, y):
    total = x * (y * random.randint(3, 100))
    return total

@task(name="sum_list_numbers")
def xsum(numbers):
    return sum(numbers)

@task(name="create_test_model")
def make_test_model(number):
    name = "test{}".format(number)
    new_model = Test.objects.get_or_create(name=name)
    new_model[0].save()

@task(name="collect_news_stories")
def collect_news_stories():
    info = fill_database_for_date()
    return info

