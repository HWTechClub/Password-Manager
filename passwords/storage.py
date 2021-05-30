import json
import getpass

#imports the json data from the file to a variable passwords
file = "jsons.json"
with open(file,"r") as f:
    passwords = json.load(f)


def read():
    for entry in passwords:
        title = entry["title"]
        site = entry["site"]
        user = entry["user"]
        pwd = entry["pwd"]
        notes = entry["notes"]
        print(f"Title: {title}")
        print (f"Site: {site}")
        print (f"User: {user}")
        print (f"Pass: {pwd}")
        if (notes != "0"):
            print (f"Notes: {notes}")

def write():
    data = {}
    data["title"] = input("Title: ")
    for entry in passwords:
        if entry["title"] == data["title"]:
            print("This title is already in use. Please try another one.")
            write()
            exit()
    data["site"] = input("Site: ")
    data["user"] = input("User ID: ")
    data["pwd"] = password = getpass.getpass()
    data["notes"] = input("Notes (Press 0 if no notes): ")
    if (data["notes"] == "0"):
        data["notes"] == None
    passwords.append(data)
    with open(file,"w+") as f:
        json.dump(passwords,f,indent = 2)

def edit():
    query = input("Please enter the title of the site to search. ")
    search_results = 0
    for entry in passwords:
        if (entry["title"] == query):
            title = entry["title"]
            site = entry["site"]
            user = entry["user"]
            pwd = entry["pwd"]
            notes = entry["notes"]
            print(f"Title: {title}")
            print (f"Site: {site}")
            print (f"User: {user}")
            print (f"Pass: {pwd}")
            if (notes != "0"):
                print (f"Notes: {notes}")
            search_results = search_results + 1
    print (f"Search results: {search_results}")
    if (search_results == 0):
        print("This entry does not exist. ")
        exit()
    print("Please enter the new data.")
    write()
     
def delete():
    query = input("Please enter the title of the site to delete. ")
    for entry in range(len(passwords)):
        if (passwords[entry]["title"] == query):
            passwords.pop(entry)
            break
    

write()
#edit()
#read()
#delete()
#read()

