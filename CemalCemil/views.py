from django.shortcuts import render
from rest_framework import generics
from .models import Pelanggan
from.serializers import PelangganSerializer

class PelangganListCreate(generics.ListCreateAPIView):
    queryset = Pelanggan.objects.all()
    serializer_class = PelangganSerializer
