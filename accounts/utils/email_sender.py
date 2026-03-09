from django.core.mail import send_mail
from django.core.mail.backends.smtp import EmailBackend
from accounts.models import EmailSettings


def send_dynamic_email(subject, message, to_email):

    config = EmailSettings.objects.first()

    connection = EmailBackend(
        host=config.email_host,
        port=config.email_port,
        username=config.email_host_user,
        password=config.email_host_password,
        use_tls=config.use_tls
    )

    send_mail(
    subject,
    message,
    config.email_host_user,
    [to_email],
    connection=connection,
    fail_silently=False
)