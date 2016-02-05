#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from apps.wedding import views  

urlpatterns = [

		url(r'^$', views.index),
		url(r'^add_comments/', views.add_comments),
			]