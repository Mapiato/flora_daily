from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.flora_daily, name='flora_daily')
]
