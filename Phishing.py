import sys
import create_attachment
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

mail_sender_address = "labcyber523@gmail.com"
application_key = "avowmnjsepifvwhi"
smtp_server = "smtp.gmail.com"
smtp_port = 465

"""
creates the mail and sends the mail.
"""

def function(array):
    username = sys.argv[1]
    mail_service_name = sys.argv[2]
    title = sys.argv[3]
    job_title = sys.argv[4]
    personal_status = sys.argv[5]
    kids = sys.argv[6]
    mail_receiver_address = username + "@" + mail_service_name

    fp = open("scam.html", "r")
    html = fp.read()
    html = html.replace("user", username)
    fp.close()

    message = MIMEMultipart("alternative")
    message["Subject"] = "Important Information about your steam account"
    message["From"] = mail_sender_address
    message["To"] = mail_receiver_address

    html_message = MIMEText(html, "html")

    message.attach(html_message)
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", smtp_port, context=context) as server:
        server.login(mail_sender_address, application_key)
        server.sendmail(mail_sender_address, mail_receiver_address, message.as_string())


if __name__ == "__main__":
    function(sys.argv)
