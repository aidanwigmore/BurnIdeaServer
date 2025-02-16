from django.core.management.base import BaseCommand
from customers.models import Customer
from django.contrib.auth.hashers import make_password

class Command(BaseCommand):
    help = 'Create an admin user'

    def handle(self, *args, **kwargs):
        if not Customer.objects.filter(email='admin@gmail.com').exists():
            admin_user = Customer.objects.create(
                email='admin@gmail.com',
                name='Aidan Admin',
                given_name='User',
                is_active=True,
                is_staff=True,
                is_superuser=True,
                password=make_password('aidanwigmore1')
            )
            admin_user.save()
            self.stdout.write(self.style.SUCCESS('Successfully created admin user'))
        else:
            self.stdout.write(self.style.WARNING('Admin user already exists'))