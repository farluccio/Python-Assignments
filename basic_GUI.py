from tkinter import *
from tkinter import ttk
from tkinter import filedialog #Used for browse function
import updated_file_and_move #script file to move files 

root = Tk()

root.title("Auto Mover")

### define widgets ###
button_browse_send = ttk.Button(root, text = "Browse")
button_browse_receive = ttk.Button(root, text = "Browse")
button_run = ttk.Button(root, text = "Run")
button_cancel = ttk.Button(root, text = "Cancel")

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

### functions ###

def browse_send_function(event):
    browse_selection = filedialog.askdirectory(initialdir = "C:", title = "Select folder")
    text_send.insert(END, browse_selection)

def browse_receive_function(event):
    browse_selection = filedialog.askdirectory(initialdir = "C:", title = "Select folder")
    text_receive.insert(END, browse_selection)

def check_entries(event):
    if not text_send.get() or not text_receive.get():
        showerror("Error", "Please select filepaths using the browse buttons.")

    else:
        send_filepath = text_send.get("1.0",'end-1c')
        receive_filepath = text_receive.get("1.0",'end-1c')
        updated_file_and_move.updated_file(send_filepath, receive_filepath)
        showinfo("Succes", "Files have been transferred")

def cancel_script(event):
    root.destroy function

button_browse_send.bind("<Button-1>", browse_send_function)
button_browse_receive.bind("<Button-1>", browse_receive_function)
button_run.bind("<Button-1>", check_entries) 
button_cancel.bind("<Button-1>", cancel_script)

root.mainloop()
