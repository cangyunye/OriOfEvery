#!/bin/bash
##################
#功能：增量更新svn，提取svn信息组装到文件
#协议：Operation,FilePath,Revision,ChangedAuthor,ChangedDate
#作者：cangyunye
#时间：2020年1月4日21:06:10
##################
localuppath=$1 #localuppath
# 定义变量
uptmp=svnupdate.tmp
upfilter=svnupdate.filter
infotmp=svninfo.tmp
patA='^A ' #增加
patU='^U ' #更新
patD='^D ' #删除
# patR='^Restored' #恢复
patRev='^Revision'
patAut='Last Changed Author'
patDat='Last Changed Date'
FileRAD=RAD.tmp
# 取最底层目录名称
shellOutFile=${localuppath##*/}_shellOut.txt
CurrentDate=$(date +"%Y-%m-%d %H:%M:%S %z")

# 判断目录是否存在，不存在则根据配置重新svn checkout

if [ ! -d ${localuppath} ]; then
  mkdir -p $localuppath
  if [ ! -n $2 ]; then
    svnuppath=$2 #mainupgradepath
    svn co ${svnuppath}
  else
    echo "没有提供check out 地址，程序退出，请手工check out。"
    exit 0
  fi
fi
cd ${localuppath}

# 清理文件
rmfile=(${uptmp} ${upfilter} ${infotmp} ${FileRAD} ${shellOutFile})
for i in ${rmfile[@]}; do
  if [ -f ${i} ]; then
    #echo "清理$i"
    rm "./$i"
  else
    continue
  fi
done

# 提取update信息中的AUD
svn update >${uptmp}
cat ${uptmp} | egrep "$patA|$patU|$patD" | sed 's/[ ]\+/,/g' >${upfilter}

# 循环处理
#cat ${upfilter}|awk -F ',' '{print $2}' | while read line
cat ${upfilter} | while read line; do
  if [ ${line%,*} == 'D' ]; then # 由于删除文件不可update后追踪info，所以直接补充
    printf "Last Changed Author: DeleterUnKnown\nLast Changed Rev: 99999\nLast Changed Date: %s (一, 06 1月 2020)\n" "${CurrentDate}" >${infotmp}
  else
    svn info ${line#*,} >${infotmp}
  fi
  # 提取Revision,Author,Date部分,删除时区+时间部分和换行符
  egrep "${patRev}|${patAut}|${patDat}" ${infotmp} | awk -F': ' '{print $2}' | sed ':a;N;s/\n/,/g;s/ +.*)$//g;ta' >>${FileRAD}
done
# 加入首行列名
echo "Operation,FilePath,Revision,ChangedAuthor,ChangedDate" >${shellOutFile}
# 并列拼接
paste -d',' ${upfilter} ${FileRAD} >>${shellOutFile}
# 返回生成文件绝对路径
echo "`pwd`/${shellOutFile}"