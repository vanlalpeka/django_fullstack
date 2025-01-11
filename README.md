This is a Django app to manage notes.


Primary features:
1. Login with socials
2. Invite only registration
3. Bulk import-export records from Admin screens
4. Automated tests using pytest 


Housekeeping tasks:
1. pg_dump -Fc --username=user --dbname=dbname --clean --file=/path/to/backup-`date +%Y-%m-%d-%H-%M-%S`.sql
2. python manage.py clearsessions


sudo fuser -k 8000/tcp

sudo systemctl restart postgresql