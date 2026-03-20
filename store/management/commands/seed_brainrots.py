from django.core.management.base import BaseCommand
from store.models import Brainrot, BRAINROT_LIST
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Seed brainrots and create default users'

    def handle(self, *args, **options):
        # Seed brainrots
        created = 0
        for name, rarity in BRAINROT_LIST:
            obj, was_created = Brainrot.objects.get_or_create(name=name, defaults={'rarity': rarity})
            if was_created:
                created += 1
        self.stdout.write(self.style.SUCCESS(f'✅ Brainrots: {created} created'))

        # Create superuser Miras
        if not User.objects.filter(username='Miras').exists():
            superuser = User.objects.create_superuser('Miras', '', '202025')
            superuser.profile.nickname = 'Miras'
            superuser.profile.status = 'creator'
            superuser.profile.save()
            self.stdout.write(self.style.SUCCESS('✅ Superuser Miras created'))
        else:
            # Make sure status is creator
            u = User.objects.get(username='Miras')
            u.profile.status = 'creator'
            u.profile.nickname = 'Miras'
            u.profile.save()
            self.stdout.write('ℹ️ Superuser Miras already exists')

        # Create regular user BaconBro2395
        if not User.objects.filter(username='BaconBro2395').exists():
            user = User.objects.create_user('BaconBro2395', '', '202025')
            user.profile.nickname = 'Miras'
            user.profile.status = 'creator'
            user.profile.save()
            self.stdout.write(self.style.SUCCESS('✅ User BaconBro2395 created'))
        else:
            u = User.objects.get(username='BaconBro2395')
            u.profile.nickname = 'Miras'
            u.profile.status = 'creator'
            u.profile.save()
            self.stdout.write('ℹ️ User BaconBro2395 already exists')
