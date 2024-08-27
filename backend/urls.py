from django.contrib import admin
from django.urls import path

from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='home-page'),
    path('graph/', views.GraphView.as_view(), name='graph-page'),
]
