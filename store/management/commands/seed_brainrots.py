from django.core.management.base import BaseCommand
from store.models import Brainrot, BRAINROT_LIST

class Command(BaseCommand):
    help = 'Seed brainrot characters'

    def handle(self, *args, **options):
        created = 0
        for name, rarity in BRAINROT_LIST:
            obj, was_created = Brainrot.objects.get_or_create(name=name, defaults={'rarity': rarity})
            if was_created:
                created += 1
        self.stdout.write(self.style.SUCCESS(f'✅ Created {created} brainrots'))
