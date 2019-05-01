from django.contrib import admin
from news_collector.models import *

# Register your models here.
admin.site.register(Topic)
admin.site.register(Article)
#admin.site.register(Comment)
#admin.site.register(Personality)
#admin.site.register(Author)
admin.site.register(Label)

admin.site.register(Test)
