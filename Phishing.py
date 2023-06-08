import sys
import create_attachment
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

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
    mail_sender_address = "labcyber523@gmail.com"
    application_key = "avowmnjsepifvwhi"
    mail_receiver_address = username + "@" + mail_service_name

    fp = open("scam.html", "r")
    content = fp.read()
    content.replace("user", username)
    fp.close()

    #create_attachment()
    port = 465  # For SSL
    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(mail_sender_address, application_key)
        server.sendmail(mail_sender_address, mail_receiver_address, content)



if __name__ == "__main__":
    function(sys.argv)
