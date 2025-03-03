# combining 3 methods-->
# 1.Instence method
# 2.Class method
# 3.static method


class Book:
    price=100       #static or class variable
    total_page=500 #static or class variable
    def __init__(self,title,author):
        self.title=title
        self.author=author
    @classmethod
    def update(cls,newprice,new_page_count):
        cls.price=newprice
        cls.total_page=new_page_count
    @classmethod
    def addnew(cls,author):
        cls.author2=author
    def showdetails(self):
        print(self.title,self.author,Book.price,Book.total_page)
    @staticmethod
    def welcome():
        print('welcome')   
    @staticmethod
    def thanx():
        print(' thanx-bye')     
obj=Book('python','kartikey')        
Book.update(110,550)
Book.welcome()
obj.showdetails()
Book.thanx()




