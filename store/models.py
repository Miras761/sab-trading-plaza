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
    ('Noobini Pizzanini', 'common'), ('Lirili Larila', 'common'), ('Tim Cheese', 'common'),
    ('Fluriflura', 'common'), ('Talpa Di Fero', 'common'), ('Noobini Santanini', 'common'),
    ('Svinina Bombardino', 'common'), ('Raccooni Jandelini', 'common'), ('Pipi Kiwi', 'common'),
    ('Tartaragno', 'common'), ('Pipi Corni', 'common'), ('Holy Arepa', 'common'),
    # Rare
    ('Trippi Troppi', 'rare'), ('Gangster Footera', 'rare'), ('Bandito Bobritto', 'rare'),
    ('Boneca Ambalabu', 'rare'), ('Cacto Hipopotamo', 'rare'), ('Ta Ta Ta Ta Sahur', 'rare'),
    ('Cupcake Koala', 'rare'), ('Tric Trac Baraboom', 'rare'), ('Frogo Elfo', 'rare'),
    ('Pipi Avocado', 'rare'), ('Pengolino Nuvoletto', 'rare'), ('Pinealotto Fruttarino', 'rare'),
    # Epic
    ('Cappuccino Assassino', 'epic'), ('Bandito Axolito', 'epic'), ('Brr Brr Patapim', 'epic'),
    ('Trulimero Trulicina', 'epic'), ('Bambini Crostini', 'epic'), ('Bananita Dolphinita', 'epic'),
    ('Perochello Lemonchello', 'epic'), ('Brri Brri Bicus Dicus Bombicus', 'epic'),
    ('Avocadini Guffo', 'epic'), ('Salamino Penguino', 'epic'), ('Ti Ti Ti Sahur', 'epic'),
    ('Penguin Tree', 'epic'), ('Penguino Cocosino', 'epic'),
    # Legendary
    ('Burbaloni Loliloli', 'legendary'), ('Chimpanzini Bananini', 'legendary'),
    ('Ballerina Cappuccina', 'legendary'), ('Chef Crabracadabra', 'legendary'),
    ('Lionel Cactuseli', 'legendary'), ('Glorbo Fruttodrillo', 'legendary'),
    ('Blueberrini Octopusini', 'legendary'), ('Strawberelli Flamingelli', 'legendary'),
    ('Pandaccini Bananini', 'legendary'), ('Cocosini Mama', 'legendary'),
    ('Sigma Boy', 'legendary'), ('Sigma Girl', 'legendary'), ('Pi Pi Watermelon', 'legendary'),
    ('Chocco Bunny', 'legendary'), ('Sealo Regalo', 'legendary'),
    # Mythic
    ('Frigo Camelo', 'mythic'), ('Orangutini Ananassini', 'mythic'), ('Rhino Toasterino', 'mythic'),
    ('Bombardiro Crocodilo', 'mythic'), ('Bombombini Gusini', 'mythic'), ('Cavallo Virtuso', 'mythic'),
    ('Gorillo Watermelondrillo', 'mythic'), ('Avocadorilla', 'mythic'), ('Tob Tobi Tobi', 'mythic'),
    ('Ganganzelli Trulala', 'mythic'), ('Cachorrito Melonito', 'mythic'), ('Elefanto Frigo', 'mythic'),
    ('Toiletto Focaccino', 'mythic'), ('Te Te Te Sahur', 'mythic'),
    ('Tracoducotulu Delapeladustuz', 'mythic'), ('Lerulerulerule', 'mythic'),
    ('Jingle Jingle Sahur', 'mythic'), ('Tree Tree Tree Sahur', 'mythic'),
    ('Spioniro Golubiro', 'mythic'), ('Zibra Zubra Zibralini', 'mythic'),
    ('Tigrilini Watermelini', 'mythic'), ('Carrotini Brainini', 'mythic'), ('Bananito Bandito', 'mythic'),
    # Brainrot God
    ('Coco Elefanto', 'brainrot_god'), ('Girafa Celestre', 'brainrot_god'),
    ('Gattatino Nyanino', 'brainrot_god'), ('Chihuanini Taconini', 'brainrot_god'),
    ('Matteo', 'brainrot_god'), ('Tralalero Tralala', 'brainrot_god'),
    ('Espresso Signora', 'brainrot_god'), ('Odin Din Din Dun', 'brainrot_god'),
    ('Statutino Libertino', 'brainrot_god'), ('Trenostruzzo Turbo 3000', 'brainrot_god'),
    ('Ballerino Lololo', 'brainrot_god'), ('Los Orcalitos', 'brainrot_god'),
    ('Dug Dug Dug', 'brainrot_god'), ('Tralalita Tralala', 'brainrot_god'),
    ('Urubini Flamenguini', 'brainrot_god'), ('Los Bombinitos', 'brainrot_god'),
    ('Los Crocodillitos', 'brainrot_god'), ('Piccione Macchina', 'brainrot_god'),
    ('Trippi Troppi Troppa Trippa', 'brainrot_god'), ('Los Tungtungtungcitos', 'brainrot_god'),
    ('Tukanno Bananno', 'brainrot_god'), ('Tipi Topi Taco', 'brainrot_god'),
    ('Extinct Ballerina', 'brainrot_god'), ('Capi Taco', 'brainrot_god'),
    ('Gattito Tacoto', 'brainrot_god'), ('Pakrahmatmamat', 'brainrot_god'),
    ('Tractoro Dinosauro', 'brainrot_god'), ('Corn Corn Corn Sahur', 'brainrot_god'),
    ('Squalanana', 'brainrot_god'), ('Los Tipi Tacos', 'brainrot_god'),
    ('Bombardini Tortinii', 'brainrot_god'), ('Pop Pop Sahur', 'brainrot_god'),
    ('Ballerina Peppermintina', 'brainrot_god'), ('Yeti Claus', 'brainrot_god'),
    ('Ginger Globo', 'brainrot_god'), ('Frio Ninja', 'brainrot_god'),
    ('Ginger Cisterna', 'brainrot_god'), ('Cacasito Satalito', 'brainrot_god'),
    ('Aquanaut', 'brainrot_god'), ('Tartaruga Cisterna', 'brainrot_god'),
    ('Trigoligre Frutonni', 'brainrot_god'), ('Orcalero Orcala', 'brainrot_god'),
    ('Bulbito Bandito Traktorito', 'brainrot_god'),
    # Secret
    ('Las Sis', 'secret'), ('La Vacca Saturno Saturnita', 'secret'),
    ('Sammyini Spyderini', 'secret'), ('Extinct Tralalero', 'secret'),
    ('Extinct Matteo', 'secret'), ('Los Tralaleritos', 'secret'),
    ('La Karkerkar Combinasion', 'secret'), ('Karker Sahur', 'secret'),
    ('Las Tralaleritas', 'secret'), ('Job Job Job Sahur', 'secret'),
    ('Los Spyderrinis', 'secret'), ('Perrito Burrito', 'secret'),
    ('Graipuss Medussi', 'secret'), ('Los Jobcitos', 'secret'),
    ('La Grande Combinasion', 'secret'), ('Tacorita Bicicleta', 'secret'),
    ('Nuclearo Dinossauro', 'secret'), ('Los 67', 'secret'), ('Money Money Puggy', 'secret'),
    ('Chillin Chili', 'secret'), ('La Extinct Grande', 'secret'), ('Los Tacoritas', 'secret'),
    ('Los Tortus', 'secret'), ('Tang Tang Kelentang', 'secret'),
    ('Garama and Madundung', 'secret'), ('La Secret Combinasion', 'secret'),
    ('To To To Sahur', 'secret'), ('Las Vaquitas Saturnitas', 'secret'),
    ('Chicleteira Bicicleteira', 'secret'), ('Agarrini la Palini', 'secret'),
    ('Mariachi Corazoni', 'secret'), ('Dragon Cannelloni', 'secret'),
    ('Los Combinasionas', 'secret'), ('Los Hotspotsitos', 'secret'),
    ('La Sahur Combinasion', 'secret'), ('Quesadilla Crocodila', 'secret'),
    ('Los Matteos', 'secret'), ('Dul Dul Dul', 'secret'), ('Blackhole Goat', 'secret'),
    ('Spaghetti Tualetti', 'secret'), ('67', 'secret'), ('Los Noo My Hotspotsitos', 'secret'),
    ('Celularcini Viciosini', 'secret'), ('Tralaledon', 'secret'), ('Tictac Sahur', 'secret'),
    ('La Supreme Combinasion', 'secret'), ('Ketupat Kepat', 'secret'),
    ('Ketchuru and Musturu', 'secret'), ('Burguro and Fryuro', 'secret'),
    ('La Grande', 'secret'), ('La Vacca Prese Presente', 'secret'),
    ('Ho Ho Ho Sahur', 'secret'), ('Chicleteira Noelteira', 'secret'),
    ('Cooki and Milki', 'secret'), ('La Jolly Grande', 'secret'),
    ('Capitano Moby', 'secret'), ('Cerberus', 'secret'),
    ('Tung Tung Tung Sahur', 'secret'), ('Tortuginni Dragonfruitini', 'secret'),
    ('Pot Hotspot', 'secret'), ('Esok Sekolah', 'secret'),
    # OG
    ('Skibidi Toilet', 'og'), ('Strawberry Elephant', 'og'), ('Meowl', 'og'),
    ('Headless Horseman', 'og'), ('Developini Braziliaspidini', 'og'), ('Kings Coleslaw', 'og'),
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
