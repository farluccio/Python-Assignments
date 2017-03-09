##Created by Eric Farley, Python 2.7.13
##
##Script created for Tech Academy drill to move files from one folder
##to another if they've been edited or created in the last 24 hours.


import shutil
import os
import datetime

## defining file paths, to and from folders (future: have user define both of these)
#originationFilePath = 'C:\Users\Student\Desktop\origination files'
#destinationFilePath = 'C:\Users\Student\Desktop\destination files'

## defining a reocurring transfer time
##lastTransfertime = datetime.datetime.today().replace(hour=23, minute=00) - datetime.timedelta(1)
##print 'Last time files were moved:', lastTransfertime.strftime('%m-%d-%y %H:%M')
##print

## for loop to determine if a file should be transferred (future update: pass in file paths)
def updated_file(originationFilePath, destinationFilePath):
    ## outlining list of files in holding folder
    fileList = os.listdir(originationFilePath)
    #print fileList

    for item in fileList:
        
        fileListDate = os.path.getmtime(originationFilePath + '\\' + item)
        modDate = datetime.datetime.fromtimestamp(fileListDate)
        fileToMove = originationFilePath + '\\' + item
                    
        if (datetime.datetime.now() - modDate) < datetime.timedelta(hours=24):
            shutil.move(fileToMove, destinationFilePath)
            print 'Moved: ', item, '\nfrom', originationFilePath, '\nto', destinationFilePath
            print

if __name__ == "__main__":
    updated_file()

##End Script##
