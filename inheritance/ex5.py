<<<<<<< HEAD
#single level inheritance

class Parent:
    #specialized method
    def m1(self):
        print('Parent class method')
        
class Child(Parent):
    #specialized method
    def m2(self):
        print('Child class method')
        
if __name__ == '__main__':
    c = Child()     #creating child object
    c.m2()      #calling specialized method of child class
    c.m1()      #calling specialized method of parent class
    
    
# o/p:
#     Child class method
=======
#single level inheritance

class Parent:
    #specialized method
    def m1(self):
        print('Parent class method')
        
class Child(Parent):
    #specialized method
    def m2(self):
        print('Child class method')
        
if __name__ == '__main__':
    c = Child()     #creating child object
    c.m2()      #calling specialized method of child class
    c.m1()      #calling specialized method of parent class
    
    
# o/p:
#     Child class method
>>>>>>> 247dc86db755a35d94ee3603e150aa5a53c0b736
# Parent class method