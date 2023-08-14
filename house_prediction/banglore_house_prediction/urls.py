from django.urls import path
from . import views

app_name ='banglore_house_prediction'

urlpatterns = [
    path('', views.return_price,name="return_price"),
]
