#Modul 8 Valter Carlens
import os
import datetime
import time
os.system("cls")


#upg1
"""
x=datetime.datetime.now()

print(x)
"""

#upg2
"""
x=datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))
"""


#upg3
def digital_clock():
    while True:
        # Rensa skärmen
        os.system("cls")

        # Hämta aktuell tid
        current_time = time.localtime()
        hours, minutes, seconds = current_time.tm_hour, current_time.tm_min, current_time.tm_sec

        # Formatera tiden som sträng
        time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"

        # Skriv ut tiden
        print(time_str)

        # Vänta en sekund innan nästa uppdatering
        time.sleep(1)

if __name__ == "__main__":
    digital_clock()


#upg5