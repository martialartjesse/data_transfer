# Siebach_FinalProject
# Programmer: Jesse Siebach
# EMail: jsiebach@cnm.edu
# Purpose: Directory watch and automatic transfer and organization of data

# import necessary libraries
import time
import os
import os.path
import shutil
import sys

#define main data transfer function
def data_transfer():
    #define variables for directories
    #transfer_dir is our watch directory
    transfer_dir = os.path.normpath('E:/transfer')
    video_dir = os.path.normpath('W:/')
    music_dir = os.path.normpath('X:/')
    pic_dir = os.path.normpath('Y:/')
    #create our log file to track files transferred
    sys.stdout = open('E:/transfer_log.txt', 'w')
    #use os.walk to recursively search directories and files
    for root, dirs, files in os.walk(transfer_dir):
        for file in files:
            #variable to join or path and files
            file_src=os.path.join(root, file)
            #if statements to determine data type
            if file.endswith('.mp4') or file.endswith('.mkv') or file.endswith('.avi'):
                shutil.move(file_src, os.path.join(video_dir, file))
                print ('Video file transferred: ')
                print (file_src + '\n')
            if file.endswith('.mp3') or file.endswith('.FLAC'):
                shutil.move(file_src, os.path.join(music_dir, file))
                print ('Music file transferred: ')
                print (file_src + '\n')
            if file.endswith('.jpeg') or file.endswith('.jpg'):
                shutil.move(file_src, os.path.join(pic_dir, file))
                print ('Picture file transferred: ')
                print (file_src + '\n')
    #close our log file and close program 
    sys.stdout.close
    time.sleep(5)
    raise SystemExit
#WARN THE USER 
print ('Please be aware and careful, once this program runs it will begin transferring all files!')
print ('Stopping the program prematurely may cause data loss!')
print ('The program will exit automatically once files have been transferred')
#ask user if they would like to start the program 
start = raw_input ('Would you like to use the transfer tool? (y/n): ')
#if they want to, start it
while start.lower() == 'y':
    print ('The program will begin transferring your files.  ')
    print ('Once your files have completed transferring the program will exit!')
    print ('You can see the files transferred in E:/transfer_log.txt')
    print('Please open program again if needed.  Please be sure to only add files that have not already been transferred!')
    try:
        #run function
        data_transfer()     
    #raise exception if OS error occurs
    except OSError:
        print ('An OS error occurred please try again!')
else:
    print ('The program will now close!  Please re-open to use again!')




    
    


