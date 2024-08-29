from django.contrib import admin
from django.urls import path

from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home-page'),
    path('feedback/<int:id>', views.customer_feedback, name='customer-feedback'),
    path('graph/', views.GraphView.as_view(), name='graph-page'),
]
