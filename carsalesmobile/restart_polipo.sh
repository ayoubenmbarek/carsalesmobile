#!/bin/bash
service='polipo'

#if (( $(ps -ef | grep -v grep | grep $service | wc -l) > 0 ))
#then
#echo "$service is running!!!"
#else
/etc/init.d/$service restart
echo "$service restarted!!!"
#fi
