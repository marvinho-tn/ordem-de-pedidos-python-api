import smtplib
from email.message import EmailMessage

from infra.config.env import settings

def send_email(to: str, subject: str, message: str):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = "marvinthomaz@gmail.com"
    msg['To'] = to
    msg.set_content(message)

    # Conexão com servidor SMTP do Gmail
    s = smtplib.SMTP(settings.smtp_host, int(settings.smtp_port))
    s.send_message(msg)
    s.quit()
