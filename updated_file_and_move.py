##Holding folder for local computer
##Scan for holding folder baseline
##Scan holding folder for new and updated files
##Move new and updated files to "company's" (destination) folder
##(I have a script for moving files from folder to folder)


##cycle through files to determine if a new one is present and add
##to the list.  Compare the other dates.


import shutil
import os
import datetime

## defining file paths, to and from folders
originationFilePath = 'C:\Users\Student\Desktop\origination files'
destinationFilePath = 'C:\Users\Student\Desktop\destination files'

## outlining list of files in holding folder
fileList = os.listdir(originationFilePath)
#print fileList

## defining the last transfer time to compare with file modification date
lastTransfertime = datetime.datetime.today().replace(hour=23, minute=00) - datetime.timedelta(1)
print 'Last time files were moved:', lastTransfertime.strftime('%m-%d-%y %H:%M')
print

## for loop to determine if a file should be transferred
def updated_file():
    for item in fileList:
        
        fileListDate = os.path.getmtime(originationFilePath + '\\' + item)
        modDate = datetime.datetime.fromtimestamp(fileListDate)
        fileToMove = originationFilePath + '\\' + item
            
        if modDate > lastTransfertime:
            shutil.move(fileToMove, destinationFilePath)
            print 'Moved: ', item, '\nfrom', originationFilePath, '\nto', destinationFilePath
            print

if __name__ == "__main__":
    updated_file()
