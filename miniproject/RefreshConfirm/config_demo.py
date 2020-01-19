VERSION='GOGOGO'
svnrootpath = f'http://127.0.0.1:9595/svn/archive/TEST{VERSION}/'
svnpath = {
    'excelpath':svnrootpath+'ExcelDir/{VERSION}_SIT进度登记.xlsx',
    'upgradepath':svnrootpath+f'UPGRATETOOL_ONLINE_{VERSION}_ng3.tar.gz',
    'mainupgradepath':f'http://127.0.0.1:9595/svn/script/{VERSION}',
    'war':svnrootpath+'WAR',
    'jar':svnrootpath+'JAR',
    'cpp':f'http://127.0.0.1:9595/svn/code/TEST{VERSION}/src/'
}

# svn存档地址
localrootpath = '/home/pi/RefreshConfirm/'
svnlocalpath = {
    'excelpath':localrootpath+f'ExcelDir/{VERSION}_SIT进度登记.xlsx',
    'upgradepath':localrootpath+f'UPGRATETOOL{VERSION}.tar.gz',
    'mainupgradepath':localrootpath+f'script/{VERSION}',
    'war':localrootpath+'WAR',
    'jar':localrootpath+'JAR',
    'cpp':localrootpath+f'TEST{VERSION}/src/'
}

# linuxssh信息
sshinfo = {
    'hostname':'192.168.0.4',
    'port':22,
    'username':'pi',
    'password':'wy20472183'
}
# 报告地址
lpath = f'D:\\ALLSVN\\ng3\\TEST{VERSION}\\InnerDoc\\NG3\\'
report = {
    'rush':lpath+f'{VERSION}_SIT进度登记.xlsx',
    'rep1':'F:\\DreamToDream\\OnMyWay\\Programming\\Python\\miniproject\\RefreshConfirm\\rep_commited.txt',
    'rep2':'F:\\DreamToDream\\OnMyWay\\Programming\\Python\\miniproject\\RefreshConfirm\\rep_ready.txt',
    'remotepath':'/home/pi/projectx/',
    'localpath':'D:\\',
}
