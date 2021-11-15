#Simply finds out the connection strength

import time
import subprocess

sleepTime = 2
n = 5
strength = []
print("Pings: " + str(n))

#Repeat process n times
for i in range(n):

    #Gets output from the shell command
    out = subprocess.check_output("netsh wlan show interfaces", shell = True)

    #Gets the required connection strength
    for entry in out.decode().split('\n'):
        if(':' in entry):
            [key, value] = entry.split(": ")
            if(key.strip(". ") == "Signal"):
                strength.append(int(value[:2]))

    #Provides a gap between pings
    time.sleep(sleepTime)

avg = sum(strength)/n
print("The average signal strength is: " + str(avg) + "%")
