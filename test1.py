import json

file = "test1.json"

def read():
    with open(file,"r") as f:
        info = json.load(f)
        for entry in info:
            site = entry["site"]
            user = entry["user"]
            pwd = entry["pwd"]
            notes = entry["notes"]
            print (f"Site: {site}")
            print (f"User: {user}")
            print (f"Pass: {pwd}")
            if (notes != "0"):
                print (f"Notes: {notes}")

def write():
    data = {}
    with open(file,"r") as f:
        temp = json.load(f)
    data["site"] = input("Site: ")
    data["user"] = input("User ID: ")
    data["pwd"] = input ("Password: ")
    data["notes"] = input("Notes (Press 0 if no notes): ")
    if (data["notes"] == "0"):
        data["notes"] == None
    temp.append(data)
    with open(file,"w+") as f:
        json.dump(temp,f,indent = 2)

write()
read()
