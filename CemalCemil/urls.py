from django.urls import path
from . import views

urlpatterns = [
    path("pelanggan/", views.PelangganListCreate.as_view(), name="Pelanggan-views-create"),
    path("pelanggan/<int:pk>/", views.PelangganRetrieveUpdateDestory.as_view(), name="Update"),
]
