from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/<str:username>/', views.profile_view, name='profile'),
    path('ban/<str:username>/', views.ban_user, name='ban_user'),
    path('unban/<str:username>/', views.unban_user, name='unban_user'),
    path('admin-panel/', views.admin_panel, name='admin_panel'),
    path('admin-panel/delete/<int:pk>/', views.admin_delete_listing, name='admin_delete_listing'),
]
