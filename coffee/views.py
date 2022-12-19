from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Coffee
from .serializers import CoffeeSerializer
from .permissions import OwnerOnly
# Create your views here.
class CoffeeListCreateView(ListCreateAPIView):
    queryset=Coffee.objects.all()
    serializer_class=CoffeeSerializer

class CoffeeDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Coffee.objects.all()
    serializer_class=CoffeeSerializer
    permission_classes=[OwnerOnly]