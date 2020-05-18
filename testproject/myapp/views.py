from django.shortcuts import render
from .serializer import MemberSerializer,ActivitySerializer
from rest_framework import viewsets
from .models import Members,Activity_periods
# Create your views here.
class MemberView(viewsets.ModelViewSet):
    queryset = Members.objects.all()
    serializer_class = MemberSerializer
class ActivityView(viewsets.ModelViewSet):
    queryset = Activity_periods.objects.all()
    serializer_class = ActivitySerializer