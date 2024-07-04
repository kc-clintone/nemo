#!/usr/bin/python3
"""
Alerting system module
"""

import smtplib
from email.mime.text import MIMEText


def send_alert(email, subject, message, smtp_server='smtp.example.com', smtp_port=587, smtp_user='your_email@example.com', smtp_password='your_password'):
    """
    Alerting system
    """
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = smtp_user
    msg['To'] = email

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.sendmail(msg['From'], [msg['To']], msg.as_string())
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False

