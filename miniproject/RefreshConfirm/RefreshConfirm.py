# 导入配置文件
from .config import *
from dataclasses import dataclass
import paramiko
from csv import DictReader
from openpyxl import load_workbook

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
	ChangedDate: str = '变更日期'


# 定义execleOut协议
@dataclass
class Data_E():
	# 修改文件，开发人员，日期，回归情况
	FilePath: str = '修改文件'
	ChangedAuthor: str = '开发人员'
	ChangedDate: str = 'yyyy/mm/dd hh24:mi:ss'
	Status: str = '回归情况'


def main():
	# 打印配置信息
	print('svnpath', locals()['svnpath'], 'localpath', locals()['localpath'], 'sshinfo', locals()['sshinfo'], 'report',
		  locals()['report'], sep='\n')
	# 建立与后台的链接对象
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(HOSTNAME, port=PORT, username=USERNAME, password=PASSWORD)
	# 调用后台shell脚本，生成shellOut文件
	ssh.exec_command(command)
	# 方式1：下载文件
	try:
		trans = ssh.get_transport()
		sftp = paramiko.SFTPClient.from_transport(trans)
		sftp.get(remotepath, localpath)
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
	wb = load_workbook('刷包.xlsx')
	sheet = wb.get_sheet_by_name('Sheet1')
	for row in map(str, range(2, sheet.max_row + 1)):
		for line in sheet[row]:
			excelOutList.append(Data_E(sheet[f'F{row}'], sheet[f'G{row}'], sheet[f'B{row}'], sheet[f'L{row}']))

	# 分析shellOut和excelparse，并输出结果到pythonOut

	# parseOut()


if __name__ == "__main__":
	main()

	# schedule.every(30).seconds.do(print('1'))
