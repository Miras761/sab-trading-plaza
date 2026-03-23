from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Listing, Brainrot, Comment, RARITY_CHOICES, BRAINROT_LIST, DELETE_REASON_CHOICES
from .forms import ListingForm, CommentForm, DeleteListingForm


def index(request):
    category = request.GET.get('category', '')
    rarity = request.GET.get('rarity', '')
    search = request.GET.get('search', '')

    listings = Listing.objects.filter(is_active=True).select_related('author', 'author__profile', 'brainrot')

    if category:
        listings = listings.filter(category=category)
    if rarity:
        listings = listings.filter(brainrot__rarity=rarity)
    if search:
        listings = listings.filter(
            Q(title__icontains=search) |
            Q(description__icontains=search) |
            Q(brainrot__name__icontains=search) |
            Q(custom_brainrot_name__icontains=search)
        )

    stats = {
        'total': Listing.objects.filter(is_active=True).count(),
        'trade': Listing.objects.filter(is_active=True, category='trade').count(),
        'sell': Listing.objects.filter(is_active=True, category='sell').count(),
        'giveaway': Listing.objects.filter(is_active=True, category='giveaway').count(),
    }

    context = {
        'listings': listings,
        'stats': stats,
        'selected_category': category,
        'selected_rarity': rarity,
        'search': search,
        'rarity_choices': RARITY_CHOICES,
    }
    return render(request, 'store/index.html', context)


def listing_detail(request, pk):
    listing = get_object_or_404(Listing, pk=pk, is_active=True)
    comments = listing.comments.select_related('author', 'author__profile').all()
    form = CommentForm()

    if request.method == 'POST' and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.listing = listing
            comment.author = request.user
            comment.save()
            messages.success(request, '💬 Комментарий добавлен!')
            return redirect('listing_detail', pk=pk)

    context = {
        'listing': listing,
        'comments': comments,
        'form': form,
    }
    return render(request, 'store/listing_detail.html', context)


@login_required
def create_listing(request):
    brainrots_by_rarity = {}
    for br in Brainrot.objects.all().order_by('rarity', 'name'):
        key = br.get_rarity_display()
        if key not in brainrots_by_rarity:
            brainrots_by_rarity[key] = []
        brainrots_by_rarity[key].append(br)

    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.author = request.user
            listing.save()
            messages.success(request, '✅ Объявление создано!')
            return redirect('listing_detail', pk=listing.pk)
    else:
        form = ListingForm()

    context = {
        'form': form,
        'brainrots_by_rarity': brainrots_by_rarity,
    }
    return render(request, 'store/create_listing.html', context)


@login_required
def delete_listing(request, pk):
    listing = get_object_or_404(Listing, pk=pk, author=request.user, is_active=True)

    if request.method == 'POST':
        form = DeleteListingForm(request.POST)
        if form.is_valid():
            listing.is_active = False
            listing.save()
            reason = dict(DELETE_REASON_CHOICES).get(form.cleaned_data['reason'], '')
            messages.success(request, f'🗑️ Объявление удалено. Причина: {reason}')
            return redirect('index')
    else:
        form = DeleteListingForm()

    return render(request, 'store/delete_listing.html', {'listing': listing, 'form': form})


@login_required
def my_listings(request):
    listings = Listing.objects.filter(author=request.user, is_active=True)
    return render(request, 'store/my_listings.html', {'listings': listings})


def donate(request):
    from django.conf import settings
    context = {
        'paypal_email': getattr(settings, 'PAYPAL_EMAIL', ''),
        'paypal_username': getattr(settings, 'PAYPAL_USERNAME', ''),
        'paypal_button_id': getattr(settings, 'PAYPAL_BUTTON_ID', ''),
    }
    return render(request, 'store/donate.html', context)
