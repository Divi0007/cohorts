from django.urls import path
from django.contrib.auth import views as auth_views
from .views import frontpage, batch_detail, edit_batch, agegroup_detail, add_batch, search,vacant_detail, savedata,login_view, logout_view


urlpatterns=[
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('add_batch/', add_batch, name='add_batch'),
    path('search/', search, name='search'),
    path('vacant/<slug:slug>/', vacant_detail, name='vacant_detail'),
    path('<slug:slug>/', agegroup_detail, name='agegroup_detail'),
    path('save/<int:pk>/', savedata, name='savedata'),
    path('edit-batch/<int:pk>/', edit_batch, name='edit_batch'),
    path('<slug:agegroup_slug>/<slug:slug>/', batch_detail, name='batch_detail'),
    path('',frontpage, name="frontpage"),
    
]