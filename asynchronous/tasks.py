from celery import shared_task
from celery.utils.log import get_task_logger
from .emails import send_feedback_email

logger = get_task_logger(__name__)


# This is the decorator which a celery worker uses
@shared_task(name="send_feedback_email_task")
def send_feedback_email_task(name, email, message):
    logger.info("Sent email")
    return send_feedback_email(name, email, message)
