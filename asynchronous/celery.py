import os
from celery import Celery
from celery.schedules import crontab
from celery.utils.log import get_task_logger

from django.conf import settings
from asynchronous.emails import send_feedback_email
logger = get_task_logger(__name__)


# Setting the Default Django settings module


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'asynchronous.settings')
app = Celery('asynchronous')

# Using a String here means the worker will always find the configuration information
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


# The decorator is used for recognizing a periodic task
# If you do not like this type of periodic task setting then you old settings
@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Sending the email every 50 Seconds
    sender.add_periodic_task(50.0, send_feedback_email_task.s('Vubon', 'vubon.roy@gmail.com', 'Hello'),
                             name='add every 10')
    # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task(
        crontab(hour=7, minute=30, day_of_week=1),
        send_feedback_email_task.s('Vubon', 'vubon.roy@gmail.com', 'Hello'), )


# The task to be processed by the worker
@app.task
def send_feedback_email_task(name, email, message):
    send_feedback_email(name, email, message)
    logger.info("Sent email")
