from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^add_comments/',views.add_comment),
]
