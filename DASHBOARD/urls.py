from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard,name='dashboard' ),
    path('search',views.search,name='search' ),
]