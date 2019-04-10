#!/bin/bash
#shell调用timesten执行sql语句
currentDir=`pwd`
logdir=$(currendDir)/log
MemSQLFile=$1
DbConnectStr=$2
shellName=`basename $0`

if [ $# -le 0 ];then
    echo "No parameter,exit 1"
    exit 1
fi

if [ "x${MemSQLFile}" = "x" ];
then
    echo "MemSQLFile can not be NULL,exit 1"
    exit 1
fi


if [ "x${DbConnectStr}" = "x" ];
then
    echo "DbConnectStr can not be NULL,exit 1"
    exit 1
fi

sqlName=`echo  "${MemSQLFile}" | awk -F"/"'{print $NF}'`

tmpSqlLog="${logdir}/${sqlName}.log"

MemResultFile="${logdir}/${sqlName}.unl"

if [ ! -f "${MemSQLFile}" ];then
    echo "${MemSQLFile}文件不存在 exit 1" >>${tmpSqlLog}
    exit 1
fi

ExecuteMemSQL()
{
    ttisqlcs >/dev/null 2>${tmpSqlLog} <<EOF
    set verbosity 1;
    connect "${DbConnectStr}";
    spool $MemResultFile;
    @$MemSQLFILE;
    commit;
EOF
    if [ -s ${tmpSqlLog} ];then
        echo "`cat ${tmpSqlLog}`"
        rm -f ${tmpSqlLog}
        rm -f ${MemResultFile}
        exit 1
    else
        if [ -s $MemResultFile ];then
            sed 's/,[]/|/g;s/<NULL>//g;s/<[]//g;s/[]>//g;s/://g;s/ //g' $MemResultFile > $MemResultFile.temp
            awk -F '|' 'BEGIN{
                OFS="|"
                OutFile="'$MemResultFile'.temp.1"
            }
            {
                for(i=1;i<=NF;i++)
                {
                    if(length($(i))) == 16 && index($(i)),"-" > 0)
                    {
                        gsub("-","",$(i))
                        $(i) = substr($(i),1,14)
                    }
                }
                print >>OutFile
            }END{}' $MemResultFile.temp
            if [ -s $MemResultFile.temp.1 ];then
                mv $MemResultFile.temp.1 $MemResultFile
            fi
            rm -f $MemResultFile.temp $MemResultFile.temp.1
        else
            echo "Success export,but file size 0,delete"
            rm -f $MemResultFile
            echo "cat ${MemResultFile}"
            rm -r ${tmpSqlLog}
            rm -f ${MemResultFile}
            exit 0
        fi
    fi
    rm -f ${tmpSqlLog}
}