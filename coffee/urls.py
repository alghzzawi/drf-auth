from django.urls import path
from .views import CoffeeListCreateView, CoffeeDetailView

urlpatterns = [
    path('',CoffeeListCreateView.as_view(),name='coffee_list_create'),
    path('<int:pk>',CoffeeDetailView.as_view(),name='coffee_detail')
]