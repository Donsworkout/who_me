from django.contrib import admin
from django.urls import include, path
from who_me import views

urlpatterns = [
    path('', views.index, name='index'),
    path('face_recognition/', views.face_recognition , name='face_recognition'),
    path('admin/', admin.site.urls),
]
