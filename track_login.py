import smtplib
import os
import time
from datetime import datetime as dt
from email.mime.text import MIMEText

log_file = os.path.join(os.path.expanduser('~'), '.trace_log.bin')


def read_track():
    if not os.path.exists(log_file):
        reset_track_file('w')

    with open(log_file, 'rt') as f:
        return f.read()


def reset_track_file(mode='a'):
    with open(log_file, f'{mode}t') as f:
        f.write(f"User {os.environ.get('USERNAME')} online at {dt.now()}\n")
        print(f"track info reset('{mode}') at:{dt.now()}")


def refresh_screen_time(mode='a'):
    while True:
        reset_track_file(mode)
        time.sleep(60)


def send_track_info():
    log = ''
    subject = "Trace Login Info"
    sender = "yubin.dmd@gmail.com"
    recipients = ["yubin.on.ca@gmail.com", "yubin.ustb@gmail.com"]
    password = "ccja tlox pder idfn"

    trace_info = f"{'-'*10}trace info{'-'*10}\n{read_track()}"
    login_info =f"User {os.environ.get('USERNAME')} Login at {dt.now()}"
    body = f"{login_info}\n{trace_info}"

    send_email(subject, body, sender, recipients, password)

    reset_track_file('w')


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
    send_track_info()
    time.sleep(30)
    refresh_screen_time()

