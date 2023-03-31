import tkinter as tk 
from tkinter import filedialog 
from datetime import datetime 
import os 
import platform 

class JournalApp:
    def __init__(self, master):
        self.master = master 
        master.title("Journal App")
        self.filename = None 
        self.save_folder = "path where journal entry will be saved" # path where journal entries will be saved 
        
        # Text widget for the journal entry 
        self.entry_text = tk.Text(master, height=20, width=80)
        self.entry_text.pack() 
        
        # creating a "Save" button to save journal entry 
        self.save_button = tk.Button(master, text="Save", command=self.save_entry)
        self.save_button.pack(side=tk.RIGHT)
        
        # creating an "Exit" button to exit the app or finilaze journal entry
        self.exit_button = tk.Button(master, text="Exit", command=master.quit)
        self.exit_button.pack(side=tk.LEFT)
        
        # bind "Save" function to CMD+S (Mac) & CNTRL+S (Windows) keyboard shortcut 
        # "Darwin" is the core Unix OS of macOS 
        if platform.system() == "Darwin":
            master.bind('<Command-s>', lambda event: self.save_entry())
        else:
            master.bind('<Control-s>', lambda event: self.save_entry())
            
        # bind "Exit" function to the Escape key. 
        master.bind('<Escape>', lambda event: master.quit())
            
    # get text of journal entry         
    def save_entry(self):
        entry = self.entry_text.get("1.0", "end-1c")
        
        # set default filename to current date if no filename chosen 
        if self.filename is None:
            now = datetime.now()
            # use the save_folder path instead of current working dir 
            self.filename = os.path.join(self.save_folder, now.strftime("%Y-%m-%d") + ".txt") 
            with open(self.filename, 'w') as f:
                f.write(f'Journal entry from {datetime.now().strftime("%Y-%m-%d")}:\n\n{entry}')
        else:
        # open the file in append mode 
            with open(self.filename, 'a') as f: 
                if os.path.getsize(self.filename) > 0: 
                    f.write('\n\n')
                # write journal entry along with date and time it was saved to the file 
                f.write(f'Journal entry from {datetime.now().strftime("%Y-%m-%d")}:\n\n{entry}')
                # clear the journal entry text 
            self.entry_text.delete('1.0', tk.END)
                
root = tk.Tk()
app = JournalApp(root) 
root.mainloop()