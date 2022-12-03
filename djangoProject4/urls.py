from django.contrib import admin
from django.urls import path
from coursach import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('tour/<int:pk>', views.create)
]
