from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Pelanggan, Pesanan, Meja, Kasir
from .serializers import PelangganSerializer, PesananSerializer, MejaSerializer, KasirSerializer
from rest_framework.views import APIView

class PelangganListCreate(generics.ListCreateAPIView):
    queryset = Pelanggan.objects.all()
    serializer_class = PelangganSerializer
    
    def delete(self, request, *args, **kwargs):
        Pelanggan.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class PelangganRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pelanggan.objects.all()
    serializer_class = PelangganSerializer
    lookup_field = "pk"
    
class PesananListCreate(generics.ListCreateAPIView):
    queryset = Pesanan.objects.all()
    serializer_class = PesananSerializer
    
    def delete(self, request, *args, **kwargs):
        Pesanan.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class PesananRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pesanan.objects.all()
    serializer_class = PesananSerializer
    lookup_field = "pk"

class MejaListCreate(generics.ListCreateAPIView):
    queryset = Meja.objects.all()
    serializer_class = MejaSerializer
    
    def delete(self, request, *args, **kwargs):
        Meja.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class MejaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meja.objects.all()
    serializer_class = MejaSerializer
    lookup_field = "pk"
    
class KasirListCreate(generics.ListCreateAPIView):
    queryset = Kasir.objects.all()
    serializer_class = KasirSerializer
    
    def delete(self, request, *args, **kwargs):
        Kasir.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class KasirRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kasir.objects.all()
    serializer_class = KasirSerializer
    lookup_field = "pk"
    
class PelangganList(APIView):
    def get(self, request, format=None):
        pelanggan = Pelanggan.objects.all()
        serializer = PelangganSerializer(pelanggan, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PelangganSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class PesananList(APIView):
    def get(self, request, format=None):
        pesanan = Pesanan.objects.all()
        serializer = PesananSerializer(pesanan, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PesananSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MejaList(APIView):
    def get(self, request, format=None):
        meja = Meja.objects.all()
        serializer = MejaSerializer(meja, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MejaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class KasirList(APIView):
    def get(self, request, format=None):
        kasir = Kasir.objects.all()
        serializer = KasirSerializer(kasir, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = KasirSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)