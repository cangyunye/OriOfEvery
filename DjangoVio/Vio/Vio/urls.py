"""Vio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from calc import views as calc_views
from rest_framework import routers
from restquick import views as rq


router = routers.DefaultRouter()
router.register(r'users',rq.UserViewSet)
router.register(r'groups',rq.GroupViewSet)

urlpatterns = [
    path('chat/',include('chat.urls')),
    path('polls/',include('polls.urls')),
    path('home/',calc_views.index,name='home'),
    path('add/',calc_views.add,name='add'), # add_new
    path('add/<int:a>/<int:b>/',calc_views.add2,name='add2'), # add_new
    path('admin/', admin.site.urls),
    path('', include('navi.urls')),
    path('codeinfo/',include('codeinfo.urls')),
    path('rq/',include(router.urls)),
    path('rq/api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    path('snippets/',include('snippets.urls')),
]
