from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterForm, ProfileForm


def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, '🎉 Добро пожаловать в SAB Trading Plaza!')
            return redirect('edit_profile')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            if user.profile.is_banned:
                messages.error(request, f'🚫 Вы заблокированы. Причина: {user.profile.ban_reason or "нарушение правил"}')
                return redirect('login')
            login(request, user)
            messages.success(request, f'👋 Привет, {user.profile.display_name()}!')
            return redirect(request.GET.get('next', 'index'))
        else:
            messages.error(request, '❌ Неверный логин или пароль')
    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    messages.info(request, '👋 Вы вышли из аккаунта')
    return redirect('index')


@login_required
def edit_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Профиль обновлён!')
            return redirect('profile', username=request.user.username)
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'accounts/edit_profile.html', {'form': form})


def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    listings = user.listings.filter(is_active=True)
    return render(request, 'accounts/profile.html', {'profile_user': user, 'listings': listings})


@login_required
def ban_user(request, username):
    if not request.user.is_superuser:
        messages.error(request, '❌ Нет доступа')
        return redirect('index')
    target = get_object_or_404(User, username=username)
    if request.method == 'POST':
        reason = request.POST.get('reason', 'нарушение правил')
        target.profile.is_banned = True
        target.profile.ban_reason = reason
        target.profile.status = 'banned'
        target.profile.save()
        # Деактивируем все объявления
        target.listings.update(is_active=False)
        messages.success(request, f'🚫 Пользователь {target.username} заблокирован')
        return redirect('profile', username=username)
    return render(request, 'accounts/ban_user.html', {'target': target})


@login_required
def unban_user(request, username):
    if not request.user.is_superuser:
        messages.error(request, '❌ Нет доступа')
        return redirect('index')
    target = get_object_or_404(User, username=username)
    target.profile.is_banned = False
    target.profile.ban_reason = ''
    target.profile.status = 'user'
    target.profile.save()
    messages.success(request, f'✅ Пользователь {target.username} разблокирован')
    return redirect('profile', username=username)


@login_required
def admin_panel(request):
    if not request.user.is_superuser:
        messages.error(request, '❌ Нет доступа')
        return redirect('index')
    from store.models import Listing
    users = User.objects.select_related('profile').order_by('-date_joined')
    listings = Listing.objects.filter(is_active=True).select_related('author', 'brainrot').order_by('-created_at')
    banned = User.objects.filter(profile__is_banned=True)
    context = {
        'users': users,
        'listings': listings,
        'banned': banned,
        'total_users': users.count(),
        'total_listings': listings.count(),
        'total_banned': banned.count(),
    }
    return render(request, 'accounts/admin_panel.html', context)


@login_required
def admin_delete_listing(request, pk):
    if not request.user.is_superuser:
        messages.error(request, '❌ Нет доступа')
        return redirect('index')
    from store.models import Listing
    listing = get_object_or_404(Listing, pk=pk)
    listing.is_active = False
    listing.save()
    messages.success(request, '🗑️ Объявление удалено администратором')
    return redirect('admin_panel')
