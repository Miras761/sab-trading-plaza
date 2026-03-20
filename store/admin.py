from django.contrib import admin
from .models import Brainrot, Listing, Comment

@admin.register(Brainrot)
class BrainrotAdmin(admin.ModelAdmin):
    list_display = ['name', 'rarity']
    list_filter = ['rarity']
    search_fields = ['name']

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'author', 'is_active', 'created_at']
    list_filter = ['category', 'is_active']
    search_fields = ['title', 'author__username']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'listing', 'is_trade_offer', 'created_at']
