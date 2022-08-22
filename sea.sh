#!/usr/bin/bash
while true
do
clear
echo "sleep 60 sec"
echo 'select top 10 * from ethdb order by numb desc' | curl 'http://localhost:8123/?query=' --data-binary @-
sleep 60
done
