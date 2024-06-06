from django.urls import path
from inicio import views
urlpatterns = [
    path('', views.inicio, name="inicio"),
    path("", views.inicio),
    path("template1/<str:nombre>/<str:apellido>/<int:edad>", views.template1),
    path("template2/<str:nombre>/<str:apellido>/<int:edad>", views.template4),
    path("prueba/", views.probando, name="probando"),
    path("autos/crear/<str:marca>/<str:modelo>",views.crear_auto, name="crear_auto"),
    
]
