# This is a Django management command that deletes all chat messages from the Message model.
from django.core.management.base import BaseCommand
from room.models import Message 

class Command(BaseCommand):
    help = 'Deletes all chat messages'

    def handle(self, *args, **options):
        try:
            Message.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('All chat messages deleted successfully.'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'An error occurred: {str(e)}'))