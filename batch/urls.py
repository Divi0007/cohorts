from django.urls import path
from .views import frontpage, batch_detail, edit_batch, agegroup_detail, add_batch, search,vacant_detail


urlpatterns=[
    
    path('add_batch/', add_batch, name='add_batch'),
    path('search/', search, name='search'),
    path('vacant/<slug:slug>/', vacant_detail, name='vacant_detail'),
    path('<slug:slug>/', agegroup_detail, name='agegroup_detail'),
    path('edit-batch/<int:pk>/', edit_batch, name='edit_batch'),
    path('<slug:agegroup_slug>/<slug:slug>/', batch_detail, name='batch_detail'),
    path('',frontpage, name="frontpage"),
    
]