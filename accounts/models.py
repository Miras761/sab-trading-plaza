from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    STATUS_CHOICES = [
        ('user', 'Пользователь'),
        ('creator', 'Создатель'),
        ('moderator', 'Модератор'),
        ('banned', 'Заблокирован'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    nickname = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    bio = models.TextField(max_length=300, blank=True)
    roblox_username = models.CharField(max_length=50, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='user')
    is_banned = models.BooleanField(default=False)
    ban_reason = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"Profile of {self.user.username}"

    def display_name(self):
        return self.nickname or self.user.username

    def get_avatar(self):
        if self.avatar:
            return self.avatar.url
        return None

    def status_color(self):
        colors = {
            'creator': '#00ff88',
            'moderator': '#60a5fa',
            'banned': '#f87171',
            'user': '#7dffb0',
        }
        return colors.get(self.status, '#7dffb0')

    def status_label(self):
        labels = {
            'creator': '👑 Создатель',
            'moderator': '🛡️ Модератор',
            'banned': '🚫 Заблокирован',
            'user': '👤 Пользователь',
        }
        return labels.get(self.status, '👤 Пользователь')


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
