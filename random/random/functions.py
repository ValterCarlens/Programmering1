
import json
import os
import tkinter as tk
os.system("cls")

with open("weehoo.json", "r") as f:
    data = json.load(f)

def questions():
    print(f"""Vilken typ av växellåda är vanligtvis enklare att använda för nybörjare?
a) Manuell
b) Automatisk
c) CVT
d) Halvautomatisk data
{data["questions"][10]["alternative-two"]}""")



def startup():
    print("""
   -           __
 --          ~( @\   ]
---   _________]_[__/_>________
     /  ____ \ <>     |  ____  ]
    =\_/ __ \_\_______|_/ __ \__D
________(__)_____________(__)____
          
{-:Välkommen till ditt körkortprov!:-}
          """)
    
def blaj():
    root = tk.Tk()

    root.geometry("600x700")
    root.title("Körkortsprov")

    label= tk.Label(root, text=""" 
    __
      ~( @\   ]
   __________]_[__/_>_____
   /  ____ \ <>            |  ____  ]
    =\_/ __ \_\_________|_/ __ \__D
______(__)_____________(__)____
-{-:Välkommen till ditt körkortprov!:-}  
""", font=("Arial", 10))
    label.pack()

    root.mainloop()

blaj()
