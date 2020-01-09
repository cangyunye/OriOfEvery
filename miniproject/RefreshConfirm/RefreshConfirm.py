# 导入配置文件
from .config import *
from dataclasses import dataclass
import paramiko
from csv import DictReader
from openpyxl import load_workbook
from pathlib import PurePath
from time import strptime, mktime
# from datetime import datetime
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
	# 如果B列为日期格式，那么会自动转换为datetime.datetime对象
	ChangedDate: str = 'yyyy-mm-dd hh24:mi:ss'
	Status: str = '回归情况'


def filematcher(tbd):
	S, iE = tbd
	# 将文件列表分成每个文件
	E_chd = mktime(strptime(iE.ChangedDate))  # 每行的处理时间
	for ie in iE.FilePaths.split('\n'):
		# 将每个文件比对是否在shellOut里出现过
		for iS in S:
			S_chd = mktime(strptime(iS.ChangedDate))
			if re.search(PurePath(ie).name, iS.FilePath) and abs(S_chd - E_chd) <= 3600:
				return True


def compare(S, E):
	# 遍历excel数据
	# excelOutList[1].ChangedDate.__rsub__(datetime.now()).seconds <= 3600

# TODO 分类比较 if re.search('BIN',iE.FileType)
# 对于BIN
# 对于JAR/WAR
# 对于脚本/配置

def retrieveAppend(command,ssh):
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

	# 读取shellout文件，保存为Data_S对象
	shellOutList = []
	with open(report['shellOut'], 'r', encoding='utf-8') as csvfile:
		reader = DictReader(csvfile)
		for row in reader:
			shellOutList.append(
				Data_S(row['Operation'], row['FilePath'], row['Revision'], row['ChangedAuthor'], row['ChangedDate']))
	# 过滤掉非指定版本的信息
	# filter
	# 读取刷包excel，保存到Data_E对象
	excelOutList = []
	wb = load_workbook(localpath['excelpath'])
	sheet = wb.get_sheet_by_name('Sheet')
	for row in map(str, range(2, sheet.max_row + 1)):
		if sheet[f'L{row}'].value == '测试回归完成' or sheet[f'L{row}'].value == None:
			continue
		excelOutList.append(
			Data_E(sheet[f'A{row}'].value, sheet[f'F{row}'].value, sheet[f'E{row}'].value, sheet[f'G{row}'].value,
				   sheet[f'B{row}'].value, sheet[f'L{row}'].value))
	wb.close()

# 分析shellOut和excelparse，并输出结果到pythonOut

# parseOut()


if __name__ == "__main__":
	main()

# schedule.every(30).seconds.do(print('1'))
