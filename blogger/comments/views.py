from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from articles.models import Article
from comments.models import Comment

import datetime

@login_required
def add_comment(request):
    username = request.session["username"]
    content = request.POST["content"]
    article_id = request.POST["article_id"]
    user = User.objects.get(username = username)
    article = Article.objects.get(id = article_id)
    print article_id
    comment = Comment(
                        content = content,
                        article = article,
                        user = user
                    )
    comment.save()
    return HttpResponseRedirect("/articles/show_article/?id=%s" % article_id)

# Create your views here.
