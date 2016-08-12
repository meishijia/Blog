from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import permission_required

from articles.models import Article
from comments.models import Comment
from django.contrib.auth.models import User

import datetime
import re
#from django.contrib.postgres.search import search

@permission_required('django.contrib.auth.can_manage')
def index(request):
    return render(request,"manager/index.html")

@permission_required('django.contrib.auth.can_manage')
def article_list(request):
    articles = Article.objects.all()
    return render(request,"manager/article_list.html",{"articles":articles})

@permission_required('django.contrib.auth.can_manage')
def add_article(request): 
    return render(request,"manager/add_article.html",{})

@permission_required('django.contrib.auth.can_manage')
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

@permission_required('django.contrib.auth.can_manage')
def del_article(request):
    article_id = request.GET["id"]
    article = Article.objects.filter(id = article_id)
    article.delete()
    return HttpResponseRedirect("/manager/article_list/")

@permission_required('django.contrib.auth.can_manage')
def manage_article(request):
    article_id = request.GET["id"]
    article = Article.objects.get(id = article_id)
    comments = Comment.objects.filter(article = article)
    return render(request,"manager/manage_article.html",{"article":article,"comments":comments})

@permission_required('django.contrib.auth.can_manage')
def mod_article(request):
	article_id = request.GET["id"]
	article = Article.objects.get(id = article_id)
	return render(request,"manager/mod_article.html",{"article":article})

@permission_required('django.contrib.auth.can_manage')
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

@permission_required('django.contrib.auth.can_manage')
def del_comment(request):
    comment_id = request.POST["comment_id"]
    comment = Comment.objects.get(id = comment_id)
    id = str(comment.article.id)
    comment.delete()
    return HttpResponseRedirect("/manager/manage_article/?id="+id)

@permission_required('django.contrib.auth.can_manage')
def manage_accounts(request):
    users = User.objects.all()
    return render(request,"manager/manage_accounts.html",{"users":users})

@permission_required('django.contrib.auth.can_manage')
def deal_manage_accounts(request):
    user_id = request.POST["user_id"]
    user = User.objects.get(id = user_id)
    user.delete()
    return HttpResponseRedirect("/manager/manage_accounts/")
    
@permission_required('django.contrib.auth.can_manage')
def search(request):
    articles=[]
    keywords = request.POST["keywords"]
    print keywords


    
    if articles:
        return render(request,"manager/article_list.html",{"articles":articles})
    else:
        message = 'NO RESULTS.TRY AGAIN'
        return HttpResponse(message)

# Create your views here.
