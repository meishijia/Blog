from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name = 'index'),
    url(r'^index/',views.index),
	url(r'^add_article/',views.add_article),
    url(r'^deal_article/',views.deal_article),
]
