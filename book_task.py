#Create your own command-line address-book program using which you can
#browse, add, modify, delete or search for your contacts such as friends, family
#and colleagues and their information such as email address and/or phone number.
#Details must be stored for later retrieval.
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
jack = Friend('Jack',"jack@gmail.com","899877321")
adam = Family('Adam',"adam@gmail.com","898761213")
becky = Colleague("Becky","Becky state","9982718913")
contaсt_list =[]
contaсt_list.append(jack)
contaсt_list.append(adam)
contaсt_list.append(becky)

def byName_key(Person):
    return Person.nameSurname
contaсt_list = sorted(contaсt_list, key = byName_key)
print("\n\n\n\n\n\n\n\n\n\n\n\n")
for member in contaсt_list:
    member.introduceSelf() 
    print("\n\n")