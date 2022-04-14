from datetime import datetime
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from rest_framework import routers
from app import viewsets as appviewsets


route = routers.DefaultRouter()

route.register(r'appempresa', appviewsets.EmpresaViewSet, basename="Empresa")

route.register(r'appcliente', appviewsets.ClienteViewSet, basename="Cliente")

route.register(r'appoffer', appviewsets.OfertaViewSet, basename="Oferta")

route.register(r'applance', appviewsets.LanceViewSet, basename="Lance")


urlpatterns = [
    path('', include(route.urls)),
    path('admin/', admin.site.urls),
]
