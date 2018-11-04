#!/bin/bash
while :
do
    sshpass -p 'robots1234' scp message.txt pi@192.168.43.94:UTRAHACKS_TEAM42/MotorControl 
done
