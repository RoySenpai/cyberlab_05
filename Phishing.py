import sys
import create_attachment
import smtplib, ssl

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

    # load mail cotent + insert the username + insert attachment

    #fp = open("scam.html", "r")
    #content = fp.read()

    #content.replace("user", username)

    #create_attachment()
    port = 465  # For SSL
    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("labcyber523@gmail.com", "avowmnjsepifvwhi")
        server.sendmail("labcyber523@gmail.com", "lidorky22@gmail.com", "hello")



if __name__ == "__main__":
    function(sys.argv)
