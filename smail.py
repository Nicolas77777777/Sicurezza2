import smtplib
from email.mime.multipart import MIMEMultipart

from email.mime.text import MIMEText

def send_email(sender_email,receiver_email, subject, body, password):
    
        # Set up the SMTP server
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    # Create the email

    msg = MIMEMultipart()
    msg['From'] = 'sairwate@gmail.com'
    msg['To'] = 'francorcr@hotmail.it'
    msg['Subject'] = 'lavoro'
    msg.attach(MIMEText(body, 'plain'))

try:

# Connect to the server and send the email
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls() # Secure the connection
    server.login('sairwater@gmail.com', 'Januspater2019!')
    text = msg.as_string()
    server.sendmail('sairwater@gmail.com', 'francorcr@hotmail.it', text)
    server.quit()
    print("Email sent successfully!") 

except Exception as e:
    print(f"Failed to send email. Error: {e}")
    # Example usage
    sender_email = "sairwater@gmail.com"
    receiver_email = "francorcr@hotmail.it"
    subject = "Test Email"
    body = "This is a test email sent from Python."
    password = "Januspater2019!"


send_email(sender_email, receiver_email,subject, body, password)
