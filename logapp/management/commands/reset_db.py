import os
from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    help = 'Reset the database'

    def handle(self, *args, **kwargs):
        db_name = settings.DATABASES['default']['NAME']
        os.system(f'echo "DROP DATABASE {db_name}; CREATE DATABASE {db_name};" | psql -h {settings.DATABASES["default"]["HOST"]} -U {settings.DATABASES["default"]["USER"]}')
        self.stdout.write(self.style.SUCCESS('Database reset successfully'))
