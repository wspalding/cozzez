from django.urls import path
from news_collector import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
               path('', views.home, name='home'),
#               path('<int:month>/<int:day>/<int:year>/fill/', views.fill_database, name="temp_data_feeder"),
               path('<int:month>/<int:day>/<int:year>/test/', views.test, name="test_stuff"),
#               path('login/', views.login, name='login'),
               path('<int:month>/', views.date, name='date'),
               path('<int:month>/<int:day>/', views.date, name='date'),
               path('<int:month>/<int:day>/<int:year>/', views.date, name='date'),
               
               # path('<int:month>/<int:day>/<int:year>/<string:title>', views.story, name='story'),
               ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
