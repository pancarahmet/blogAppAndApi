"""BlogAppAndApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from blog.views import index
from blog.api_views import *
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings


router=DefaultRouter()
# router.register(r'listpost',PostListSet,basename="listpost")
# router.register(r'updatepost',PostUpdateSet,basename="updatepost")
# router.register(r'deletepost',PostDeleteSet,basename="deletepost")
router.register(r'posts',PostViewSet,basename='postsView')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('blog/',include('blog.urls')),
    path('api/',include(router.urls)),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
