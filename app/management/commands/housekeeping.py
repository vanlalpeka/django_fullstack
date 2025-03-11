# housekeeping.py is a script that performs housekeeping tasks.
# Cron job example:
# 0 3 * * * python manage.py housekeeping
# (runs at 3:00 AM daily)


import os
import django
import subprocess
import logging.handlers
from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.conf import settings
from datetime import datetime, timedelta, timezone
from app.models import *

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
# django.setup()

class Command(BaseCommand):
    help = 'Run housekeeping tasks'

    def handle(self, *args, **options):
        # Remove expired sessions
        call_command('clearsessions')
        print("Cleaned expired sessions.")

# # models with timestamps, remove old or inactive data
#     cutoff_time = timezone.now() - timedelta(days=30)
#     MyModel.objects.filter(last_updated__lt=cutoff_time).delete()
#     print("Cleaned stale data.")

        # Collect Static Files 
        call_command('collectstatic', '--noinput')
        print("Collected static files.")

        # Backup the database
        # read the credentials from settings.py
        # This is a logical backup.
        # Logical backup is more portable than a physical backup.
        backup_dir = settings.BASE_DIR / 'backups'
        os.makedirs(backup_dir, exist_ok=True)
        backup_file = backup_dir / f"db_backup_{timezone.now().strftime('%Y%m%d_%H%M%S')}.sql"
        try:
            subprocess.run(
                ["pg_dump", "-U", settings.DATABASES['default']['USER'], 
                "-d", settings.DATABASES['default']['NAME'], 
                "-h", settings.DATABASES['default']['HOST'], 
                "-p", settings.DATABASES['default']['PORT'], 
                "-F", "p", # Plain text format
                #  "-F", "c",  # Custom format
                "-f", str(backup_file)],
                check=True
            )
            print(f"Database backup created: {backup_file}")
        except subprocess.CalledProcessError as e:
            print(f"Error creating database backup: {e}")

        # Rotate logs
        logger = logging.getLogger()
        for handler in logger.handlers:
            if isinstance(handler, logging.handlers.RotatingFileHandler):
                handler.doRollover()
        print("Rotated logs.")
