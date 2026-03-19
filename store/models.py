from django.db import models
from django.contrib.auth.models import User

RARITY_CHOICES = [
    ('common', 'Common'),
    ('rare', 'Rare'),
    ('epic', 'Epic'),
    ('legendary', 'Legendary'),
    ('mythic', 'Mythic'),
    ('brainrot_god', 'Brainrot God'),
    ('secret', 'Secret'),
    ('og', 'OG'),
]

RARITY_COLORS = {
    'common': '#9ca3af',
    'rare': '#3b82f6',
    'epic': '#a855f7',
    'legendary': '#f59e0b',
    'mythic': '#ec4899',
    'brainrot_god': '#ef4444',
    'secret': '#06b6d4',
    'og': '#10b981',
}

CATEGORY_CHOICES = [
    ('trade', 'Трейд'),
    ('sell', 'Продаю'),
    ('giveaway', 'Раздача'),
]

DELETE_REASON_CHOICES = [
    ('traded', 'Трейд совершён'),
    ('sold', 'Продано'),
    ('given', 'Отдано'),
    ('other', 'Другая причина'),
]

BRAINROT_LIST = [
    # Common
    ('Noobini Pizzanini', 'common'),
    ('Lirili Larila', 'common'),
    ('Tim Cheesee', 'common'),
    ('Frurifrura', 'common'),
    ('Talpa Di Ferro', 'common'),
    ('Svivina Borbardino', 'common'),
    ('Noobini Santanini', 'common'),
    ('Raccooni Jandelini', 'common'),
    ('Pipi Kiwi', 'common'),
    ('Tartaragno', 'common'),
    ('Pipi Corni', 'common'),
    ('Borborino Saltarino', 'common'),
    # Rare
    ('Trippi Troppi', 'rare'),
    ('Gangster Footera', 'rare'),
    ('Patata Fritta', 'rare'),
    ('Crocodilino Rampante', 'rare'),
    ('Papagallo Azzurro', 'rare'),
    ('Serpentino Agitato', 'rare'),
    ('Fenicottero Alato', 'rare'),
    ('Farfallino Colorato', 'rare'),
    # Epic
    ('Bombardiro Crocodilo', 'epic'),
    ('Tralalero Tralala', 'epic'),
    ('Brr Brr Patapim', 'epic'),
    ('Bing Bing Bong', 'epic'),
    ('Lirilì Larilà', 'epic'),
    ('Capuccino Assassino', 'epic'),
    ('Bananino Caramellato', 'epic'),
    ('Polpo Spaghettoso', 'epic'),
    ('Gattino Volante', 'epic'),
    ('Tiranosaurio Rex Fantasmino', 'epic'),
    ('Squalo Carpiato', 'epic'),
    # Legendary
    ('Burbaloni Loliloli', 'legendary'),
    ('Chimpanzini Bananini', 'legendary'),
    ('Ballerina Cappuccina', 'legendary'),
    ('Chef Crabracadaba', 'legendary'),
    ('Lionel Cactuseli', 'legendary'),
    ('Glorbo Fruttodillo', 'legendary'),
    ('Quivioli Ameleonni', 'legendary'),
    ('Blueberrenni Octopusini', 'legendary'),
    ('Clickerino Clabo', 'legendary'),
    ('Caramello Filtrello', 'legendary'),
    ('Pipi Potato', 'legendary'),
    ('Strawberrlli Flamingelli', 'legendary'),
    ('Cocosino Mamá', 'legendary'),
    ('Pandaccini Bananini', 'legendary'),
    ('Quackula Pipi Watermelon', 'legendary'),
    ('Signore Carapece', 'legendary'),
    ('Sigma Boy', 'legendary'),
    ('Chocco Bunny Puffaball', 'legendary'),
    ('Sigma Girl Sealo', 'legendary'),
    ('Buho De Fuego', 'legendary'),
    ('Kirilikalika Kirilikalato', 'legendary'),
    # Mythic
    ('Tung Tung Tung Sahur', 'mythic'),
    ('La Vacca Saturno Saturnita', 'mythic'),
    ('Brr Brr Patapim Avanzado', 'mythic'),
    ('Gattatino Nyanino', 'mythic'),
    ('Giraffini Longocollo', 'mythic'),
    ('Elefantino Magico', 'mythic'),
    ('Delfino Spaziale', 'mythic'),
    ('Orso Polare Cosmico', 'mythic'),
    ('Tartaruga Ninja Pizzaiola', 'mythic'),
    ('Unicorno Pastello', 'mythic'),
    ('Rinoceronte Motociclista', 'mythic'),
    # Brainrot God
    ('Tralalero Tralalero', 'brainrot_god'),
    ('Il Grande Bombardiro', 'brainrot_god'),
    ('Ballerina Suprema', 'brainrot_god'),
    ('Re Dei Brainrot', 'brainrot_god'),
    # Secret
    ('Graipuss Medussi', 'secret'),
    ('Los Tralaleritos', 'secret'),
    ('Smurf Cat', 'secret'),
    ('Pineapple Owl', 'secret'),
    ('Skibidi Toilet', 'secret'),
    ('Meowl', 'secret'),
    ('Headless Horseman', 'secret'),
    ('Yin Yang Dragon', 'secret'),
    # OG
    ('Strawberry Elephant', 'og'),
    ('Meowl OG', 'og'),
    ('Skibidi Toilet OG', 'og'),
    ('Developini Braziliaspidini', 'og'),
    ('Kings Coleslaw', 'og'),
]


class Brainrot(models.Model):
    name = models.CharField(max_length=100, unique=True)
    rarity = models.CharField(max_length=20, choices=RARITY_CHOICES, default='common')
    image = models.ImageField(upload_to='brainrots/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['rarity', 'name']

    def __str__(self):
        return f"{self.name} ({self.get_rarity_display()})"

    def rarity_color(self):
        return RARITY_COLORS.get(self.rarity, '#9ca3af')


class Listing(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=200)
    description = models.TextField()
    brainrot = models.ForeignKey(Brainrot, on_delete=models.SET_NULL, null=True, blank=True, related_name='listings')
    custom_brainrot_name = models.CharField(max_length=100, blank=True)
    custom_brainrot_image = models.ImageField(upload_to='custom_brainrots/', blank=True, null=True)
    want_description = models.CharField(max_length=300, blank=True, help_text='Что хочу получить взамен')
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"[{self.get_category_display()}] {self.title}"

    def get_brainrot_name(self):
        if self.brainrot:
            return self.brainrot.name
        return self.custom_brainrot_name or 'Не указан'

    def get_brainrot_image(self):
        if self.custom_brainrot_image:
            return self.custom_brainrot_image.url
        if self.brainrot and self.brainrot.image:
            return self.brainrot.image.url
        return None

    def get_brainrot_rarity(self):
        if self.brainrot:
            return self.brainrot.rarity
        return 'common'


class Comment(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    is_trade_offer = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"{self.author.username}: {self.text[:50]}"
