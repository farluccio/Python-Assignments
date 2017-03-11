##Created by Eric Farley, in Python 3.6.0

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog #Used for browse function
import updated_file_and_move #script file to move files 

root = Tk()
root.title("Auto Mover")

#filepaths
'''  C:/Users/Farley/Desktop/discard_send  C:/Users/Farley/Desktop/discard_receive  '''
### functions ###

def browse_send_function():
    browse_selection = filedialog.askdirectory(initialdir = "C:", title = "Select folder")
    text_send.insert(END, browse_selection)

def browse_receive_function():
    browse_selection = filedialog.askdirectory(initialdir = "C:", title = "Select folder")
    text_receive.insert(END, browse_selection)

def check_entries():
    if not text_send.get() or not text_receive.get():
        messagebox.showerror("Error", "Please select filepaths using the browse buttons.")

    else:
        send_filepath = text_send.get()
        receive_filepath = text_receive.get()
        moved_summary = updated_file_and_move.updated_file(send_filepath, receive_filepath)
        messagebox.showinfo("Succes", "These files have been transferred:\n{}".format(moved_summary))
        print(send_filepath, receive_filepath)
    
def cancel_script():
    if messagebox.askokcancel("Quit", "Do you really wish to cancel?"):
        root.destroy()

### define widgets ###
button_browse_send = ttk.Button(root, text = "Browse", command = browse_send_function)
button_browse_receive = ttk.Button(root, text = "Browse", command = browse_receive_function)
button_run = ttk.Button(root, text = "Run", command = check_entries)
button_cancel = ttk.Button(root, text = "Cancel", command = cancel_script)

text_send = ttk.Entry(root, width = 20)
text_receive = ttk.Entry(root, width = 20)

label_send = ttk.Label(root, text = "Select folder to send")
label_receive = ttk.Label(root, text = "Select destination folder")

### widget placement ###
button_browse_send.grid(row=1, column=1, padx=5)
button_browse_receive.grid(row=1, column=3, padx=5)
button_run.grid(row=3, column=1, pady=20)
button_cancel.grid(row=3, column=2, pady=20)

text_send.grid(row=1, column=0, padx=5)
text_receive.grid(row=1, column=2, padx=5)

label_send.grid(row=0, column=0, pady=10)
label_receive.grid(row=0, column=2, pady=10)


if __name__ == "__main__":
    root.mainloop()
    
