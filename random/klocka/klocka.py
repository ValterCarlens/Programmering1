import time
import os
while True:
    localtime = time.localtime()
    result = time.strftime("%I:%M:%S %p", localtime)
    os.system("cls")
    print(result)
    time.sleep(1)   