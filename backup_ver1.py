import os
import time

#1. The files and directories to be backed up are specified in a list
source = ['"C:\\My Documents"', 'C:\\Code']
#Use double quotes inside the string  for names with spaces in it

#Backup directory
target_dir = 'D:\\Backup'
#Back it up into a zip file
#The name of the zip file are the current date and time
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

#Use the zip command to put the files in a zip archive

zip_command = "zip -ar {0} {1}".format(target, ''.join(source))

#Run the backup

if os.system(zip_command) == 0:
    print("Succesful backup to: ", target )
else:
    print("Backup failed ")
