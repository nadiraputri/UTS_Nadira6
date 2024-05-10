from django.db import models

# Create your models here.
class Pesanan(models.Model):
    nama_pesanan = models.CharField(max_length=100)
    meja = models.TextField()
    jumlah = models.TextField()
    total = models.TextField()
    
    def __str__(self):
        return self.nama_pesanan
    
class Kasir(models.Model):
    Pesanan = models.ForeignKey(Pesanan, related_name='kasir', on_delete=models.CASCADE)
    nama_pelanggan = models.CharField(max_length=100)
    total = models.TextField()
    uang_masuk = models.TextField()
    kembalian = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):  
        return self.Pesanan
    
class Pelanggan(models.Model):
    nama = models.CharField(max_length=100)
    published_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nama
    
class Meja(models.Model):
    nomor_meja = models.CharField(max_length=100)
    pesanan = models.TextField()
    
    def __str__(self):
        return self.nomor_meja
