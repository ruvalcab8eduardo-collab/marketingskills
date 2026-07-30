from celery import shared_task

@shared_task
def run_deadline_reminders_task():
    """Task wrapper around NotificationService.generate_deadline_reminders
    Ejecuta la generación de recordatorios. Importa de forma perezosa para evitar ciclos.
    """
    try:
        from services.notification_service import NotificationService
        from core.database import SessionLocal
        db = SessionLocal()
        try:
            NotificationService.generate_deadline_reminders(db)
        finally:
            db.close()
    except Exception as e:
        # Logging: si tienes logger, úsalo; aquí usamos print por simplicidad
        print("Error ejecutando task run_deadline_reminders_task:", e)
        raise
