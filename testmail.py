import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()
#Next, log in to the server
server.login("toshidev123", "ampdtbaf")

#Send the mail
msg = "\nHello!" # The \n separates the message from the headers
server.sendmail("toshidev123@gmail.com", "leonardotkimura@gmail.com", msg)
print(" \n Sent!")
mailServer.quit()   