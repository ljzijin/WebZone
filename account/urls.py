from django.conf.urls import patterns, include, url

from django.contrib import admin
import views

urlpatterns=patterns('',
	url(r'^login/',views.login),
<<<<<<< HEAD
	url(r'^logout',views.logout),
=======
>>>>>>> 8d0c4837016056e72d3829b4e2a11fa4fdaee17d
	)