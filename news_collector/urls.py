from django.urls import path
from news_collector import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
               # temporary homepage
               path('', views.reader_page, name='home'),
               path('story/<data>', views.story_page, name='story'),
               path('story/', views.story_page, name='story'),
               path('requests/news_links', views.get_news_links, name='request_news_links'),
               path('requests/news_links/<key_word>', views.get_news_links, name='request_news_links')
#               path('<int:month>/<int:day>/<int:year>/fill/', views.fill_database, name="temp_data_feeder"),
               #path('<int:month>/<int:day>/<int:year>/test/', views.test, name="test_stuff"),
#               path('login/', views.login, name='login'),
               #path('<int:month>/', views.date, name='date'),
               #path('<int:month>/<int:day>/', views.date, name='date'),
               #path('<int:month>/<int:day>/<int:year>/', views.date, name='date'),
               
               # path('<int:month>/<int:day>/<int:year>/<string:title>', views.story, name='story'),
               
               ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
