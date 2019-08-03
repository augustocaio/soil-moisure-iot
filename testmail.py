import smtplib, ssl, html_builder
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def attach_images(message):
  with open('./wet-plant.png', 'rb') as f:
    # set attachment mime and file name, the image type is png
    mime = MIMEBase('image', 'png', filename='img1.png')
    # add required header data:
    mime.add_header('Content-Disposition', 'attachment', filename='img1.png')
    mime.add_header('X-Attachment-Id', '0')
    mime.add_header('Content-ID', '<0>')
    # read attachment file content into the MIMEBase object
    mime.set_payload(f.read())
    # encode with base64
    encoders.encode_base64(mime)
    # add MIMEBase object to MIMEMultipart object
    message.attach(mime)

  with open('./dry-plant.png', 'rb') as f:
      # set attachment mime and file name, the image type is png
      mime = MIMEBase('image', 'png', filename='img2.png')
      # add required header data:
      mime.add_header('Content-Disposition', 'attachment', filename='img2.png')
      mime.add_header('X-Attachment-Id', '1')
      mime.add_header('Content-ID', '<1>')
      # read attachment file content into the MIMEBase object
      mime.set_payload(f.read())
      # encode with base64
      encoders.encode_base64(mime)
      # add MIMEBase object to MIMEMultipart object
      message.attach(mime)
  return message

def send_email(message):

  sender_email = "toshidev123@gmail.com"
  receiver_email = "leonardotkimura@gmail.com"
  password = "ampdtbaf"

  message["Subject"] = "multipart test"
  message["From"] = sender_email
  message["To"] = receiver_email

  context = ssl.create_default_context()
  with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
      server.login(sender_email, password)
      server.sendmail(
          sender_email, receiver_email, message.as_string()
      )

html = html_builder.build([1,1,0])


message = MIMEMultipart("alternative")


message = attach_images(message)

html_part = MIMEText(html, "html")
message.attach(html_part)

send_email(message)
print(" \n Sent!")


