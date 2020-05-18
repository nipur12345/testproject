from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register('new',views.MyAccountView)
urlpatterns=[
    path('api/', include(router.urls))
]