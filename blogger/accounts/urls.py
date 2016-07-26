from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name = 'index'),
    url(r'^login',views.index),
    url(r'^index/',views.index),
	url(r'^logout/',views.logout_do),
    url(r'^deal_form/',views.login_do),
    url(r'^register/',views.register),
    url(r'^deal_register/',views.deal_register),
]
