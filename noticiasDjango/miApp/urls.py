from django.db import router
from django.urls import path, include
from .views import  home, eliminarNoticia, modificarNoticia, listarNoticias, contacto, login, agregarNoticia, quienessomos, sismos, tarjetaNoticia, NoticiaViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('noticias', NoticiaViewset)

urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('login/', login, name="login"),
    path('quienessomos/', quienessomos, name="quienessomos"),
    path('sismos/', sismos, name="sismos"),
    path('tarjetaNoticia/', tarjetaNoticia, name="tarjetaNoticia"),
    path('agregarNoticia/', agregarNoticia, name="agregarNoticia"),
    path('listarNoticias/', listarNoticias, name="listarNoticias"),
    path('modificarNoticia/<id>/', modificarNoticia, name="modificarNoticia"),
    path('eliminarNoticia/<id>/', eliminarNoticia, name="eliminarNoticia"),
    path('api/', include(router.urls)),
]