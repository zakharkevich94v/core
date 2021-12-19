from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'), 
    path('all_vacancy', views.all_vacancy, name='all_vacancy'),  
    path('one_vacancy/<vacncy_id>', views.description_one_vacancy, name='one_vacancy'),
]
