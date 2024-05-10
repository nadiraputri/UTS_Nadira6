from rest_framework import serializers
from .models import Pelanggan, Pesanan, Meja, Kasir

class PelangganSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelanggan
        fields = ["id", "nama", "published_date"]

class PesananSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pesanan
        fields = ["id", "nama_pesanan", "meja", "jumlah", "total"]
        
class MejaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meja
        fields = ["id", "nomor_meja", "pesanan"]
        
class KasirSerializer(serializers.ModelSerializer):
    # pesanan = serilizers.PriaryKeyRelatedfield(many=True, read_only=True)
    class Meta:
        model = Kasir
        fields = ["id", "Pesanan", "nama_pelanggan", "total", "uang_masuk", "kembalian", "published_date"]