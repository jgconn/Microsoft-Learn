#run this with the command uvicorn unitec_class:app
from fastapi import FastAPI
import requests
import os
from cryptography.fernet import Fernet

app = FastAPI(docs_url="/")

@app.get("/hello")
def blah():
    return "this is an api"

@app.get("/users")
def getUsers():
    return ["Justin", "Apil", "Max", "Kris"]

errorChk = "This video isn't available any more"
fakePage = "<html> Website code </html>"
validURL = "https://www.youtube.com/watch?v=MNLcUVGTflI5555555"

page = requests.get(validURL).text

# print(validURL.split("=")[1])
# print(len("LqME1y6Mlyg"))
#print(page.index(errorChk))

try:
    page.index(errorChk) # and validURL.split("=")[1] == 11
except:
    print("Valid URL")
else:
    print("Invalid URL: " + errorChk)

key = Fernet.generate_key()

f = Fernet(key)
token = f.encrypt(b"A really secret message")
print(token)