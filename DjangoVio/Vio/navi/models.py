from django.db import models


class msgboard(models.Model):
	visitor = models.CharField('拜访者',max_length=50,null=True)
	msgdate = models.DateTimeField('发表时间',auto_now=True)
	email = models.EmailField('邮箱',null=True)
	message = models.TextField('留言',null=False)

	def __str__(self):
		return f'msgboard<visitor = {self.visitor},msgdate = {self.msgdate},email = {self.email}\n {self.message}'