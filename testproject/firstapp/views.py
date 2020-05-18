from django.shortcuts import render
from .models import Members
from .cjson import AccountSer
from rest_framework import viewsets


# Create your views here.
class MyAccountView(viewsets.ModelViewSet):
    serializer_class = AccountSer
    queryset = Members.objects.all()
    print(queryset)
