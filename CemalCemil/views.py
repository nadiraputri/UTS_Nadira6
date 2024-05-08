from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Pelanggan, Pesanan, Meja, Kasir
from.serializers import PelangganSerializer, PesananSerializer, MejaSerializer, KasirSerializer
from rest_framework.views import APIView
from.serializers import PesananSerializer

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
    
class PesananListCreate(generics.ListCreateAPIView):
    queryset = Pesanan.objects.all()
    serializer_class = PesananSerializer
    
    def delete(self, request, *args, **kwargs):
        Pesanan.objects.all().delete()
        return Response(status=status.HTTP_204__NO_CONTEN)
    
class PesananRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pesanan.objects.all()
    serializer_class = PesananSerializer
    lookup_field = "pk"

class MejaListCreate(generics.ListCreateAPIView):
    queryset = Meja.objects.all()
    serializer_class = MejaSerializer
    
    def delete(self, request, *args, **kwargs):
        Meja.objects.all().delete()
        return Response(status=status.HTTP_204__NO_CONTEN)
    
class MejaRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meja.objects.all()
    serializer_class = MejaSerializer
    lookup_field = "pk"
    
class KasirListCreate(generics.ListCreateAPIView):
    queryset = Kasir.objects.all()
    serializer_class = KasirSerializer
    
    def delete(self, request, *args, **kwargs):
        Kasir.objects.all().delete()
        return Response(status=status.HTTP_204__NO_CONTEN)
    
class KasirRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kasir.objects.all()
    serializer_class = KasirSerializer
    lookup_field = "pk"