from django.shortcuts import render, HttpResponseRedirect, reverse

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login, logout
from .serializers import *


class TodoAppView(APIView):

	permission_classes = [AllowAny]
	# print("PUT")
	def get(self,request,format=None):

		objects = TodoApp.objects.all()
		serialized_object = TodoAppSerializer(objects,many=True)
		return Response(serialized_object.data)


	def post(self,request, format=None):
		typ = request.data.get("typ")
		
		if int(typ) == 1:
			heading = request.data.get("heading")
			description = request.data.get("description")
			schedule = request.data.get("schedule")
			
			instance = TodoApp.objects.create(owner=request.user, heading=heading,description=description,schedule=schedule)
			instance.save()
			
			serialized_object = TodoAppSerializer(instance,many=False)
			return Response(serialized_object.data)

		elif int(typ) == 2:
			id = request.data.get("id")
			instance = TodoApp.objects.get(id=id)
			instance.delete()

			return Response("Success")
		# else:
		# 	return Response("Error")
		elif int(typ) == 3:
			heading = request.data.get("heading")
			description = request.data.get("description")
			schedule = request.data.get("schedule")
			id = request.data.get("id")
			instance = TodoApp.objects.get(id=id)
			instance.heading = heading
			instance.description = description
			instance.schedule = schedule
			instance.save()

			serialized_object = TodoAppSerializer(instance,many=False)
			return Response(serialized_object.data)

	def put(self,request, format=None):
		print(request.user, "PUT request")
		id = request.data.get("id")
		instance = TodoApp.objects.get(id=id)
		instance.delete()

		return Response("Success")


def login_user(request):
	if request.method == "GET":
		if request.user.is_authenticated:
			return HttpResponseRedirect(reverse('todolist'))
		return render(request, 'todo/login.html')

	elif request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')
		print(email,password)
		try:
			user = User.objects.get(email=email)
			user = authenticate(request, username=user.username, password=password)
			if user is not None:
				login(request, user)
				return HttpResponseRedirect(reverse('todolist'))
			return Response("Wrong username and password.")
		except Exception as e:
			print(e)
			return Response("Wrong username and password.")


def register(request):
	if request.method == 'GET':
		if request.user.is_authenticated:
			return HttpResponseRedirect(reverse('todolist'))
		return render(request, 'todo/register.html')

	if request.method == 'POST':
		name = request.POST.get('name')
		email = request.POST.get('email')
		password = request.POST.get('password')

		try:
			user =User()
			user.username = email.split('@')[0]
			user.first_name = name
			user.email = email
			user.set_password(password)
			user.save()
			return HttpResponseRedirect(reverse('login'))
		except Exception as e:
			print(e)
			return HttpResponseRedirect(reverse('register'))

def logout_user(request):
	logout(request)
	return HttpResponseRedirect(reverse('login'))

def todolist(request):
	if request.user.is_authenticated:
		print(request.user,request.user.first_name, "todolist")
		objects = TodoApp.objects.filter(owner=request.user)
		tasks = {}
		tasks["todos"] = objects
		tasks["user"] = request.user
		return render(request, 'todo/index.html', tasks)
	else:
		return HttpResponseRedirect(reverse('login'))