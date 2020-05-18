from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('member/', views.MemberView)
router.register('act/',views.ActivityView)

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include(router.urls))
]
