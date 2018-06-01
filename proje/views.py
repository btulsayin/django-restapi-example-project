from django.shortcuts import render

# Create your views here.
# Django user ve group modelleri
from django.contrib.auth.models import User, Group
# rest_framework'in viewsets'i
from rest_framework import viewsets
# serializers.py'in bulunduğu klasör adından hepsini import ettik.
from .serializers import *


class UserViewSet(viewsets.ModelViewSet):
    # en son kayıt olan kullanıcan itibaren sıraladık
    queryset = User.objects.all().order_by('-date_joined')
    # Form mantığı gibi düşünün, çağıralın modelin formu
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    # Bütün grup modelini çağırdık
    queryset = Group.objects.all()
    # Group modelin formu
    serializer_class = GroupSerializer