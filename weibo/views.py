#-*-coding:utf-8 -*-
from django.shortcuts import render, render_to_response
from django.template import Context,RequestContext
from django.conf import settings
from django.contrib import auth
from models import *
import json
HOME_SECOND_NAV=[{
	'navs':[{
		'name':'person_page',
		'title':u'个人主页',
		'url':'',		
		},{
		'name':'friend_list',
		'title':u'好友列表',
		'url':'',
		}]
}]
# Create your views here.
def index(request):
	c= RequestContext(request,{
		'second_navs':HOME_SECOND_NAV,

		})
	return render_to_response('weibo/index.html',c)