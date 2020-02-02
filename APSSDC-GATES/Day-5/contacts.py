contact_application={}
# data storing
def store(name,number):
    if (name not in contact_application):
        contact_application.setdefault(name,number)
        print(name,"stored Sucessfully..!!")
    else:
        print("Already Exits in contacts..!!!")
# data Display
def display():
    if(len(contact_application)!=0):
        for name,number in contact_application.items():
            print(name,"--->",number)
    else:
        print("Contacts are Emty..!!!")
# Delete Particular Data
def delete(name):
    if(name not in contact_application.keys()):
        print(name,"dos't exits in contacts..!!!")
    else:
        contact_application.pop(name)
        print(name,"Deleted Sucessfully...!!")
# Serching particular Data
def search(name):
    if(name not in contact_application.keys()):
        print(name,"dos't exits in contacts..!!!")
    else:
        print(name,"-->",contact_application.get(name))
        