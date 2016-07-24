from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from articles.models import Article
from comments.models import Comment

import traceback
import datetime

@login_required
def index(request):
    try:    
        username = request.session["username"]
    except:
        username = ""
    data = {}
    user = User.objects.filter(username = username)
    articles = Article.objects.filter(author = user)
    for article in articles:
        comments = Comment.objects.filter(article = article)
        data[article] = comments
    return render(request,'articles/article_list.html',{'data':data,'user':user,'articles':articles})

def add_article(request):
    return render(request,'articles/add_article.html')

@login_required
def deal_article(request):
    try:
        username = request.session["username"]
        title = request.POST["title"]
        content = request.POST["content"]
        user = User.objects.get(username = username)
        article = Article(title = title,
                          content = content,
                          author = user,
                          time_stamp = datetime.datetime.now().strftime('%Y-%m-%d'),
                         )
        article.save()
    except:
        print traceback.print_exc()
    return HttpResponseRedirect("/articles/index/")

def show_article(request):
    article_id = request.GET["id"]
    article = Article.objects.get(id = article_id)
    comments = Comment.objects.filter(article = article)
    return render(request,"articles/show_article.html",{"article":article,"comments":comments})

# Create your views here.

