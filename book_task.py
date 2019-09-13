#check
import time
i = 0
contaсt_list =[]
friends_cat = "friends"
colleague_cat = ""
#Create your own command-line address-book program using which you can
#browse, add, modify, delete or search for your contacts such as friends, family
#and colleagues and their information such as email address and/or phone number.
#Details must be stored for later retrieval.
def startProg():
    print("\n\n\n\n\nWelcome to the address-book!",
          "\n\n\n\n\nPlease make your choice :)")
def startSpeech():
    print("\n\n-------------------->Press 1 to browse the addres book"+
          "\n-------------------->Press 2 to add a contact"+
          "\n-------------------->Press 3 to modify a contact"+
          "\n-------------------->Press 4 to delete a contact"+
          "\n-------------------->Press 5 to search a contact")
    time.sleep(2)
def byName_key(Person):
    return Person.nameSurname
def byEmail_key(Person):
    return Person.eMail
def byPhoneNumber_key(Person):
    return Person.phone
def byAddInfo(Person):
    return Person.addinfo
def doNprintByName():
    a = sorted(contaсt_list, key = byName_key)
    for member in a:
        member.introduceSelf() 
        print("\n\n")
def doNprintByEmail():
    a = sorted(contaсt_list, key = byEmail_key)
    for member in a:
        member.introduceSelf() 
        print("\n\n")
def doNprintByPhone():
    a = sorted(contaсt_list, key = byPhoneNumber_key)
    for member in a:
        member.introduceSelf() 
        print("\n\n")
def doNprintByAddInfo():
    a = sorted(contaсt_list, key = byAddInfo)
    for member in a:
        member.introduceSelf() 
        print("\n\n")
class Person:
    def __init__(self,nameSurname,eMail,phone,addInfo):
        self.nameSurname = nameSurname
        self.eMail = eMail
        self.phone = phone
        self.addInfo = addInfo
    def introduceSelf(self):
        print('Name and surname:'+self.nameSurname,
             '\nE-mail address:'+self.eMail,
             '\nPhone number:'+self.phone,
             '\nType: '+self.addInfo)
jack = Person('Jack Sparrow',"jack@gmail.com","899877321","no one")
adam = Person('Adam Johnson',"adam@gmail.com","898761213","Collegue")
becky = Person("Becky Mouse ","Becky state","9982718913","Friend")
#s1 = 'abc def ghi'
#s2 = 'def ghi abc'
#set1 = set(s1.split(' '))
#set2 = set(s2.split(' '))
#print set1 == set2 converting two strings to sets and comparing them
contaсt_list.append(jack)
contaсt_list.append(adam)
contaсt_list.append(becky)

#end of functions list
#algo for the main part
startProg()
exit = True
while exit != False:
    startSpeech()
    choice = input("Your choice: ")
    if choice == 1:
        print("You have decided to browse an address book, here you are")
        doNprintByName()
        break
    elif choice == 2:
       print("You have decided to add a new contact to the address book")
       print("Name and surname?")
       name = input()
       print("Email?")
       email = input()
       print("Phone number?")
       phoneNum = input()
       print("Additional info?")
       addInfo = input()
       contaсt_list.append(Person(name,email,phoneNum,addInfo))
       break
    elif choice == 3:
        print("You have decided to modify a contact, type the number or something else you've saved \n")
        searchIn = input()
        for member in contaсt_list:
            if any (searchIn == x for x in member.__dict__.values()):
                print("Type what you want to change: phone , email, name surname or additional info")
                change = input()
                if change == "phone":
                    print("Type it's new number")
                    newNumber = input()
                    member.phone = newNumber
                    break
                elif change == email:
                    print("Type new e-mail:\n")
                    newEmail = input()
                    member.eMail = newEmail
                    break
                elif change == "name surname":
                    print("Type new Name and Surname:\n")
                    newNameSurname = input()
                    member.nameSurname = newNameSurname
                elif change == "additional info":
                    print("Type new additional info\n")
                    newAddInfo = input()
                    member.addInfo = newAddInfo


        break
    elif choice == 4:
        print("You hace decided to delete a contact")
        break
    elif choice == 5:
        print("You have decided to search a contact")
        break
    elif choice == 6:
        print("You have decided to quit, thank you for using me!")
        time.sleep(3)
        exit = False

    
