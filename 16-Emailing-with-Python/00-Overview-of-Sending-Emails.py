import smtplib
import getpass

smtp_object = smtplib.SMTP('smtp.gmail.com', 587)

smtp_ehlo = smtp_object.ehlo()
print(smtp_ehlo)

smtp_start_tls = smtp_object.starttls()
print(smtp_start_tls)

result = getpass.getpass("Type something here and it will be hidden: ")
print(result)