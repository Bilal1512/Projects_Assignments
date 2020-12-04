from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
import os.path
import re
import time
from time import *

# Defining all the functions based on which our Sub-Menus will work

# Function for creating new file
def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)

# Function for opening a file
def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "."),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()

# Function to save a file
def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "."),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()

# Function which implements save as
def saveasFile():
    global file
    file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "."),
                                     ("Text Documents", "*.txt")])
    if file =="":
        file = None

    else:
        #Save as a new file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()

        root.title(os.path.basename(file) + " - Notepad")
        print("File Saved")

# Function to close our GUI App
def quitApp():
    root.destroy()

# Functions to implements Cut, Copy and Paste
def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

# Function to count number of characters in Text Area
def charcount():
    text = TextArea.get(1.0, END)
    showinfo("Character Count", len(text))

# Function to count number of words in Text Area    
def wordcount():
    text = TextArea.get(1.0, END)
    showinfo("Word Count", len(re.split("\s",text))-1)

# Function to display modified time
def modification_time():
    global file
    import os.path, time
    mtime = time.ctime(os.path.getmtime(file))
    showinfo("Modification time",mtime)

# Function to display creation time    
def creation_time():
    global file
    import os.path, time
    ctime = time.ctime(os.path.getctime(file))
    showinfo("Creation time:",ctime)

# Function to Find/Replace a word given as Input
def find_func(event=None):
##using tag inbuilt function
    def find():
        word = find_input.get()
        TextArea.tag_remove('match','1.0',tk.END)
        matches = 0
        if word :
            start_pos = '1.0'
            while True :
                start_pos = TextArea.search(word,start_pos,stopindex=tk.END)
                if(not start_pos):
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                TextArea.tag_add('match',start_pos,end_pos)
                matches +=1
                start_pos=end_pos
            TextArea.tag_config('match',background='blue')
        find_input.focus_set()




    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = TextArea.get(1.0,tk.END)
        new_content = content.replace(word,replace_text)
        TextArea.delete(1.0,tk.END)
        TextArea.insert(1.0,new_content)


    find_dialogue = tk.Toplevel()
    find_dialogue.geometry('450x250+500+200')
    find_dialogue.resizable(0,0)

    ## frame
    find_frame = tk.LabelFrame(find_dialogue, text ='Find/Replace')
    find_frame.pack(pady=20)

    ## labels 
    text_find_label = tk.Label(find_frame,text ='Find :')
    text_replace_label = tk.Label(find_frame,text ='Replace')

    ##entry boxes 
    find_input = tk.Entry(find_frame,width=30)
    replace_input = tk.Entry(find_frame,width=30)


    ## Button
    find_button = tk.Button(find_frame,text ='Find',command=find)
    replace_button = tk.Button(find_frame,text ='Replace',command=replace)

    ##label grid
    text_find_label.grid(row=0,column=0,padx=4,pady=4)
    text_replace_label.grid(row=1,column=0,padx=4,pady=4)

    ##entry grid
    find_input.grid(row=0, column=1,padx=4,pady=4)
    replace_input.grid(row=1, column=1,padx=4,pady=4)

    ##button grid
    find_button.grid(row=2 ,column=0 ,padx=8,pady=4)
    replace_button.grid(row=2 ,column=1 ,padx=8,pady=4)

    find_dialogue.mainloop()


if __name__ == '__main__':
    
    # Basic tkinter setup
    root = Tk()
    root.title("Untitled - Notepad") # Default title of our GUI
    root.geometry("644x788") # Default Geometry of our GUI
    root.minsize(200,100) # Set min width,height 
    root.maxsize(800,800) # Set max width,height

    # Add TextArea
    TextArea = Text(root, font="lucida 13") # Defining the textarea with a particular Font
    file = None
    TextArea.pack(expand=True, fill=BOTH)
    import tkinter as tk
    from tkinter import *

    # Lets create a menubar
    MenuBar = Menu(root)

    #File Menu Starts
    FileMenu = Menu(MenuBar, tearoff=0) # Tearoff = 0 means that it can't be separated from NotePad Window
    
    # To open new file
    FileMenu.add_command(label="New", command=newFile) # Add Command adds a menu item to the Menu

    #To Open already existing file
    FileMenu.add_command(label="Open", command = openFile)

    # To save the current file
    FileMenu.add_command(label = "Save", command = saveFile)
    
    # To save the current file with name of our Choice
    FileMenu.add_command(label = "Save As", command = saveasFile)
    FileMenu.add_separator() # Adds a separate line to the Menu
    
    # To exit the NotePad
    FileMenu.add_command(label = "Exit", command = quitApp)
    MenuBar.add_cascade(label = "File", menu=FileMenu) # Creates a new hierarchical menu by associating a given menu to a parent menu
    # File Menu ends

    # Edit Menu Starts
    EditMenu = Menu(MenuBar, tearoff=0)
    #To give a feature of cut, copy and paste
    EditMenu.add_command(label = "Cut", command=cut)
    EditMenu.add_command(label = "Copy", command=copy)
    EditMenu.add_command(label = "Paste", command=paste)
    
    # To find a particular word and then replace it
    EditMenu.add_command(label = "Find/Replace", command=find_func)

    MenuBar.add_cascade(label="Edit", menu = EditMenu)

    # Edit Menu Ends

    # Stats Menu Starts
    HelpMenu = Menu(MenuBar, tearoff=0)
    
    # To count total number of words
    HelpMenu.add_command(label = "Word Count", command=wordcount)
    # To count total number of characters
    HelpMenu.add_command(label = "Char Count", command=charcount)
    # To see the time when file was created
    HelpMenu.add_command(label = "Created Time", command=creation_time)
    # TO see the time when file was last Modified
    HelpMenu.add_command(label = "Modified Time", command=modification_time)
    MenuBar.add_cascade(label="Stats", menu=HelpMenu)

    # Stats Menu Ends

    root.config(menu=MenuBar) # This sets MEnuBar as menu in our GUI
    
    root.mainloop() # Event Loop / Main Loop(Keeps us in GUI Window and implements GUI Logic)