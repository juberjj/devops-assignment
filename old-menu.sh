#!/bin/bash

clear
echo "==========================================="
echo "AWS Ops. Please choose one of the following"
echo "==========================================="
echo

PS3=$'\n  Please choose a VALID option : '


options=("Create Instance" "List Instances" "Copy & Run WebsCheck" "Create & Copy to Bucket" "Terminate Instances" "Delete Bucket" "Quit")

#this produces a count on array list
#echo "length is ${#options[@]}"

COLUMNS=4

select opt in "${options[@]}"; do

	echo
case $opt in

"Create Instance")
echo -e "\nyou chose option $REPLY which is $opt\n"
./run_newwebserver.py
;;
"List Instances")
echo -e "\nyou chose option $REPLY which is $opt\n"
./list_instances.py
;;
"Copy & Run WebsCheck")
echo -e "\nyou chose option $REPLY which is $opt\n"
./copy_run_webckeck.py
;;
"Create & Copy to Bucket")
echo -e "\nyou chose option $REPLY which is $opt\n"
./bucket_cc.py
;;
"Terminate Instances")
echo -e "\nyou chose option $REPLY which is $opt\n"
./terminate_instances
;;
"Delete Bucket")
echo -e "\nyou chose option $REPLY which is $opt\n"
./delete_bucket
;;
"Quit")
break
;;
*) echo "invalid option $REPLY";;
esac
done
