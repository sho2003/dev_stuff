#Checks if a certain url is available or not

import requests
import webbrowser

print("Enter the url: ")
url = input().strip()
try:
    response = requests.get(url, timeout = 5)
    print("The URL is valid, do you wish to open the page? [y,n]")
    op = input().lower().strip()
    if(op == 'y'):
        webbrowser.open(url, new = 1)
    else:
        print("Terminating program")
except:
    print("Given URL does not exist or there is a connection problem")
