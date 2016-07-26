from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/',views.index),
	url(r'^article_list/',views.article_list),
	url(r'^add_article/',views.add_article),
	url(r'^deal_add_article/',views.deal_add_article),
	url(r'^del_article/',views.del_article),
	url(r'^deal_mod_article/',views.mod_article),
	url(r'^deal_mod_article/',views.deal_mod_article),
	url(r'^del_comment/',views.del_comment),
	]
