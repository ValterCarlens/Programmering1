import tkinter as tk
from tkinter import ttk
from functions import *

class MinGUI:
    
    def __init__(self):
        
        self.root = tk.Tk()

        self.check_state = tk.IntVar()

        self.root.geometry("600x700")
        self.root.title("Körkortsprov")

        self.label= tk.Label(self.root, text=""" 
    __
      ~( @\   ]
   __________]_[__/_>_____
   /  ____ \ <>            |  ____  ]
    =\_/ __ \_\_________|_/ __ \__D
______(__)_____________(__)____
-{-:Välkommen till ditt körkortprov!:-}  
""", font=("Arial", 10))
        self.label.pack()


        self.check = tk.Checkbutton(self.root, text="Alternativ 1", font=("Arial", 10))
        self.check.pack(padx=10, pady=10)

        self.check = tk.Checkbutton(self.root, text="Alternativ 2", font=("Arial", 10))
        self.check.pack(padx=10, pady=10)

        self.check = tk.Checkbutton(self.root, text="Alternativ 3", font=("Arial", 10))
        self.check.pack(padx=10, pady=10)

        self.check = tk.Checkbutton(self.root, text="Alternativ 4", font=("Arial", 10))
        self.check.pack(padx=10, pady=10)


        self.button = tk.Button(self.root, text="<-", font=("Arial", 10))
        self.button.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="->", font=("Arial", 10))
        self.button.pack(padx=10, pady=10)

        self.root.mainloop()

MinGUI()

