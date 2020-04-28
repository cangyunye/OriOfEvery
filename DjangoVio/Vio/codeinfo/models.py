from django.db import models

# Create your models here.

class CodeInfo(models.Model):
	module = models.CharField('模块',max_length=20,null=False)
	source = models.CharField('源文件名',max_length=20,null=False)
	errcode = models.CharField('告警错误码',max_length=20,null=False)
	errattr = models.CharField('告警属性',max_length=50,null=False)
	errpara = models.CharField('告警参数',max_length=50,null=False)
	syseffect = models.CharField('系统影响',max_length=512,null=True)
	sysproc = models.TextField('系统处理过程')
	cause = models.CharField('原因',max_length=512,null=True)
	procstep = models.CharField('处理步骤', max_length=256, null=True)
	upgradedate = models.DateTimeField('更新时间',auto_now=True)
	class Meta:
		unique_together = ["module", "source","errcode"]

	def __str__(self):
		return f'CodeInfo<module = {self.module},source = {self.source},errcode = {self.errcode},' \
			   f'errattr = {self.errattr},code = {self.errpara},' \
			   f'syseffect = {self.syseffect},sysproc = {self.sysproc},cause = {self.cause},' \
			   f'procstep = {self.procstep},upgradedate = {self.upgradedate}'

class CodeInfoSpe(models.Model):
	module = models.CharField('模块',max_length=20,null=False)
	codefile = models.CharField('源文件名',max_length=20,null=False)
	code = models.CharField('信息码',max_length=40,null=False)
	upgradedate = models.DateTimeField('更新时间',auto_now=True)
	# upload = models.FileField(upload_to="")
	class Meta:
		unique_together = ["module", "codefile","code"]

	def __str__(self):
		return f'CodeInfo<module = {self.module},codefile = {self.codefile},code = {self.code}'
"""
上传代码文件
class SourceFile(models.Model):
	code = models.ForeignKey(Question,on_delete=models.CASCADE)
	upload = models.FileField(upload_to="")
"""


class CodeDetail(models.Model):
	code = models.ForeignKey(CodeInfoSpe,on_delete=models.CASCADE,default='')
	codesummary = models.CharField('信息码描述',max_length=256,null=True)
	codeclip = models.CharField('代码片段',max_length=512,null=True)
	docinfo = models.CharField('需求名称', max_length=128, null=True)
	def __str__(self):
		return f'CodeDetail<codesummary = {self.codesummary},codeclip = {self.codeclip},docinfo = {self.docinfo}>'

class CodeStrategy(models.Model):
	code = models.ForeignKey(CodeInfoSpe,on_delete=models.CASCADE,default='')
	solution = models.CharField('解决方案',max_length=256,null=True)
	def __str__(self):
		return f'CodeStrategy<solution = {self.solution}>'