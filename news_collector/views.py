from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from news_collector.models import Test


def index(request):
    tests = Test.objects.all()
    test2 = Test.objects.get_or_create(name="test2")
    all_tests = [x.name for x in tests]
    return JsonResponse({"test models": all_tests})
