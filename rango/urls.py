from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('category/<slug:category_name_slug>/',
         views.show_category,
         name='show_category'),
    path('add_category/', views.add_category, name='add_category'),
    path('category/<slug:category_name_slug>/add_page/',
         views.add_page,
         name='add_page'),
    path('restricted/', views.restricted, name='restricted'),
    path('category/<slug:category_name_slug>/add_comment/',
         views.add_comment,
         name='add_comment'),
     path('delete_comment/', views.delete_comment, name='delete_comment'),
     #like
     path('like_category/', views.like_category, name='like_category'),
     path('like_comment/', views.like_comment, name='like_comment'),
]