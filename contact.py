import pandas as pd
import re
import pymongo
client = pymongo.MongoClient("mongodb+srv://suriya315:12345678s@cluster0.kbh9v.mongodb.net/?retryWrites=true&w=majority")
db = client.mobile
pc=db.contacts
intp=input("view contact press (1),search contact press (2),create contact press (3),delete contact press (4) :")
#functions
def createc():
    name=input("enter the neme :")
    def finder(name):
        try:
            pc.find_one({"_id":name})["_id"]
        except:
            return False
        return True
    if finder(name)==True:
        print("this name alread exised enter valid number")
    else:
        for i in range(10):
            num=input("enter your nubmer :")
            if re.match("\d{10}",num):
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
    ent=input("enter name are number")
    g={"$or":[{"_id":{"$regex":ent}},{"number":{"$regex":ent}}]}
    a=pc.find(g)
    for i in a:
        print(i)
                
        
            



if intp=="1":
    viewer()
    
elif intp=="2":
    view_c()
    
elif intp=="3":
    createc()
    
elif intp=="4":
    pass
else:
    print("enter valid input try again")
