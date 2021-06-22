from django.contrib import admin
from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',csrf_exempt(views.home),name="home"),
    path('result/',csrf_exempt(views.result),name="result")
]
