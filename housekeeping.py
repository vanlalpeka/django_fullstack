# housekeeping.py is a script that performs housekeeping tasks.
# Cron job example:
# 0 3 * * * python manage.py shell -c "from housekeeping import run_housekeeping; run_housekeeping()" 
# (runs at 3:00 AM daily)


import os
from datetime import timedelta, timezone
from django.core.management import call_command
import subprocess
from django.conf import settings
import logging.handlers
from app.models import *

# Remove expired sessions
def clean_expired_sessions():
    call_command('clearsessions')
    print("Cleaned expired sessions.")

# # models with timestamps, remove old or inactive data
# def clean_stale_data():
#     cutoff_time = timezone.now() - timedelta(days=30)
#     MyModel.objects.filter(last_updated__lt=cutoff_time).delete()
#     print("Cleaned stale data.")

# Collect Static Files 
def collect_static_files():
    call_command('collectstatic', '--noinput')
    print("Collected static files.")

# Backup the database
# read the credentials from settings.py
# This is a logical backup.
# Logical backup is more portable than a physical backup.
def backup_database():
    backup_dir = settings.BASE_DIR / 'backups'
    os.makedirs(backup_dir, exist_ok=True)
    backup_file = backup_dir / f"db_backup_{timezone.now().strftime('%Y%m%d_%H%M%S')}.sql"
    try:
        subprocess.run(
            ["pg_dump", "-U", settings.DATABASES['default']['USER'], 
             "-d", settings.DATABASES['default']['NAME'], 
             "-h", settings.DATABASES['default']['HOST'], 
             "-p", settings.DATABASES['default']['POST'], 
             "-F", "p", # Plain text format
            #  "-F", "c",  # Custom format
             "-f", str(backup_file)],
            check=True
        )
        print(f"Database backup created: {backup_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error creating database backup: {e}")

# Rotate logs
def rotate_logs():
    logger = logging.getLogger()
    for handler in logger.handlers:
        if isinstance(handler, logging.handlers.RotatingFileHandler):
            handler.doRollover()
    print("Rotated logs.")

def run_housekeeping():
    clean_expired_sessions()
    # clean_stale_data()
    collect_static_files()
    backup_database()
    rotate_logs()

if __name__ == "__main__":
    run_housekeeping()