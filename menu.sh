#!/bin/bash
# Author: Juber Nunes
# Date: 05/03/2019
# Description: Main Menu program. 

#clear
exit=0
# Controls the menu loop until user hits 0 to exit the menu
while [ $exit -ne 1 ] # It will repeat itself as long exit is not equal to 1
  do
    # Main Menu  - Options
    clear
    echo "==========================================="
    echo "AWS Ops. Please choose one of the following"
    echo "==========================================="
    echo -e "\n"
    echo "1. Create Instance"
    echo "2. List Instances"
    echo "3. Copy & Run WebsCheck"
    echo "4. Create & Copy to Bucket"
    echo "5. Terminate Instances"
    echo "6. Delete Bucket"
    echo "0. Exit"
    echo -e "\n"
    echo -e "Enter a number: \c"
    read number
      case "$number" in
        1) ./run_newwebserver.py 
           ;;
        2) ./list_instances.py 
           ;;
        3) ./copy_run_webckeck.py 
           ;;
        4) ./bucket_cc.py 
           ;;
        5) ./terminate_instances.py
           ;;
        6) ./delete_buckets.py 
           ;;
        0) echo "Exiting...." # Ends the program
           sleep 1
           clear
           exit
           ;;
           # Capture invalid selection asking for new selection
        *) echo "Invalid option. Please choose again!"
           sleep 1
           clear
           ;;
     esac
  done

