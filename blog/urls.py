# -*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from . import views, feed

urlpatterns = patterns(
    '',
    url(r'^$', views.BlogIndex.as_view(), name = "index"),
    url(r'^feed/$', feed.LatestPosts(), name = "feed"),
    url(r'^entry/(?P<slug>\S+)$', views.BlogDetail.as_view(), name="entry_detail"),    
   # url(r'^contato/$', 'blog.views.contato', name = "contact"),
    url(r'^sobre/$', 'blog.views.sobre', name = "about"),
    url(r'^contato/thankyou/$', 'blog.views.thankyou'),
    url(r'^contato/$', 'blog.views.contactview', name = "contato"),
)
