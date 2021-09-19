from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)


def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()


def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
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


def quitApp():
    root.destroy()   # app close ho jayega

def Undo():
    TextArea.edit_undo()

def cut():
    TextArea.event_generate("<<Cut>>")

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def Del():
    TextArea.delete('1.0','end')  #1.0- first line se  #end- last line tak

def SelectAll():
    TextArea.tag_add('sel','1.0','end') #sel- select, 1.0- first line, 'end'- last line
def TimeDate():
    from datetime import datetime
    now = datetime.now()
    ft = now.strftime('%Y-%m-%d %I:%M:%S')
    TextArea.insert('end', ft)


def NewWindow():
    if __name__ == '__main__':
        # Basic tkinter setup
        root = Tk()
        root.title("Untitled - Notepad")
        root.wm_iconbitmap("note.png")
        root.geometry("788x444")

        # Add TextArea
        TextArea = Text(root, font="lucida 13" )
        file = None
        TextArea.pack(expand=True, fill=BOTH )

        # Lets create a menubar
        MenuBar = Menu(root)

        # File Menu Starts
        FileMenu = Menu(MenuBar, tearoff=0)
        # To open new file
        FileMenu.add_command(label="New", command=newFile)

        # to open new window file

        FileMenu.add_command(label="New Window", command=NewWindow)

        # To Open already existing file
        FileMenu.add_command(label="Open", command=openFile)

        # To save the current file

        FileMenu.add_command(label="Save", command=saveFile)
        FileMenu.add_separator()
        FileMenu.add_command(label="Exit", command=quitApp)
        MenuBar.add_cascade(label="File", menu=FileMenu)
        # File Menu ends

        # Edit Menu Starts
        EditMenu = Menu(MenuBar, tearoff=0)
        # To give a feature of cut, copy and paste
        EditMenu.add_command(label="Undo", command= TextArea.edit_undo)
        EditMenu.add_command(label="Cut", command=cut)
        EditMenu.add_command(label="Copy", command=copy)
        EditMenu.add_command(label="Paste", command=paste)
        EditMenu.add_command(label="Del", command=Del)
        EditMenu.add_separator()
        EditMenu.add_command(label="Select All", command=SelectAll)
        EditMenu.add_command(label="Time/Date", command=TimeDate)

        MenuBar.add_cascade(label="Edit", menu=EditMenu)

        # Edit Menu Ends

        # Help Menu Starts
        HelpMenu = Menu(MenuBar, tearoff=0)
        HelpMenu.add_command(label="About Notepad", command=about)
        MenuBar.add_cascade(label="Help", menu=HelpMenu)

        # Help Menu Ends

        root.config(menu=MenuBar)

        # Adding Scrollbar using rules from Tkinter lecture no 22
        Scroll = Scrollbar(TextArea)
        Scroll.pack(side=RIGHT, fill=Y)
        Scroll.config(command=TextArea.yview)
        TextArea.config(yscrollcommand=Scroll.set)

        root.mainloop()

def about():
    showinfo("Notepad", "Notepad by noushad ansari")

if __name__ == '__main__':
    #Basic tkinter setup
    root = Tk()
    root.title("Untitled - Notepad")
    root.wm_iconbitmap("note.png")
    root.geometry("788x444")

    #Add TextArea
    TextArea = Text(root, font="lucida 13" ,undo=True)
    file = None
    TextArea.pack(expand=True, fill=BOTH )

    # Lets create a menubar
    MenuBar = Menu(root)

    #File Menu Starts
    FileMenu = Menu(MenuBar, tearoff=0)  # --------ye line ayegi tearoff nhi lagaya to
    # To open new file
    FileMenu.add_command(label="New", command=newFile)

    # to open new window file

    FileMenu.add_command(label="New Window", command=NewWindow)

    #To Open already existing file
    FileMenu.add_command(label="Open", command = openFile)

    # To save the current file

    FileMenu.add_command(label = "Save", command = saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label = "Exit", command = quitApp)
    MenuBar.add_cascade(label = "File", menu=FileMenu)
    # File Menu ends

    # Edit Menu Starts
    EditMenu = Menu(MenuBar, tearoff=0)
    #To give a feature of cut, copy and paste
    EditMenu.add_command(label="Undo", command= TextArea.edit_undo)
    EditMenu.add_command(label="Redo", command=TextArea.edit_redo)
    EditMenu.add_command(label = "Cut", command=cut)
    EditMenu.add_command(label = "Copy", command=copy)
    EditMenu.add_command(label = "Paste", command=paste)
    EditMenu.add_command(label="Del", command=Del)
    EditMenu.add_separator()
    EditMenu.add_command(label="Select All", command=SelectAll)
    EditMenu.add_command(label="Time/Date", command=TimeDate)

    MenuBar.add_cascade(label="Edit", menu = EditMenu)

    # Edit Menu Ends

    # Help Menu Starts
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label = "About Notepad", command=about)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)

    # Help Menu Ends

    root.config(menu=MenuBar)

    #Adding Scrollbar using rules from Tkinter lecture no 22
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,  fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)

    root.mainloop()
