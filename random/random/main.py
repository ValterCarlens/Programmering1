import os
import json
from msvcrt import getwch
from functions import *
"keys=[1, 2, 3, 4]"

"choice = getwch()"

startup()
while True:
    os.system("cls")

    with open("weehoo.json", "r") as f:
        data = json.load(f)

    print(data["questions"][10]["alternative-two"])