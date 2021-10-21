import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#
class MAILER:
    def __init__(self,email_bot:str,password_bot:str,to_email:str,title:str,msg:str) -> None:
        self.BOT_EMAIL = email_bot
        self.BOT_PASSWORD = password_bot
        self.TO_EMAIL = to_email
        self.TITLE = title
        self.MSG = msg
    def send(self):
        msg = MIMEMultipart()
        msg['From'] = self.BOT_EMAIL
        msg['To'] = self.TO_EMAIL
        msg['Subject'] = self.TITLE
        msg.attach(MIMEText(self.MSG, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.BOT_EMAIL, self.BOT_PASSWORD)
        text = msg.as_string()
        server.sendmail(self.BOT_PASSWORD, self.TO_EMAIL, text)
        server.quit()
