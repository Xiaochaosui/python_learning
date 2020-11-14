# 发邮件的库
import smtplib
#  邮件文本
from email.mime.text import MIMEText

# SMTP服务器
SMTPSever = "smtp.163.com"

# 发邮件的地址
sender = "xiaochaosui@163.com"
# 发送者邮箱的密码
passwd = "123456a"

# 设置发生的内容
message = "xcs is a good man"
# 转换成邮件文本
msg = MIMEText(message)
# 标题
msg["Subject"] = "来自牛牛问候"
# 邮件接收者
msg["From"] = sender

print(msg)
# 创建SMTP服务器
mailSever = smtplib.SMTP(SMTPSever,25)
# 登录邮箱
mailSever.login(sender,passwd)
# 发送邮件
for i in range(100):
    mailSever.sendmail(sender, ["xiaochaosui@163.com"], msg.as_string())
    i += 1
# 退出邮箱
mailSever.quit()