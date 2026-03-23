from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listing/<int:pk>/', views.listing_detail, name='listing_detail'),
    path('listing/create/', views.create_listing, name='create_listing'),
    path('listing/<int:pk>/delete/', views.delete_listing, name='delete_listing'),
    path('my-listings/', views.my_listings, name='my_listings'),
    path('donate/', views.donate, name='donate'),
]
