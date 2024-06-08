import smtplib
import schedule
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email configuration
SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
SMTP_PORT = 587  # Replace with your SMTP port (usually 587 for TLS)
EMAIL_ADDRESS = 'example@email'  # Replace with your email address
EMAIL_PASSWORD = 'examplepasword'  # Replace with your email password
RECIPIENT_ADDRESS = 'example@email'  # Replace with recipient's email address


def send_email_report():
    # Create the email
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = RECIPIENT_ADDRESS
    msg['Subject'] = 'Daily Report'

    # Email body content
    body = 'This is your report'
    msg.attach(MIMEText(body, 'plain'))

    # Connect to the server and send the email
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        text = msg.as_string()
        server.sendmail(EMAIL_ADDRESS, RECIPIENT_ADDRESS, text)
        server.quit()
        print('Email sent successfully!')
    except Exception as e:
        print(f'Failed to send email: {e}')


# Schedule the email to be sent daily at a specific time
schedule.every().day.at("14:32").do(send_email_report)  # Set your preferred time

print('Scheduling daily email reports...')

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(60)
