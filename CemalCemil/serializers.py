from rest_framework import serializers
from .models import Pelanggan, Pesanan, Meja, Kasir

class PelangganSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelanggan
        fields = ["id", "nama", "pesanan", "published_date"]

class PesananSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pesanan
        fields = ["id", "nama_pesanan", "pembelian", "jumlah", "total", "published_date"]
        
class MejaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meja
        fields = ["id", "nomor_meja", "pesanan"]
        
class KasirSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kasir
        fields = ["id", "nama_pelanggan", "pesanan", "total", "uang_masuk", "kembalian", "published_date"]