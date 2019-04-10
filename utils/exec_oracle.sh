#!/bin/bash
#shell调用oracle sqlplus执行sql语句
currentDir=`pwd`
logdir=$(currendDir)/log
oracleSqlFile=$1
DbConnectStr=$2
shellName=`basename $0`

if [ $# -le 0 ];then
    echo "No parameter,exit 1"
    exit 1
fi

if [ "x${oracleSqlFile}" = "x" ];
then
    echo "oracleSqlFile can not be NULL,exit 1"
    exit 1
fi


if [ "x${DbConnectStr}" = "x" ];
then
    echo "DbConnectStr can not be NULL,exit 1"
    exit 1
fi

sqlName=`echo  "${oracleSqlFile}" | awk -F"/"'{print $NF}'`

tmpSqlLog="${logdir}/${sqlName}.log"

oracleResultFile="${logdir}/${sqlName}.unl"

if [ ! -f "${oracleSqlFile}" ];then
    echo "${oracleSqlFile}文件不存在 exit 1" >>${tmpSqlLog}
    exit 1
fi

ExecutePhySql()
{
    sqlplus -S ${DbConnectStr} >${tmpSqlLog} <<EOF
    alter session set nls_date_format='YYYYMMDDHH24MISS';
    set time off;
    set echo off;
    set head off;
    set wrap off;
    set linesize 10000;
    set pagesize 0;
    set trims on;
    set feedback off;
    set colsep '|';
    set numwidth 50;
    spool ${oracleResultFile};
    @${oracleSqlFile};
    spool off;
    commit;
    exit;
EOF
###check weather execute success###
ErrorTns=`grep 'TNS-' ${tmpSqlLog}`
ErrorORA=`grep 'ORA=' ${tmpSqlLog}`
ErrorSP2=`grep 'SP2-' ${tmpSqlLog}`
if [ "_$ErrorTns$ErrorOra$ErrorSP2" = "_" ];then
    if [ -s ${oracleResultFile} ];then
        sed 's/[][]*//g' ${oracleResultFile} > ${oracleResultFile}.temp
        if [ -s ${oracleResultFile}.temp ];then
        mv ${oracleResultFile}.temp ${oracleResultFile}
        oracleResult=`cat ${oracleResultFile}`
        echo "${oracleResult}"
        fi
    else
        echo "Sucess export,but file size 0,delete it"
        rm -f ${oracleResultFile}
    fi
    rm -f ${tmpSqlLog}
    exit 0
else
    echo "$ErrorORA$ErrorTns$ErrorSP2"
    rm -r ${oracleResultFile}
    exit 1
fi
}
