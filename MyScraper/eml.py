from smtplib import SMTP_SSL, SMTP_SSL_PORT

service_account = 'pos@diversey.com'
service_password = 'TjmiVu0q'
server = 'imap.gmail.com'
port = 993
to = ['alekhya.ravula@diversey.com', 'nakul.deshmukh@wipro.com']
to_str = 'alekhya.ravula@diversey.com, nakul.deshmukh@wipro.com'
body = 'hi'

headers = f"From:{service_account}\r\n"
headers += f"To:{to_str}\r\n"
headers += f"Co:{to_str}\r\n"
headers += f"Subject: Hello\r\n"

email_msg = headers + "\r\n" + body

s = SMTP_SSL(server, port=465)
s.set_debuglevel(1)
s.login(service_account, service_password)
s.sendmail(service_account,to, email_msg)

s.quit()

