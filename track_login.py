import smtplib
import os
from datetime import datetime as dt
from email.mime.text import MIMEText


def send_trace_info():
    subject = "Trace Login Info"
    sender = "yubin.dmd@gmail.com"
    recipients = ["yubin.on.ca@gmail.com", "yubin.ustb@gmail.com"]
    password = "ccja tlox pder idfn"

    body = f"User {os.environ.get('USERNAME')} Login at {dt.now()}"

    send_email(subject, body, sender, recipients, password)


def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")


if __name__ == "__main__":
    send_trace_info()
