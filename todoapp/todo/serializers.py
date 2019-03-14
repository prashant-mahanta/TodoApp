from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import *

class UserSerializer(ModelSerializer):

	class Meta:
		model = User
		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
			]

		extra_kwargs = {
			'password': {'write_only':True}
		}

class TodoAppSerializer(ModelSerializer):
	owner = UserSerializer(required=True, many=False)
	
	class Meta:
		model = TodoApp
		fields = "__all__"
