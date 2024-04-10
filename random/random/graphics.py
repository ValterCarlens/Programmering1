import tkinter as tk
from tkinter import *
from functions import *

class MinGUI:
    
    def __init__(self):
        
        self.root = tk.Tk()

        self.check_state = tk.IntVar()

        def display():
            if(checkbox.get()==True):
                print("Hej")
            else:
                print("Tjenis")

        checkbox = BooleanVar()

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


        self.check = tk.Checkbutton(self.root, text="Alternativ 1", font=("Arial", 10), variable=checkbox, onvalue=True, offvalue=False, command=display)
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

