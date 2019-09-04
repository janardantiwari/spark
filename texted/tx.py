from tkinter import *
from tkinter import filedialog 
from tkinter import messagebox


class Menubar:
    
    def __init__(self, parent):
      font_specs = ("ubuntu mono", 12)

      menubar =  Menu(parent.root, font=font_specs)
      parent.root.config(menu=menubar)

      filemenu =  Menu(menubar, font=font_specs, tearoff=0)
      filemenu.add_command(label="New",accelerator="Ctrl+N",
                                  command=parent.new_file)
      filemenu.add_command(label="Open",accelerator="Ctrl+O",
                                  command=parent.open_file)
      filemenu.add_command(label="Save",accelerator="Ctrl+S",
                                  command=parent.save)
      filemenu.add_command(label="Save As",accelerator="Ctrl+Shift+S",
                                  command=parent.save_as)
      filemenu.add_separator()
      filemenu.add_command(label="Exit",
                                  command=parent.root.destroy)
      about = Menu(menubar, font=font_specs, tearoff=0)
      about.add_command(label="Release Notes",
                                   command=self.show_release_notes)
      about.add_separator()
      about.add_command(label="About",
                                   command=self.show_about_message)


      menubar.add_cascade(label="File", menu=filemenu)
      menubar.add_cascade(label="About", menu=about)
    
    def show_about_message(self):
        title="About Jeditor"
        m="A simple text editor build in python"
        messagebox.showinfo(title,m)
    
    def show_release_notes(self):
        title="Release Notes"
        m="version -1.0 spark_in"
        messagebox.showinfo(title,m)

class statusbar:
    def __init__(self,parent):
         self.bar=StringVar()
         self.bar.set("Jeditor ver 1.0")
         font_specs = ("ubuntu mono", 14)
         l=Label(parent.tx,textvariable=self.bar,anchor='sw',fg='blue',font=font_specs)
         l.pack(side=BOTTOM,fill=BOTH)

    def update_status(self, *args):
        if isinstance(args[0], bool):
            self.bar.set("Your File Has Been Saved!")
        else:
            self.bar.set("Jeditor ver 1.0")

class jeditor:
  

    def __init__(self, root):
        root.title("Untitled - jeditor")
        root.geometry("1200x700")

        font_specs = ("ubuntu mono", 16)

        self.root = root

        self.tx =  Text(root, font=font_specs)
        self.scroll =  Scrollbar(root, command=self.tx.yview)
        self.tx.configure(yscrollcommand=self.scroll.set)
        self.tx.pack(side= LEFT, fill= BOTH, expand=True)
        self.scroll.pack(side= RIGHT, fill= Y)

        self.menubar = Menubar(self)
        self.filename = None
        self.status=statusbar(self)
        self.bind_shortcuts()
    def set_window_title(self,name=None,*k):
        
        if name:
            l=[str(x) for x in self.filename.split("/")]
            self.root.title( l[len(l)-1]+ '- jeditor')
        else:
            self.root.title("Untitled - jeditor")

    def new_file(self,*k):
        
        self.tx.delete(1.0, END)
        self.root.title("Untitled - jeditor") 

    def open_file(self,*k):
            self.filename = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("All Files", "*.*"),
                       ("Text Files", "*.txt"),
                       ("Python Scripts", "*.py")
                       ])
            if self.filename : 
                    
                    self.tx.delete(1.0, END)
                    with open(self.filename, "r") as f:
                        self.tx.insert(1.0, f.read())
                        self.set_window_title(self.filename)
       
    
    def save(self,*k):
        if self.filename :
            content = self.tx.get(1.0, END)
            with open(self.filename, "w") as f:
                f.write(content)
            self.status.update_status(True)
        else:
            self.save_as()

    def save_as(self,*k):
        try:
            new = filedialog.asksaveasfilename(
                initialfile="Untitled.txt",
                defaultextension=".txt",
                filetypes=[("All Files", "*.*"),
                       ("Text Files", "*.txt"),
                       ("Python Scripts", "*.py")
                       ])
            content = self.tx.get(1.0, END)
            with open(new, "w") as f:
                f.write(content)
            self.filename = new
            self.set_window_title(self.filename)
            self.status.update_status(True)
        except Exception as e:
            print(e)
    
    def bind_shortcuts(self):
        self.tx.bind('<Control-n>', self.new_file)
        self.tx.bind('<Control-o>', self.open_file)
        self.tx.bind('<Control-s>', self.save)
        self.tx.bind('<Control-S>', self.save_as)
        self.tx.bind('<Key>', self.status.update_status)


if __name__ == "__main__":
    root =  Tk()
    pt = jeditor(root)
    root.mainloop()
