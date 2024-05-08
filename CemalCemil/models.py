from django.db import models

# Create your models here.
class Pelanggan(models.Model):
    nama = models.CharField(max_length=100)
    pesanan = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nama
