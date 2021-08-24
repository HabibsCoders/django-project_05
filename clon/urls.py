from django.urls import path, include
from. import views

app_name = 'clon'

urlpatterns = [
     path('', views.clon, name='clon'),
    
]


