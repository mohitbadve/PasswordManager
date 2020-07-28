from django.contrib import admin
from django.urls import path, include
from app.views import *

urlpatterns = [
    path('user/',registerUser),
    path('user/auth/',authUser),
    path('sites/list/',getWebsites),
    path('sites/',addWebsite),
 ]