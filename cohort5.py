import smtplib
import ssl
from email.message import EmailMessage

name = input("Please Enter Name Here: ")
sender = input("Enter your eMail address: ")
my_password = input("Enter your eMail Password: ")
recipients_eMail_input = input("Enter Recipients emails addresses: ")
recipients_eMail_add = recipients_eMail_input.split(',')

subject = input("Your eMail Subject?: ")
body = input('Enter the body of the mail: ') 

mail_msg = EmailMessage()

mail_msg['subject'] = subject
mail_msg['From'] = sender
mail_msg['To'] = ','.join(recipients_eMail_add)
mail_msg.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as mysmtp:
    mysmtp.login(sender, my_password,)
    mysmtp.sendmail(sender,recipients_eMail_add, mail_msg.as_string())
if mail_msg:
    print('Message Sent')
else:
    print('Error Sending Message')
mysmtp.close()