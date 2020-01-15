# 导入配置文件
from .config import *
from dataclasses import dataclass
import paramiko
from csv import DictReader
from openpyxl import load_workbook
from pathlib import PurePath
from time import strptime, mktime
from datetime import datetime
import re

# 版本更新
# VERSION=1
# def updateconfig(VERSION):
#     #根据刷新的版本，自动更新配置文件
#     pass

# 读取配置
HOSTNAME = sshinfo['hostname']
PORT = sshinfo['port']
USERNAME = sshinfo['username']
PASSWORD = sshinfo['password']

# 此处要主要路径转换为绝对路径不能使用~
downloadlist = []  # (remotefile,localfile)
remotepath = report['remotepath']
localpath = report['localpath']
# 调用脚本执行命令
command = f'export BASH_ENV=~/.bashrc;. ~/.profile && bash ~/RefreshConfirm/GetSvnLatestInfo.sh {localpath["upgradepath"]} {svnpath["upgradepath"]} '

# 定义shellOut协议
@dataclass
class Data_S():
	Operation: str = 'U'
	FilePath: str = '修改文件'
	Revision: int = '版本'
	ChangedAuthor: str = '变更人员'
	ChangedDate: str = 'yyyy-mm-dd hh24:mi:ss'  # strptime(ChangedDate, '%Y-%m-%d %H:%M:%S')


# 定义execleOut协议
@dataclass
class Data_E():
	# 编号，修改文件，开发人员，日期，回归情况
	Number: int = 0
	FilePaths: str = '文件列表'
	FileType: str = '交付件'
	ChangedAuthor: str = '开发人员'
	TestEngineer: str = '测试人员'
	UpStatus: str = '转测状态'
	# 如果B列为日期格式，那么会自动转换为datetime.datetime对象
	ChangedDate: str = 'yyyy-mm-dd hh24:mi:ss'
	Status: str = '回归情况'

def setdata(svnoutfile):
	svnoutlist = []
	with open(svnoutfile, 'r', encoding='utf-8') as csvfile:
		reader = DictReader(csvfile)
		for row in reader:
			svnoutlist.append(
				Data_S(row['Operation'], row['FilePath'], row['Revision'], row['ChangedAuthor'], row['ChangedDate']))
	return svnoutlist

def GetFileName(text: str):
	# 过滤掉特殊字符
	tarray = []
	for i in text.split():
		tarray.append(re.sub('["。”]', "", PurePath(i).name))
	return tarray

def retrieveAppend(command, ssh):
	stdin, stdout, stderr = ssh.exec_command(command)
	_file = stdout.read()
	remotefile = _file
	# 过滤为仅文件名不带目录
	localfile = PurePath(localpath, _file).name
	downloadlist.append((remotefile, localfile))


def main():
	# 打印配置信息
	print('svnpath', locals()['svnpath'], 'localpath', locals()['localpath'], 'sshinfo', locals()['sshinfo'], 'report',
		  locals()['report'], sep='\n')
	# 建立与后台的链接对象
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(HOSTNAME, port=PORT, username=USERNAME, password=PASSWORD)
	# 调用后台shell脚本，生成shellOut文件
	retrieveAppend(command, ssh)

	# 方式1：下载文件
	try:
		trans = ssh.get_transport()
		sftp = paramiko.SFTPClient.from_transport(trans)
		for file in downloadlist:
			sftp.get(*file)
	except FileNotFoundError as e:
		print("文件不存在，")

	# 方式2：直接返回数据
	# stdin,stdout,stderr=ssh.exec_command('cat '+ remotepath)
	# shellOut=stdout.read()
	# shellOut.decode().split('\n')
	ssh.close()

	# 读取svnout文件，保存为Data_S对象
	shellOutList = setdata(downloadlist[0][1])
	binOutList = setdata(downloadlist[1][1])
	jarOutList = setdata(downloadlist[2][1])
	warOutList = setdata(downloadlist[3][1])
	cfgOutList = setdata(downloadlist[4][1])

	def FindOne(efilename, eFileType, eChangedDate):
		# 判断文件是否一小时内更新
		f = lambda x: abs(
			datetime.strptime(x.ChangedDate, '%Y-%m-%d %H:%M:%S').__rsub__(eChangedDate).total_seconds()) < 3600
		if re.search('脚本', eFileType):
			for s in shellOutList:
				if re.search(efilename, s.FilePath) and f(s):
					return True
		elif re.search('BIN包', eFileType):
			for s in binOutList:
				if re.search(efilename, s.FilePath) and f(s):
					return True
		elif re.search('JAR包', eFileType):
			for s in jarOutList:
				if re.search(efilename, s.FilePath) and f(s):
					return True
		elif re.search('WAR包', eFileType):
			for s in warOutList:
				if re.search(efilename, s.FilePath) and f(s):
					return True
		elif re.search('配置', eFileType):
			for s in cfgOutList:
				if re.search(efilename, s.FilePath) and f(s):
					return True
		else:
			return False

	# 过滤掉非指定版本的信息
	# filter
	# 读取刷包excel，保存到Data_E对象
	excelOutList = []
	wb = load_workbook(localpath['excelpath'])
	sheet = wb.get_sheet_by_name('Sheet')
	for row in map(str, range(2, sheet.max_row + 1)):
		if sheet[f'L{row}'].value == '测试回归完成' or sheet[f'A{row}'].value == None:
			continue
		excelOutList.append(
			Data_E(sheet[f'A{row}'].value, sheet[f'F{row}'].value, sheet[f'E{row}'].value, sheet[f'G{row}'].value,
				   sheet[f'H{row}'].value, sheet[f'I{row}'].value, sheet[f'B{row}'].value, sheet[f'L{row}'].value))
	wb.close()
	# 分析shellOut和excelOut，并输出结果到ReportOut
	# rep = load_workbook(report['ReportOut'])

	rep_commited = open(report['rep1'], 'w+')
	rep_commited.write("==============" * 5 + "刷包转测文件数据整理，已转测部分" + "============" * 5 + "\n")
	rep_ready = open(report['rep2'], 'w+')
	rep_ready.write("=============" * 5 + "刷包转测文件数据整理，登记1小时以上部分" + "============" * 5 + "\n")

	for e in excelOutList[1:]:
		# 打印已转测部分
		if e.UpStatus is not None and re.search('已转测', e.UpStatus):
			rep_commited.write(f"编号：{e.Number}\n")
			rep_commited.write(f"文件：{e.FilePaths}\n")
			rep_commited.write(f"测试人员：{e.TestEngineer}\n")
			rep_commited.write(f"说明： excel中登记已转测")
			rep_commited.write("=================================" * 5 + "\n")
		# 对文件类型分类，用于对不同地址获取的svn信息进行确认
		else:
			for efilename in GetFileName(e.FilePaths):
				# 查找excel中未登记已转测，但svn有最近1小时提交记录的文件
				if FindOne(efilename, e.FileType, e.ChangedDate):
					rep_commited.write(f"编号：{e.Number}\n")
					rep_commited.write(f"文件：{e.FilePaths}\n")
					rep_commited.write(f"测试人员：{e.TestEngineer}\n")
					rep_commited.write(f"说明： excel中未登记已转测，但svn有最近1小时提交记录的文件")
					rep_commited.write("=================================" * 5 + "\n")
					# excel中未登记已转测，但svn有1小时以上提交记录的文件
				elif e.ChangedDate.__rsub__(datetime.now()).seconds >= 3600:
					rep_commited.write(f"编号：{e.Number}\n")
					rep_commited.write(f"文件：{e.FilePaths}\n")
					rep_commited.write(f"测试人员：{e.TestEngineer}\n")
					rep_commited.write(f"说明： excel中未登记已转测，但svn有1小时以上提交记录的文件")
					rep_commited.write("=================================" * 5 + "\n")
				else:
					rep_ready.write(f"编号：{e.Number}\n")
					rep_ready.write(f"文件：{e.FilePaths}\n")
					rep_ready.write(f"测试人员：{e.TestEngineer}\n")
					rep_ready.write(f"说明： 不完整数据，待确认")
					rep_ready.write("=================================" * 5 + "\n")

	rep_commited.close()
	rep_ready.close()


# 发到指定人员邮箱


if __name__ == "__main__":
	main()

# schedule.every(30).seconds.do(print('1'))
