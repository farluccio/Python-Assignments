##Created by Eric Farley, Python 2.7.13
##
##This script is designed to move files from a directory to another directory.
##No user input is currently required.  User selected origination and destingation
##can be added later.

import shutil
import os


files = os.listdir('C:\Users\Student\Desktop\origination files')
print 'Files to be moved: ', files
print

originationPath = 'C:\Users\Student\Desktop\origination files\\'
#print originationPath
destinationFolder = 'C:\Users\Student\Desktop\destination files'
#print destinationFolder

##shutil.move('C:\Users\Student\Desktop\origination files\\first.txt',
##           'C:\Users\Student\Desktop\destination files')

for item in files:
    shutil.move(originationPath + item, destinationFolder)
    print 'moved', item, 'from', originationPath, 'to', destinationFolder
    print

##End Code##
