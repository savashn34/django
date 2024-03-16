from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="baslangic"),
    path("index", views.index),
    path("о_словаре", views.bilgilendirme, name="bilgilendirme"),
    path("bukva", views.sozcukler, name="sozcukler"),
    path("<slug:slug>", views.icerik, name="icerik_baglanti"),
    path("bukva/<slug:slug>", views.seslere_gore_sozcukler, name="seslere_gore_sozcukler"),
    path("jazyk/<slug:slug>", views.dillere_gore_sozcukler, name="dillere_gore_sozcukler"),
    path('search/', views.search, name='search'),
    path('results/<str:search_term>/', views.search_results, name='search_results')
]
