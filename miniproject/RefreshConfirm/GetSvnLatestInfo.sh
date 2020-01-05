#!/bin/bash
##################
#功能：增量更新svn，提取svn信息组装到文件
#协议：Operation,FilePath,Revision,ChangedAuthor,ChangedDate
#作者：cangyunye
#时间：2020年1月4日21:06:10
##################
localuppath=$1 #localuppath
mainuppath=$2 #mainupgradepath
# 定义变量
uptmp=svnupdate.tmp
upfilter=svnupdate.filter
infotmp=svninfo.tmp
FileA=svnupdate.A
FileU=svnupdate.U
FileD=svnupdate.D
patA='^A ' #增加
patU='^U ' #更新
patD='^D ' #删除
patRev='^Revision'
patAut='Last Changed Author'
patDat='Last Changed Date'
FileRAD=RAD.tmp
shellOutFile=shellOut.txt


# 判断目录是否存在，不存在则根据配置重新svn checkout

if [ ! -f ${localuppath} ]
    then
    mkdir -p $localuppath
    svn co ${mainuppath}
fi
cd ${localuppath}

# 清理文件
rm ${uptmp} ${upfilter} ${infotmp} ${FileA} ${FileU} ${FileD} ${shellOutFile}

# 进入localrootpath
cd ${localrootpath}
# 提取update信息中的AUD
svn update > ${uptmp}
cat ${uptmp} | egrep "$patA|$patU|$patD" | sed  's/[ ]\+/,/g' > ${upfilter}
#cat ${uptmp} | grep "$patA" > ${FileA}
#cat ${uptmp} | grep "$patU" > ${FileU}
#cat ${uptmp} | grep "$patD" > ${FileD}
# 用逗号分隔成csv文件
# awk '{print $1 ","$2}' ${upfilter} >　${uptmp}
# 循环处理
cat ${upfilter}|awk -F ',' '{print $2}' | while read line
do
svn info $line > ${infotmp}
# 提取Revision,Author,Date部分
egrep "${patRev}|${patAut}|${patDat}" ${infotmp} | awk -F': ' '{print $2}'| sed ':a;N;s/\n/,/g;ta' >>${FileRAD}
done
# 并列拼接
paste -d',' ${upfilter} ${FileRAD} >${shellOutFile}