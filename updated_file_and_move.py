##Created by Eric Farley, Python 2.7.13
##
##Script created for Tech Academy drill to move files from one folder
##to another if they've been edited or created in the last 24 hours.


import shutil
import os
import datetime

## defining file paths, to and from folders (future: have user define both of these)
#originationFilePath = 'C:/Users/Farley/Desktop/discard_send'
#destinationFilePath = 'C:/Users/Farley/Desktop/discard_receive'


## for loop to determine if a file should be transferred (future update: pass in file paths)
def updated_file(originationFilePath, destinationFilePath):
    ## outlining list of files in holding folder
    fileList = os.listdir(originationFilePath)
    #print fileList
    moved_summary = []

    for item in fileList:
        
        fileListDate = os.path.getmtime(originationFilePath + '\\' + item)
        modDate = datetime.datetime.fromtimestamp(fileListDate)
        fileToMove = originationFilePath + '\\' + item
                    
        if (datetime.datetime.now() - modDate) < datetime.timedelta(hours=24):
            shutil.move(fileToMove, destinationFilePath)
            string_summary = [item]
            #print(string_summary)
            #print()
            moved_summary = moved_summary + string_summary

    return moved_summary


if __name__ == "__main__":
    pass

##End Script##
