from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.decorators import periodic_task


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bluerun.settings')

app = Celery('bluerun')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings')
from celery.schedules import crontab

app.conf.beat_schedule = {
    'send-report-every-single-minute': {
        'task': 'celery.bluerun.tasks.debug_task',
        'schedule': crontab(minute=1),
    },
}
# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

