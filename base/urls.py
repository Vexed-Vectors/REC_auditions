from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    
    path('', views.index, name='index' ),
    path('experiences/', views.experiences, name='experiences'),
    path('create-experience/', views.create_experience, name='create-experience'),
    path('experience/<int:pk>', views.experienceDetail, name= 'experienceDetail'),

]
