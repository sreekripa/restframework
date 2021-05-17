from django.contrib.auth import get_user_model
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView

from . models import Task
from . serializers import TaskSerializer,UserSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny

class Taskviewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset=Task.objects.all().order_by('-date_created')
    serializer_class=TaskSerializer

class DueTaskviewset(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-date_created').filter(completed=False)
    serializer_class = TaskSerializer

class CreateUserView(CreateAPIView):
    model=get_user_model()
    permission_classes = (AllowAny),
    serializer_class = UserSerializer



class CompletedTaskviewset(viewsets.ModelViewSet):
    queryset=Task.objects.all().order_by('-date_created').filter(completed=True)
    serializer_class=TaskSerializer



