#!/usr/bin/python3
#-*- coding : utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import parseaddr, formataddr
import traceback

class MailSession():
	def __init__(self,my_sender,my_password,emailhost):
		self.sender=my_sender
		self.password=my_password
		self.emailhost=emailhost


	def __enter__(self):
		self.server = self.login()
		return self.server

	def __exit__(self, exc_type, exc_val, exc_tb):
		self.close()

	def login(self):
		try:
			#找到你的发送邮箱的服务器地址，已加密的形式发送
			server = smtplib.SMTP_SSL(self.emailhost, 465)  # 发件人邮箱中的SMTP服务器
			# server = smtplib.SMTP(self.emailhost, 25)
			server.ehlo()
			#登录你的账号
			server.login(self.sender, self.password)  # 括号中对应的是发件人邮箱账号、邮箱密码
			return server
		except Exception :
			print(traceback.print_exc())
			print("连接失败")


	def close(self):
		print("处理完毕。")
		self.server.quit()


class MailCreater():
	def _format_addr(self,s):
		name, addr = parseaddr(s)
		return formataddr((Header(name, 'utf-8').encode(), addr))

	def create_email(self,email_from, email_to, email_Subject, email_text, annex_path, annex_name):
		# 输入发件人昵称、收件人昵称、主题，正文，附件地址,附件名称生成一封邮件
		# 生成一个空的带附件的邮件实例
		message = MIMEMultipart()
		# 将正文以text的形式插入邮件中
		message.attach(MIMEText(email_text, 'plain', 'utf-8'))
		# 生成发件人名称（这个跟发送的邮件没有关系）
		message['From'] =  self._format_addr(email_from)
		# 生成收件人名称（这个跟接收的邮件也没有关系）
		message['To'] =  self._format_addr(email_to)
		# 生成邮件主题
		message['Subject'] = Header(email_Subject, 'utf-8')
		# 读取附件的内容
		att1 = MIMEText(open(annex_path, 'rb').read(), 'base64', 'utf-8')
		att1["Content-Type"] = 'application/octet-stream'
		# 生成附件的名称
		att1["Content-Disposition"] = 'attachment; filename=' + annex_name
		# 将附件内容插入邮件中
		message.attach(att1)
		# 返回邮件
		return message


def main():
	my_email_from = 'fei frommail@163.com'
	my_email_to = 'yue tomail@gmail.com'
	# 邮件标题
	my_email_Subject = '啊哈？怎么回事'
	# 邮件正文
	resultinfo = '将测试输出用日志记录到文件中'
	my_email_text = "你希望将单元测试的输出写到到某个文件中去，而不是打印到标准输出。运行单元测试一个常见技术就是在测试文件底部加入下面这段代码片段" + resultinfo
	# 附件地址
	file_path = 'C:\\Users\\Administrator\\Desktop\\ff.txt'
	my_annex_path = file_path
	# 附件名称
	my_file_name = 'examplefile '
	my_annex_name = my_file_name
	# 邮件实例
	my_sender = 'example@163.com'
	my_password = 'mypass'
	my_receiver = ['commonexample@gmail.com','monster@163.com']#接收人邮箱列表
	smtp_server = "smtp.163.com"

	# 创建批量发送邮件会话
	with MailSession(my_sender,my_password,smtp_server) as ms:
		mc = MailCreater()
		# 创建邮件内容生成
		msg = mc.create_email(my_email_from, my_email_to, my_email_Subject,
					  my_email_text, my_annex_path, my_annex_name)
		# 发送邮件
		ms.sendmail(my_sender, my_receiver, msg.as_string())

if __name__ == '__main__':
	main()