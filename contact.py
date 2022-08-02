import pandas as pd
import re
import pymongo
client = pymongo.MongoClient("mongodb+srv://suriya315:12345678s@cluster0.kbh9v.mongodb.net/?retryWrites=true&w=majority")
db = client.mobile
pc=db.contacts
intp=input("view contact press (1),search contact press (2),create contact press (3),delete contact press (4) update conduct press (5):")
#functions
def finder(name):
    try:
        pc.find_one({"_id":name})["_id"]
    except:
        return False
    return True
def createc():
    name=input("enter the neme :")
    finder(name)
    if finder(name)==True:
        print("this name already exists enter valid name")
    else:
        for i in range(10):
            num=input("enter your nubmer :")
            if re.match("^\d{10}$",num):
                f={"_id":name,"number":num}
                pc.insert_one(f)
                print("contact created")
                break
            else:
                print("syntax error enter 10 digit number")
def viewer():
    data=pc.find()
    df=pd.DataFrame(data,columns=["_id","number"])
    df.rename(columns={"_id":"name"},inplace=True)
    df.set_index("name",inplace=True)
    print(df)
def view_c():
    ent=input("enter name are number :")
    g={"$or":[{"_id":{"$regex":ent}},{"number":{"$regex":ent}}]}
    a=pc.find(g)
    for i in a:
        print(i)
def deleten():
    ent=input("enter name :")
    g={"$or":[{"_id":{"$regex":ent}},{"_id":ent}]}
    a=pc.find_one(g)
    print(a)
    if a==None:
        print("not found")
    else:
        conf=input("yes//no confirm delete this number :")
        if conf=="yes":
            pc.delete_one(g)
            print("contact as deleted")
        else:
            pass
def updates():
    ent=input("enter name :")
    g={"_id":{"$regex":ent}}
    a=pc.find_one(g)
    print(a)
    if a==None:
        print("not found")
    else:
        wht=input("what do you update number or name")
        if wht=="name":
            names=input("enter your name :")
            if finder(names)==True:
                print("this name already exists enter valid name")
            else:
                new={"_id":names,"number":a["number"]}
                pc.insert_one(new)
                pc.delete_one(a)
                print("name as updated")
        elif wht=="number":
            for i in range(10):
                num=input("enter your nubmer :")
                if re.match("^\d{10}$",num):
                    my={"$set":{"number":num}}
                    pc.update_one(g,my)
                    print("contact number updated")
                    break
                else:
                    print("syntax error enter 10 digit number")
        else:
            print("enter valid input")
if intp=="1":
    viewer()
    
elif intp=="2":
    view_c()
    
elif intp=="3":
    createc()
    
elif intp=="4":
    deleten()
    
elif intp=="5":
    updates()
else:
    print("enter valid input try again")
