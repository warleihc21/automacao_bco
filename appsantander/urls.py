from django.urls import path
from . import views

app_name = "appsantander"   

urlpatterns = [
  path("", views.homepage, name="homepage"),
  
]