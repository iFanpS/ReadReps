#iFanpSisNoob
#MakeTheWorldWithCode - NumeX#1234
import requests
from pprint import pprint
import json

print("[ + ] Author:iFanpS")
print("[ + ] Credit: PythonCode(API)")
username = input("[?]Please input Github username: ")
url = f"https://api.github.com/users/"
pengguna_data = requests.get(url + username).json()
print("[ + ] ===========================")
pprint(pengguna_data)
print("[ + ] ===========================")