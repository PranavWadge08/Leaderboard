from django.core.management.base import BaseCommand
from accounts.models import User


class Command(BaseCommand):
    help = 'Initialize admin user if it does not exist'

    def handle(self, *args, **kwargs):
        admin_user = User.objects.filter(is_staff=True, is_superuser=True)
        if admin_user.count() > 0:
            self.stdout.write(self.style.WARNING(f'Admin user already exists.'))
        else:
            User.objects.create_superuser(
                email="admin@admin.com", password="tulakaymahit",
                first_name="Admin", last_name="User")
            self.stdout.write(self.style.SUCCESS(f'Admin user created successfully.'))
