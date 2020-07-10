import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now > self.pub_date >= now - datetime.timedelta(days=1)
    # 依据pub_date做排序
    was_published_recently.admin_order_field = 'pub_date'
    # 使用图标表示True/False
    was_published_recently.boolean = True
    # 展示字段名称
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class OverTimeWork(models.Model):
    name = models.CharField('员工', max_length=20, null=False)
    jobid = models.CharField('工号', max_length=20, null=False)
    corporate_firm = models.CharField('合作公司', max_length=20, null=False)
    group_leader = models.CharField('组长', max_length=20, null=False)
    project_team = models.CharField('项目组', max_length=20, null=False)
    project_manager = models.CharField('PM', max_length=20, null=False)
    reason = models.CharField('原因', max_length=128, null=False)
    begindate = models.CharField('开始时间',max_length=24, null=False)
    enddate = models.CharField('结束时间',max_length=24, null=False)
    msgdate = models.CharField('更新时间',max_length=24, null=False)


    def __str__(self):
        return f'OverTimeWork<name = {self.name},jobid = {self.jobid},corporate_firm = {self.corporate_firm},group_leader = {self.group_leader},project_team = {self.project_team},	project_manager = {self.project_manager},reason = {self.reason},begindate = {self.begindate},enddate ={self.enddate}>'
