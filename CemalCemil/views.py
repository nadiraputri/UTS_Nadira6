from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Pelanggan
from.serializers import PelangganSerializer

class PelangganListCreate(generics.ListCreateAPIView):
    queryset = Pelanggan.objects.all()
    serializer_class = PelangganSerializer
    
    def delete(self, request, *args, **kwargs):
        Pelanggan.objects.all().delete()
        return Response(status=status.HTTP_204__NO_CONTEN)
    
class PelangganRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pelanggan.objects.all()
    serializer_class = PelangganSerializer
    lookup_field = "pk"
