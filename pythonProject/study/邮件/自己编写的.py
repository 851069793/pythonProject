import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender = "z1013@vip.qq.com"
my_user = "z1013@vip.qq.com"
password = "awsahqidvxerbbha"

msg = MIMEText("邮件内容","plain","utf-8")
msg['from']=formataddr(["发送人名字",my_sender])
msg['to']=formataddr(["收件人名字",my_user])
msg['subject']="标题"

server = smtplib.SMTP_SSL("smtp.qq.com", 465)
server.login(my_sender,password)
server.sendmail(my_sender,my_user,msg.as_string())
server.quit()