from django.shortcuts import render
from django.http import HttpResponse

from articles.models import Article
from comments.models import Comment
from django.contrib.auth.models import User

import datetime

def index(request):
    return render(request,"/manager/index.html")

def article_list(request):
    return render(request,"/manager/article_list.html")

def add_article(request):
    title = request.POST["title"]
    content = request.POST["content"]
    time_stamp = datetime.datetime.now().strftime('%Y-%m-%d')
    article = Article(title = title,
                      content = content,
                      time_stamp = time_stamp,
            )
    article.save()
    return HttpResponseRedirect("/manager/index/")

def del_article(request):
    article_id = request.POST["article_id"]
    article = Article.objects.filter(id = article_id)
    article.delete()
    return HttpResponseRedirect("/maneger/deal_mod_article/")

def mod_article(request):
    article_id = request.POST["article_id"]
    article = Article.objects.filter(id = article_id)
    return rende(request,"manager/mod_article.html",{"articel":article})

def deal_mod_article(request):
    article_id = request.POST["article_id"]
    article = Article.objects.get(id=article_id)
    title = request.POST["title"]
    content = request.POST["content"]
    time_stamp = datetime.datetime.now().strfwtime('%Y-%m-%d')
    articel.title = title
    article.content = content
    article.time_stamp = time_stamp
    article.save()
    return HttpResponseRedirect("/manager/deal_mod_article")

def del_comment(request):
    comment_id = request.POST["comment_id"]
    comment = Comment.objects.get(id = comment_id)
    comment.delete()
    return HttpResponseRedirect("/manager/deal_mod_article/")

# Create your views here.
