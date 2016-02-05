#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from apps.blog import views


urlpatterns = [
		url(r'^$', views.BlogListView.as_view(), name="home"),
		url(r'^(?P<pk>\d+)/(?P<blog_link>[\w,-]*)$', views.BlogDetailView.as_view(), name='blog_detail'),
               ]
