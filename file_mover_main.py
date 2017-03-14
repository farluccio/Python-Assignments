## Created by Eric Farley, in Python 3.6.0
##
## Used to answer a drill in moving files using mod dates and the last time
## the script was run

from tkinter import *
from tkinter import ttk
import file_mover_gui_setup



class fileMove(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)


        self.master = master
        #self.master.geometry(500)
        self.master.title("File Mover")
        
        # setting up GUI
        file_mover_gui_setup.load_gui(self)
        


if __name__ == "__main__":
    root = Tk()
    App = fileMove(root)
    root.mainloop()
    
