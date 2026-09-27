from celery import Celery
import os

broker = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
backend = os.getenv('CELERY_RESULT_BACKEND', broker)

celery = Celery('backend', broker=broker, backend=backend)

# Load celery config from environment or module
celery.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
)

# Autodiscover tasks
celery.autodiscover_tasks(['backend.tasks'])
