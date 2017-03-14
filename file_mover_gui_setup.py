from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog #Used for browse function
import datetime
import file_mover_functions

def load_gui(self):
    
    # database
    file_mover_functions.create_db(self)

    ### define widgets ###
    self.button_browse_send = ttk.Button(self.master, text = "Browse", command =lambda:browse_send_function(self))
    self.button_browse_receive = ttk.Button(self.master, text = "Browse", command = lambda:browse_receive_function(self))
    self.button_run = ttk.Button(self.master, text = "Run", command = lambda:check_entries(self))
    self.button_cancel = ttk.Button(self.master, text = "Cancel", command = lambda:cancel_script(self))

    self.text_send = ttk.Entry(self.master, width = 20)
    self.text_receive = ttk.Entry(self.master, width = 20)

    self.label_send = ttk.Label(self.master, text = "Select folder to send")
    self.label_receive = ttk.Label(self.master, text = "Select destination folder")
    self.label_last_run_date = ttk.Label(self.master, text = "NOTE: This script was last run " + file_mover_functions.get_date(self))

    ### widget placement ###
    # buttons
    self.button_browse_send.grid(row=1, column=1, padx=5)
    self.button_browse_receive.grid(row=1, column=3, padx=5)
    self.button_run.grid(row=3, column=1, pady=20)
    self.button_cancel.grid(row=3, column=2, pady=20)

    # text
    self.text_send.grid(row=1, column=0, padx=5)
    self.text_receive.grid(row=1, column=2, padx=5)

    # labels
    self.label_send.grid(row=0, column=0, pady=10)
    self.label_receive.grid(row=0, column=2, pady=10)
    self.label_last_run_date.grid(row=4, column=0, columnspan=2)


### functions directly related to buttons on GUI ###

# Establishes browse function for locating folder of contents to send
def browse_send_function(self):
    self.browse_selection = filedialog.askdirectory(initialdir = "C:", title = "Select folder")
    self.text_send.insert(END, self.browse_selection)

# Establishes browse function for locating folder for destination of contents
def browse_receive_function(self):
    self.browse_selection = filedialog.askdirectory(initialdir = "C:", title = "Select folder")
    self.text_receive.insert(END, self.browse_selection)

# Checking to make sure fields have some data entry and then executes a series of
# calls to movement script and database for keeping script run dates
def check_entries(self):
    if not self.text_send.get() or not self.text_receive.get():
        messagebox.showerror("Error", "Please select filepaths using the browse buttons.")

    else:
        self.send_filepath = self.text_send.get()
        self.receive_filepath = self.text_receive.get()

        #Calling sqlite date_tracker.py script to get last_run_date of when updated_file_and_move.py was run
        self.last_run_date = file_mover_functions.get_date(self)

        #Calling updated_file_and_move.py to move files
        self.moved_summary = file_mover_functions.updated_file(self, self.send_filepath, self.receive_filepath, self.last_run_date)
        self.run_date = datetime.datetime.now()

        #Calling sqlite date_tracker.py to update database with new last_run_date
        file_mover_functions.log_date(self, self.run_date)
        
        #Messagebox to let user know which files have been transferred
        messagebox.showinfo("Succes", "These files have been transferred:\n{}".format(self.moved_summary))
        self.master.destroy()
        print(send_filepath, receive_filepath)

# Function for canceling script    
def cancel_script(self):
    if messagebox.askokcancel("Quit", "Do you really wish to cancel?"):
        self.master.destroy()


if __name__ == "__main__":
    pass
