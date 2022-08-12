<<<<<<< HEAD
#Hierarchical level inheritance

class Parent:
    #specialized method
    def m1(self):
        print('Parent class method')
        
class Child1(Parent):
    #specialized method
    def m2(self):
        print('Child1 class method')

class Child2(Parent):
    #specialized method
    def m3(self):
        print('Child2 class method')
        
if __name__ == '__main__':
    c1 = Child1()     #creating child object
    #c1.m3()      Attribute error
    c1.m2()      #calling specialized method of child1 class
    c1.m1()      #calling specialized method of parent class
    
    c2 = Child2()     #creating child object
    c2.m3()      #calling specialized method of child2 class
    #c2.m2()     Attribute error
    c2.m1()      #calling specialized method of parent class


# o/p:
# Child1 class method
# Parent class method
# Child2 class method
=======
#Hierarchical level inheritance

class Parent:
    #specialized method
    def m1(self):
        print('Parent class method')
        
class Child1(Parent):
    #specialized method
    def m2(self):
        print('Child1 class method')

class Child2(Parent):
    #specialized method
    def m3(self):
        print('Child2 class method')
        
if __name__ == '__main__':
    c1 = Child1()     #creating child object
    #c1.m3()      Attribute error
    c1.m2()      #calling specialized method of child1 class
    c1.m1()      #calling specialized method of parent class
    
    c2 = Child2()     #creating child object
    c2.m3()      #calling specialized method of child2 class
    #c2.m2()     Attribute error
    c2.m1()      #calling specialized method of parent class


# o/p:
# Child1 class method
# Parent class method
# Child2 class method
>>>>>>> 247dc86db755a35d94ee3603e150aa5a53c0b736
# Parent class method