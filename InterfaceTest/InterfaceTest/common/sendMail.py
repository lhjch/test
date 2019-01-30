import smtplib
from email.mime.text import MIMEText
import readConfig
import os

rc = readConfig.readConfig()
host = rc.get_email("mail_host")
username = rc.get_email("mail_user")
password = rc.get_email("mail_pass")
receive = rc.get_email("receive")
sender = rc.get_email("sender")

#获取项目路径
prodir = readConfig.proDir
reportDir = os.path.join(prodir,"result\\report\\report.html")

class sendMail:
    def __init__(self):
        self.smtp = smtplib.SMTP()
        # 连接邮箱服务器
        self.smtp.connect(host)
        # 登录
        self.smtp.login(username, password)

    #发送文本
    def sendText(self):
        #配置邮件
        content = "hello word"
        text = MIMEText(content,"plain","utf-8")
        text["Subject"] = "自动化测试报告"
        text["From"] = sender
        text["To"] = receive
        self.smtp.sendmail(sender,receive,text.as_string())

    #发送附件
    def sendReport(self):
        #配置邮件
        sendfile = open(reportDir,"rb").read()
        attachfile = MIMEText(sendfile,"base64","utf-8")

        attachfile["Subject"] = "自动化测试报告"
        attachfile["From"] = sender
        attachfile["To"] = receive

        attachfile["Content-Type"] = "application/octet-stream"
        attachfile["Content-Disposition"] = "attachment; filename='111.html'"

        self.smtp.sendmail(sender,receive,attachfile.as_string())


if __name__ == "__main__":
    sendermail = sendMail()
    #sendermail.send()
    sendermail.sendReport()
