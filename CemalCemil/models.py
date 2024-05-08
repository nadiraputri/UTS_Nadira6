from django.db import models

# Create your models here.
class Pelanggan(models.Model):
    nama = models.CharField(max_length=100)
    pesanan = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nama
    
class Pesanan(models.Model):
    nama_pesanan = models.CharField(max_length=100)
    pembelian = models.TextField()
    jumlah = models.TextField()
    total = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nama_pesanan
    
class Meja(models.Model):
    nomor_meja = models.CharField(max_length=100)
    pesanan = models.TextField()
    
    def __str__(self):
        return self.nomor_meja

class Kasir(models.Model):
    nama_pelanggan = models.CharField(max_length=100)
    pesanan = models.TextField()
    total = models.TextField()
    uang_masuk = models.TextField()
    kembalian = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nama_pelanggan