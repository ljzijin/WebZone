#-*-coding:utf-8-*-
from django.contrib import admin
from django.conf.urls import *
import views

urlpatterns=patterns('',
	url(r'^index/',views.index),
	url(r'^create_blog/$',views.create_blog),
<<<<<<< HEAD
	url(r'^comment_blog/',views.comment_blog),
=======
>>>>>>> 80918682690ef858f30cb54d80448d158eb453f6
	)