#-*-coding:utf-8 -*-
from django.shortcuts import render, render_to_response
from django.template import Context,RequestContext
from django.conf import settings
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest, Http404
from models import *
from core.jsonresponse import create_response
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
	blogs=Blog.objects.all().order_by('-created_at')
	blog_comments=BlogComment.objects.all().order_by('-created_at')
	blog_list=[]
	for blog_c in blog_comments:
		blog_id=blog_c.blog_id
		blog_dict={
			'comment_content':blog_c.comment_content,
			'comment_created_at':blog_c.created_at,
		}

	c= RequestContext(request,{
		'second_navs':HOME_SECOND_NAV,
		'blogs':blogs,
		'blog_comments':blog_comments,

		})
	return render_to_response('weibo/index.html',c)
#===============================================================
#发布微博
#===============================================================
def create_blog(request):
	blog_user = request.user.id
	blog_content=request.POST.get('bolg_content','')
	try:
		if blog_content:
			Blog.objects.create(
				blog_user=blog_user,
				blog_content=blog_content,
				)
		response=create_response(200)
	except:
		response=create_response(500)
		response.errMsg='创建失败'
	return response.get_response()			
#===============================================================
#评论微博
#===============================================================	
def comment_blog(request):
	blog_comment=request.POST.get('comment_content','')
	blog_id=request.POST.get('blog_id','')
	comment_user_id=request.user.id
	if blog_id:
		BlogComment.objects.create(
			comment_user_id=comment_user_id,
			blog_id=blog_id,
			comment_content=blog_comment,
			)
		response=create_response(200)
	else:
		response=create_response(500)
		response.errMsg='评论失败'
	return response.get_response()		

