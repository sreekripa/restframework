from django.contrib.auth import get_user_model

from . models import Task
from rest_framework import serializers


class TaskSerializer(serializers.ModelSerializer):
    image=serializers.ImageField(max_length=None,use_url=True)
    class Meta:
        model=Task
        fields=['id','Task_name','Task_desc','date_created','completed','image']


class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    def create(self, validated_data):
        user=get_user_model().objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    class Meta:
        model=get_user_model()
        fields=('username','password')

