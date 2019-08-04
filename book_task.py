#Create your own command-line address-book program using which you can
#browse, add, modify, delete or search for your contacts such as friends, family
#and colleagues and their information such as email address and/or phone number.
#Details must be stored for later retrieval.
def startProg():
    print("Welcome to the address-book!")
def startSpeech():
    print("Please, make your choise!",
      "/n/n-------------------->Press 1 to browse the addres book",
          "-------------------->Press 2 to add a contact",
          "-------------------->Press 3 to modify a contact",
          "-------------------->Press 4 to delete a contact",
          "-------------------->Press 5 to search a contact")
def byName_key(Person):
    return Person.nameSurname
def doNprint():
    a = sorted(contaсt_list, key = byName_key)
    print("\n\n\n\n\n\n\n\n\n\n\n\n")
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
jack = Friend('Jack Sparrow',"jack@gmail.com","899877321")
adam = Family('Adam Johnson',"adam@gmail.com","898761213")
becky = Colleague("Becky Mouse","Becky state","9982718913")
contaсt_list =[]
contaсt_list.append(jack)
contaсt_list.append(adam)
contaсt_list.append(becky)
doNprint()
