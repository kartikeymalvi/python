# PROPERTIES OF OOPS=====>
# Abstraction===>Showing only required code and hide internal process
    # in order to use abstract class we have to import==>
    # from abc import ABC,abstractmethod
# example==>

from abc import ABC,abstractmethod
class BankApp(ABC):
    def login(self):
        print('user login..')
    def logout(self):
        print('User Logout...')
    def userdata(self):
        print('user-details')
    @abstractmethod #Abstractmethod decorator
    def database(self): 
        pass
class webpage(BankApp):
    def database(self):
        print('database')
    def new(self):
        print('this is anoter method od chlid')

obj=webpage()     
obj.database()
obj.login()
obj.userdata()
obj.logout()  
obj.new()                                                                                                                             



