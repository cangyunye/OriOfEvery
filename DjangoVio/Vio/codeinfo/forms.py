from django import forms
class codeinfo(forms.Form):
    module = forms.CharField(label='模块', max_length=20, null=False, primary_key=True)
    codefile = forms.CharField(label='源文件名', max_length=20, null=False, primary_key=True)
    code = forms.CharField(label='信息码', max_length=40, null=False, primary_key=True)
    codeinfo = forms.CharField(label='信息码描述', max_length=256, null=True)
    solution = forms.CharField(label='解决方案', max_length=256, null=True)
    codeclip = forms.CharField(label='代码片段', max_length=512, null=True)
    docinfo = forms.CharField(label='需求名称', max_length=128, null=True)
    upgradedate = forms.DateTimeField(label='更新时间', auto_now=True)
