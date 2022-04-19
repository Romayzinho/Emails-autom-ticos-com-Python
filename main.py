# Feito por Romay
# 🐦: @romayzinho
# https://github.com/Romayzinho/Emails-autom-ticos-com-Python/new/main
import os 
import smtplib
from email.message import EmailMessage
from secret import password
 
EMAIL_ADRESS = 'seugmail@gmail.com'
EMAIL_PASSWORD = password


msg = EmailMessage()
msg['Subject'] = 'Título do E-mail'
msg['From'] = 'seuemail@gmail.com'
msg['To'] = 'destinário@gmail.com'
msg.set_content('Conteúdo do Email!')


with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(EMAIL_ADRESS,EMAIL_PASSWORD)
    smtp.send_message(msg)
    
    
