from django.shortcuts import render, render_to_response
from django.template import Context,RequestContext
from django.conf import settings
from django.contrib import auth
from models import *
import json

# Create your views here.
def index(request):
	c= RequestContext(request,{

		})
	return render_to_response('weibo/index.html',c)