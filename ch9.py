import smtplib 
from email.mime.text import MIMEText
msg =MIMEText("A journey of a thousand miles begins with one")
msg['Subject']="an email alert"
msg['From']='kyaloobama@gmail.com'
msg['To']='kyalomwele@gmail.com'
s=smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()
'''Don't use "email" in your .py file name or even in package name as well.
 This will cause confusion to the interpreter between user declared module and pre-defined modules'''