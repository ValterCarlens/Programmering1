import json
import os
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

questions()

