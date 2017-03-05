##Created by Eric Farley, Python 2.7.13
##
##This script is designed to move files from a directory to another directory.
##No user input is currently required.  User selected origination and destingation
##can be added later.

import shutil
import os


files = os.listdir('C:\Users\Student\Desktop\origination files')
print 'Files contained in originating folder moved: ', files
print

originationPath = 'C:\Users\Student\Desktop\origination files\\'
#print originationPath
destinationFolder = 'C:\Users\Student\Desktop\destination files'
#print destinationFolder

##shutil.move('C:\Users\Student\Desktop\origination files\\first.txt',
##           'C:\Users\Student\Desktop\destination files')

def move_txt():
    for item in files:
        if '.txt' in item:
            shutil.move(originationPath + item, destinationFolder)
            print 'Moved', item, 'from', originationPath, 'to', destinationFolder
            print

if __name__ == "__main__":
    move_txt()


##End Code##
