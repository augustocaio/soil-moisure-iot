import smtplib, ssl, html_builder
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def attach_images(path, id, message):
  xid = str(id)
  cid = '<' + str(id) + '>'
  with open(path, 'rb') as f:
    mime = MIMEBase('image', 'png', filename='img1.png')
    mime.add_header('Content-Disposition', 'attachment', filename='img1.png')
    mime.add_header('X-Attachment-Id', xid)
    mime.add_header('Content-ID', cid)
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    message.attach(mime)
  return message

def send_email(message):
  sender_email = "toshidev123@gmail.com"
  receiver_email = "leonardotkimura@gmail.com"
  password = "ampdtbaf"

  message["Subject"] = "Relatório Plantinhas IoT"
  message["From"] = sender_email
  message["To"] = receiver_email

  context = ssl.create_default_context()
  with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
      server.login(sender_email, password)
      server.sendmail(
          sender_email, receiver_email, message.as_string()
      )


message = MIMEMultipart("alternative")
message = attach_images('./images/wet-plant.png', 0 ,message)
message = attach_images('./images/dry-plant.png', 1 ,message)

html = html_builder.build([1,0,0])
html_part = MIMEText(html, "html")
message.attach(html_part)

send_email(message)
print(" \n Sent!")


