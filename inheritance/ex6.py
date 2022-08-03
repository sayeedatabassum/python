#multi level inheritance

class Grandparent:
    #specialized method
    def m1(self):
        print('Grandparent class method')
        
class Parent(Grandparent):
    #specialized method
    def m2(self):
        print('Parent class method')
        
class Child(Parent):
    #specialized method
    def m3(self):
        print('Child class method')
        
if __name__ == '__main__':
    c = Child()     #creating child object
    c.m3()      #calling specialized method of child class
    c.m2()      #calling specialized method of Parent class
    c.m1()      #calling specialized method of Grandparent class
    
    
# # o/p:
# #Child class method
# Parent class method
# Grandparent class method