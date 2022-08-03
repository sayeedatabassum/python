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
# Parent class method