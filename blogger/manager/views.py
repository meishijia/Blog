from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

from articles.models import Article
from comments.models import Comment
from django.contrib.auth.models import User

import datetime

def index(request):
    return render(request,"manager/index.html")

def article_list(request):
    articles = Article.objects.all()
    return render(request,"manager/article_list.html",{"articles":articles})

def add_article(request):
    return render(request,"manager/add_article.html")

def deal_add_article(request):
    title = request.POST["title"]
    content = request.POST["content"]
    time_stamp = datetime.datetime.now().strftime('%Y-%m-%d')
    article = Article(title = title,
                      content = content,
                      time_stamp = time_stamp,
            )
    article.save()
    return HttpResponseRedirect("/manager/article_list/")

def del_article(request):
    article_id = request.GET["id"]
    article = Article.objects.filter(id = article_id)
    article.delete()
    return HttpResponseRedirect("/manager/article_list/")

def manage_article(request):
    article_id = request.GET["id"]
    article = Article.objects.get(id = article_id)
    comments = Comment.objects.filter(article = article)
    return render(request,"manager/manage_article.html",{"article":article,"comments":comments})

def mod_article(request):
	article_id = request.GET["id"]
	article = Article.objects.get(id = article_id)
	return render(request,"manager/mod_article.html",{"article":article})

def deal_mod_article(request):
    article_id = request.POST["article_id"]
    article = Article.objects.get(id = article_id)
    title = request.POST["title"]
    content = request.POST["content"]
    time_stamp = datetime.datetime.now().strftime("%Y-%m-%d")
    article.title = title
    article.content = content
    article.time_stamp = time_stamp
    article.save()
    return HttpResponseRedirect("/manager/article_list/")

def del_comment(request):
    comment_id = request.POST["comment_id"]
    comment = Comment.objects.get(id = comment_id)
    id = str(comment.article.id)
    comment.delete()
    return HttpResponseRedirect("/manager/manage_article/?id="+id)

# Create your views here.
