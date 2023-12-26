import os

from celery import Celery

# Reference: https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

app = Celery('worker') # type: ignore

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()
"""
looking for all the tasks like below:
- app1/
    - tasks.py
    - models.py
- app2/
    - tasks.py
    - models.py
"""


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
