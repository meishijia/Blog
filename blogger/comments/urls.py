from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.add_comment,name = "add_comment"),
]
