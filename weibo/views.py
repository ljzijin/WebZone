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
	blog_list=[]
	comment_list=[]
	blog_comments=BlogComment.objects.all().order_by('-created_at')
	for c in blog_comments:
		blog_id=c.blog_id
		comment_dict={
			'blog_id':blog_id,
			'comment_content':c.comment_content,
			'comment_created_at':c.created_at,
		}
		if comment_dict not in comment_list:
			comment_list.append(comment_dict)			
	comment_blog_ids=[c.blog_id for c in blog_comments]
	for blog in blogs:
		b_id=blog.id
		if b_id in comment_blog_ids:
			for comment_dic in comment_list:
				print comment_dic['blog_id'],6666666666666
			blog_comments=BlogComment.objects.filter(blog_id=b_id)
			for comm in blog_comments:				
				blog_dict={
					'blog_id':b_id,
					'blog_content':blog.blog_content,
					'blog_created_at':blog.created_at.strftime('%Y-%m-%d %H:%M:%S'),
					'comment_content':comm.comment_content,
					'comment_created_at':comm.created_at.strftime('%Y-%m-%d %H:%M:%S'),
				}
		else:
			blog_dict={
				'blog_id':b_id,
				'blog_content':blog.blog_content,
				'blog_created_at':blog.created_at.strftime('%Y-%m-%d %H:%M:%S'),
			}					
		if blog_dict not in blog_list:
			blog_list.append(blog_dict)
	blog_list=sorted(blog_list,key=lambda blog_dict:blog_dict['blog_created_at'],reverse=True)
	c= RequestContext(request,{
		'second_navs':HOME_SECOND_NAV,
		'blogs':blogs,
		'blog_comments':blog_comments,
		'blog_list':blog_list,

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

