#check
import time
contaсt_list =[]
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
def doNprint():
    a = sorted(contaсt_list, key = byName_key)
    for member in a:
        member.introduceSelf() 
        print("\n\n")
class Person:
    def __init__(self,nameSurname,eMail,phone):
        self.nameSurname = nameSurname
        self.eMail = eMail
        self.phone = phone
    def introduceSelf(self):
        print('Name and surname:'+self.nameSurname,
             '\nE-mail address:'+self.eMail,
             '\nPhone number:'+self.phone)
class Friend(Person):
    def __init__(self,nameSurname,eMail,phone):
        Person.__init__(self, nameSurname,eMail,phone)
        print('\n\n\nNew contact added!\n\n'+
              'Name and surname :'+self.nameSurname,
              '\nE-mail address: '+self.eMail,
              '\nPhone number: '+self.phone+
                  '\nCategory: Friends')
    def introduceSelf(self):
        print('Name and surname :'+self.nameSurname,
              '\nE-mail address: '+self.eMail,
              '\nPhone number: '+self.phone+
              '\nCategory: Friends')
class Family(Person):
    def __init__(self,nameSurname,eMail,phone):
        Person.__init__(self, nameSurname,eMail,phone)
        print('\n\n\nNew contact added!\n\n'+
              'Name and surname :'+self.nameSurname,
              '\nE-mail address: '+self.eMail,
              '\nPhone number: '+self.phone+
              '\nCategory: Family')
    def introduceSelf(self):
        print('Name and surname:'+self.nameSurname,
             '\nE-mail address:'+self.eMail,
             '\nPhone number:'+self.phone+
             '\nCategory: Family')
class Colleague(Person):
    def __init__(self,nameSurname,eMail,phone):
        Person.__init__(self, nameSurname,eMail,phone)
        print('\n\n\nNew contact added!\n\n'+
              'Name and surname :'+self.nameSurname,
              '\nE-mail address: '+self.eMail,
              '\nPhone number: '+self.phone+
              '\nCategory: Collegues')
    def introduceSelf(self):
        print('Name and surname:'+self.nameSurname,
             '\nE-mail address:'+self.eMail,
             '\nPhone number:'+self.phone+
                 '\nCategory: Collegues')
#                                                            Checklist
#jack = Friend('Jack Sparrow',"jack@gmail.com","899877321")
#adam = Family('Adam Johnson',"adam@gmail.com","898761213")
#becky = Colleague("Becky Mouse ","Becky state","9982718913")
#contaсt_list.append(jack)
#contaсt_list.append(adam)
#contaсt_list.append(becky)

#end of functions list
#algo for the main part

startProg()
exit = True
while exit != False:
    startSpeech()
    choice = input("Your choice: ")
    if choice == 1:
        print("You have decided to browse an address book, here you are")
        doNprint()
        break
    elif choice == 2:
       print("You have decided to add a new contact to the address book")
       doNprint()
       break
    elif choice == 3:
        print("You hace decided to modify a contact")
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

    
