'''
Day 41 05/10/26

OOP --> Encapsulation --> It is one of the key features of OOP,it binds(bundles) the
data (attributes) and methods (ctions) aroun a single class.It also provides sepcific accessibility
as Public,Protected and Private Attributes.

Let's understand in details about each one in detail

Public Attributes --> These are defined inside the class and can be modified
outside the class.

class Users:
    """Users data"""
    def __init__(self,name):
        self.name = name #public attribute
    def details(self):
        print(f'User name is {self.name}')

u1 = Users("Samitha")
u1.details()
print(u1.name)
u1.name = "Hemitha" #Modifying public attribute
u1.details()

#Protected Attribute :This is generally preferred in Developer Point of view
#as a hint,we generally use single underscore before the attribute,they can
#also be nmodified outside the class
class Users:
    """Users data"""
    def __init__(self,name,_otp):
        self.name = name #public attribute
        self._otp = _otp #protected attribute
    def details(self):
        print(f'User name is {self.name}')
u1 = Users("Samitha",8745)
print(u1._otp)
u1._otp = 3425
print(u1._otp)


#private Attribute --> In this case we make the attribute name with double
#leading underscores,in very specific where the attribute need not be accessed
#directtly such as we make it as __var
#Python breaches it by Name Mangling,but we prefer usafe of Setters and Getters
#Accessors/Modifiers

class Users:
    """Users data"""
    def __init__(self,name,_otp,__password):
        self.name = name #public attribute
        self._otp = _otp #protected attribute
        self.__password = __password #private attribute
    def details(self):
        print(f'User name is {self.name}')
u1 = Users("Samitha",4523,"sam@123")
print(u1.name)
print(u1._otp)
#print(u1.__password)#it raises Attribute Error as we made it Private
print(u1._Users__password) #Here NameMangling is used as we can access
#private attribute by classname with leading underscore usage...

#As NameMangling is not recommended approach we make use of Accessors and
#Modifiers in Python


class Users:
    """Users data"""
    def __init__(self,name,_otp,__password):
        self.name = name #public attribute
        self._otp = _otp #protected attribute
        self.__password = __password #private attribute
    #To make use of private attributes (getter method)
    def get_password(self):
        #return "******"
        return self.__password
    #Now to modify the password (setter method)
    def set_password(self,new_password):
        if len(new_password) >=6:
            self.__password = new_password
            print("Password is Updated")
        else:
            print("Make sure to have password with min 6 characters")
    def details(self):
        print(f'User name is {self.name}')
u1 = Users("Samitha",5423,"samit")
print(u1.get_password())
(u1.set_password("samit2"))
print(u1.__dict__)#now password is updated for u1 User
u2 = Users("Hemi",2345,"asdfgef")
print(u2.get_password())
u2.set_password("qwer") #it wii not be updated as we are not matching criteria
print(u2.get_password())
'''


#So we prefer usage of Accessors and Modifiers in case of Private attributes
#to access and modify the data ,we can also use it for Protected Attributes.

#Task : Use Getter and Setter methods for both Protected and private
#attributes (take a new scenario),additionally u can also have Public attributes

#Inheritance --> Single Inheritance,Multiple Inheritance,Multilevel Inheritance
#Hierarchical Inheritance,Hybrid Inheitance
#Inheritance --> It is one of the key features of OOP,which heps in
#acquiring or reusing the properties (attributes,methods) from one class
#to another class
'''

class Base_class:  #Parent class
    statement(s)...
    .........
class Derived_Class(Base_class): #Derived --> Child class
    statement(s)...
    .........
'''
'''
#Single Inheritance -->FingerPrint
Class A:
    statement(s)....
    .........
class B(A):
    statement(s)....
    .........
'''

'''
#let's take example of Social Media Login
class Users:
    """Users details"""
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    #initial case we just display
    def full_name(self):
        return self.fname + self.lname
#u1 = Users("samitha","rao")
#print(u1.full_name())
'''
'''
class User_v1(Users):
    pass #this is like placeholder (only for syntax)'''
'''
class User_v2(Users):
    """Updating username"""
    def update_name(self):
        return self.fname.title().strip()+" "+self.lname.title().strip()
u1 = User_v2("samitha","     rao")
print(u1.full_name())
print(u1.update_name())

#using Single inheritance we will make use of Class Attributes and Classmethods
#along with the importance of super() (Constructor Overriding/Method Overriding)
'''

#Task : Use Getter and Setter methods for both Protected and private
#attributes (take a new scenario),additionally u can also have Public attributes

class Employees:
    """Employee data"""
    def __init__(self, name, _emp_id, __salary):
        self.name = name #public attribute
        self._emp_id = _emp_id #protected attribute
        self.__salary = __salary #private attribute

    #To make use of private attributes (getter method)
    def get_salary(self):
        return self.__salary
    #Now to modify the salary (setter method)
    def set_salary(self, new_salary):
        if new_salary >= 10000:
            self.__salary = new_salary
            print("Salary is Updated")
        else:
            print("Salary should be minimum 10000")
    def details(self):
        print(f'Employee name is {self.name}')


e1 = Employees("Samitha", 101, 25000)
print(e1.get_salary())
e1.set_salary(30000)
print(e1.__dict__) #Now salary is updated for e1 Employee
e2 = Employees("Hemi", 102, 18000)
print(e2.get_salary())
e2.set_salary(5000) #It will not be updated as it does not match the criteria
print(e2.get_salary())







