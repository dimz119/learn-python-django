import os
from celery import Celery
from celery.schedules import crontab
from datetime import timedelta

# Reference: https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

app = Celery('worker') # type: ignore

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.update(
    task_routes = {
        'worker.tasks.dumb': {
            'queue': 'celery'
        },
        'worker.tasks.add': {
            'queue': 'celery'
        }
    },
)

# Rate limiting
app.conf.task_default_rate_limit = '5/m'  # 5 tasks per minute

# Redis specific
# https://docs.celeryq.dev/en/stable/userguide/routing.html#redis-message-priorities
app.conf.broker_transport_options = {
    'priority_steps': list(range(10)), # default is 4
    # 'sep': ':',
    'queue_order_strategy': 'priority',
}
"""
['celery', 'celery:1', 'celery:2', 'celery:3', 'celery:4', 'celery:5', 'celery:6', 'celery:7', 'celery:8', 'celery:9']
"""

# app.conf.task_routes = {
#     'worker.tasks.dumb': {
#         'queue': 'queue1'
#     },
#     'worker.tasks.add': {
#         'queue': 'queue2'
#     }
# }

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

# # Periodic task & Cron Table
# app.conf.beat_schedule = {
#     'add-every-5-seconds': {
#         'task': 'worker.tasks.add',
#         'schedule': timedelta(seconds=5),
#         'args': (10, 10),
#         # 'kwargs': {"key": "value"},
#         # 'options': {
#         #     'queue': 'celery'
#         # }
#     },
#     'add-every-minute': {
#         'task': 'worker.tasks.add',
#         'schedule': crontab(minute='*'),
#         'args': (20, 20)
#     },
# }

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
