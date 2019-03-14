from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf.urls import url

namespace = 'todo'

urlpatterns = [
	url(r'^$', login_user, name="login"),
	url(r'^register/$', register, name="register"),
	url(r'^logout/$', logout_user, name="logout"),
	url(r'todolist/$', todolist, name="todolist"),


	# rest api for save, delete and update todos
    url(r'^api-auth/$', TodoAppView.as_view(), name="TodoAppView"),
]