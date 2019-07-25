# https://myaccount.google.com/lesssecureapps?pli=1 linki Açık yap

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

mesaj = MIMEMultipart()

mesaj["From"] = "durmusyasar13@gmail.com"

mesaj["To"] = "durmusyasar13@gmail.com"

mesaj["Subject"] = "Smtp Mail Gönderme"


yazi = """

Smtp ile mail gönderiyorum.

Durmuş YAŞAR


"""


mesaj_govdesi = MIMEText(yazi,"plain")

mesaj.attach(mesaj_govdesi)

try:
    mail = smtplib.SMTP("smtp.gmail.com",587)

    mail.ehlo()

    mail.starttls()

    mail.login("","")

    mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())

    print("Mail Başarıyla Gönderildi....")

    mail.close()

except:
    sys.stderr.write("Bir sorun oluştu!")
    sys.stderr.flush()
