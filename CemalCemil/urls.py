from django.urls import path
from . import views

urlpatterns = [
    path("pelanggan/", views.PelangganListCreate.as_view(), name="Pelanggan-views-create"),
    path("pelanggan/<int:pk>/", views.PelangganRetrieveUpdateDestory.as_view(), name="Update"),
    path("pesanan/", views.PesananListCreate.as_view(), name="Pesanan-views-create"),
    path("pesanan/<int:pk>/", views.PesananRetrieveUpdateDestory.as_view(), name="Update"),
    path("meja/", views.MejaListCreate.as_view(), name="Meja-views-create"),
    path("meja/<int:pk>/", views.MejaRetrieveUpdateDestory.as_view(), name="Update"),
    path("kasir/", views.KasirListCreate.as_view(), name="Kasir-views-create"),
    path("kasir/<int:pk>/", views.KasirRetrieveUpdateDestory.as_view(), name="Update"),
]
