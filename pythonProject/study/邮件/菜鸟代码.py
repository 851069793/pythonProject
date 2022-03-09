import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from time import sleep

my_sender = 'z1013@vip.qq.com'  # 发件人邮箱账号
my_pass = 'awsahqidvxerbbha'  # 发件人邮箱密码
my_user = '2956223746@qq.com'  # 收件人邮箱账号，我这边发送给自己
my_user2 = "1652799286@qq.com"


def mail():
    ret = True
    try:
        msg = MIMEText('这是第一封骚扰邮件', 'plain', 'utf-8')
        msg['From'] = formataddr(["老父亲", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["乖儿子", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "骚扰邮件"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user,my_user2 ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret

while True:
    ret = mail()
    if ret:
        print("邮件发送成功")
    else:
        print("邮件发送失败")
    sleep(10)

