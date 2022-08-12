<<<<<<< HEAD
#accessing attribute of parent class using child class object reference
class Parent:
    a=10 #static variable
    
    #constructor executes 1st always
    def __init__(self):
        print('Inside parent class Constructor')
        self.b = 20 #Instance Variable
    
    def i_m(self):
        print('Inside parent class im')
        
    @staticmethod
    def s_m():
        print('inside parent class sm')
        
    @classmethod
    def c_m(cls):
        print('inside parent class cm')
        
class Child(Parent):
    pass

if __name__ == '__main__':
    c = Child()
    print(f' Accessing the sv of parent class: {Child.a}') #using child class
    print(f' Accessing the sv of parent class: {Parent.a}') #using parent class
    print(f' Accessing the iv of parent class: {c.b}') #using child class obj ref
    c.i_m()
    c.s_m()
    c.c_m()
   
#    o/p: 
# Inside parent class Constructor
#  Accessing the sv of parent class: 10
#  Accessing the sv of parent class: 10
#  Accessing the iv of parent class: 20
# Inside parent class im
# inside parent class sm
=======
#accessing attribute of parent class using child class object reference
class Parent:
    a=10 #static variable
    
    #constructor executes 1st always
    def __init__(self):
        print('Inside parent class Constructor')
        self.b = 20 #Instance Variable
    
    def i_m(self):
        print('Inside parent class im')
        
    @staticmethod
    def s_m():
        print('inside parent class sm')
        
    @classmethod
    def c_m(cls):
        print('inside parent class cm')
        
class Child(Parent):
    pass

if __name__ == '__main__':
    c = Child()
    print(f' Accessing the sv of parent class: {Child.a}') #using child class
    print(f' Accessing the sv of parent class: {Parent.a}') #using parent class
    print(f' Accessing the iv of parent class: {c.b}') #using child class obj ref
    c.i_m()
    c.s_m()
    c.c_m()
   
#    o/p: 
# Inside parent class Constructor
#  Accessing the sv of parent class: 10
#  Accessing the sv of parent class: 10
#  Accessing the iv of parent class: 20
# Inside parent class im
# inside parent class sm
>>>>>>> 247dc86db755a35d94ee3603e150aa5a53c0b736
# inside parent class cm