#!/bin/bash
# Test Version 1.0
####################Initialization
# Display "User", "Logging time"
echo  AD-OEM Ottocode running scripts
echo "Author: W.."
echo "wait ......"
who
sleep 3
####################Install fping if not
echo Checking fping installed or not
echo Wait ......
sleep 3
if  dpkg-query -W -f='${Status}' fping 2>/dev/null | grep -c "ok installed";then
    echo "fping installed";   
    #apt install git;
else
    echo "fping not installed!";
    sudo apt-get install fping;
    echo "fping done"
fi
echo "Installation are all set! Thanks"
#sleep 2
###################Check PC connection
echo Checking PC1 PC2 HMI-PC  
echo "Wait ......"
sleep 3
PC1="192.168.1.110"
PC2="192.168.1.120"
HMI="192.168.1.150"
# PC1
echo PC1:$PC1
if fping -q $PC1;then
    echo "PC1 connection is working"
else
    echo "Issue: PC1 connection is not working"
    exit 1
fi
# PC2
echo PC2:$PC2
if fping -q $PC2;then
    echo "PC2 connection is working"
else
    echo "Issue: PC2 connection is not working"
    exit 1
fi
# HMI
echo HMI:$HMI
if fping -q $HMI;then    
echo "HMI connection is working"
else
    echo "Issue: HMI connection is not working!"
    exit 1
fi
echo "PC1 PC2 HMI-PC Ping connection Done!"
echo "wait ......"
sleep 3
##################Bash trap monitor function
trap bashtrap INT
# bash trap function is executed when CTRL-C is pressed:
# bash prints message => Executing bash trap subrutine !
bashtrap()
{
   clear 
   echo "CTRL+C Detected !...executing bash trap !"
   # clear
}
##################Check sync time
echo "Check ntpdate until 0.000"
echo "Wait ......"
sleep 3
#sudo ntpdate -b PC1
for i in `seq 1 3`;
do
    sudo ntpdate -b $PC1
    echo $i times to check ntpdate
done   
echo "Ntpdate less than 0.001 second done !"
###################TCP connection
echo "Check --tcp"
echo "Wait ......"
sleep 3
#clear
#gnome-terminal --window-with-profile=Terminal -e "scs --tcp"
scs --tcp
#echo "TCP done"
###################Start ottoview
# open another terminal
gnome-terminal --window-with-profile=Terminal -e "ottoview_mian"
#gnome-terminal --window-with-profile=Terminal -e "ping www.aptiv.com"
#gnome-terminal -e history
#ping www.aptiv.com
#ottoview_main
