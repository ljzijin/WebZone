from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf.urls import *
import views

urlpatterns=patterns('',
	url(r'^weibo/index/$',views.index),
	)