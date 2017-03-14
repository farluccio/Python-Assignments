import sqlite3
import datetime
import shutil
import os


############### Moving Modified and New Files Function ###############

## for loop to determine if a file should be transferred (future update: pass in file paths)
def updated_file(self, originationFilePath, destinationFilePath, last_run_date):
    ## outlining list of files in holding folder
    fileList = os.listdir(originationFilePath)
    #print(fileList)
    self.moved_summary = []

    for item in fileList:
        
        fileListDate = os.path.getmtime(originationFilePath + '\\' + item)
        modDate = datetime.datetime.fromtimestamp(fileListDate)
        fileToMove = originationFilePath + '\\' + item

                   
        if modDate.strftime("%Y-%m-%d %H:%M:%S") > last_run_date:
            shutil.move(fileToMove, destinationFilePath)
            string_summary = [item]
            #print(string_summary)
            #print()
            self.moved_summary = self.moved_summary + string_summary

    return self.moved_summary


############### Database Query Functions ###############

# Function used to establish database if not present with default date
# and to pull the last datetime the file move script was ran to compare
# against possible new files that will need to be moved

def create_db(self):
    conn = sqlite3.connect('AutoMover.db')
    c = conn.cursor()

    c.execute('CREATE TABLE IF NOT EXISTS scriptRunDates(lastRun Text)')

    c.execute('SELECT * FROM scriptRunDates')

    #Entering a default date, (to be run only if there is no data in table)
    last_date_count = c.fetchall()
    #print(last_date_count)
    if not last_date_count:
        default_date = datetime.datetime(2001, 12, 13, 14, 15, 16)
        default_date = default_date.strftime("%Y-%m-%d %H:%M:%S")
        c.execute('INSERT INTO scriptRunDates VALUES(?)', (default_date,))
        conn.commit()
        
    conn.close()
    

def get_date(self):
    conn = sqlite3.connect('AutoMover.db')
    c = conn.cursor()
    
    #Querying for the latest date in table and returned for file date comparisons
    c.execute("SELECT max(lastRun) FROM scriptRunDates")
    self.last_run_dates = c.fetchone()
    self.last_run_date = self.last_run_dates[0]
    #print("max: ", last_run_date)

    conn.close()
    return self.last_run_date


#Function used to pass in date to table immediately after script is run
def log_date(self, log_run_date):
    conn = sqlite3.connect('AutoMover.db')
    c = conn.cursor()

    log_run_date = log_run_date.strftime("%Y-%m-%d %H:%M:%S")
    c.execute('INSERT INTO scriptRunDates VALUES(?)', (log_run_date,))
    conn.commit()

    conn.close()



if __name__ == "__main__":
    pass
