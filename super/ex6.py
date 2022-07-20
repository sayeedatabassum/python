#accessing the c,im,sm,cm of parent class using sm of child class

class Parent:
    def __init__(self):
        print('parent class constructor')
        
    def i_m(self):
        print('parent class instance method')
        
    @staticmethod
    def s_m():
        print('parent class sm')
        
    @classmethod
    def c_m():
        print('parent class cm')
        
class Child(Parent):
    # super().__init__()  
    # super().i_m()   
    # super().s_m()   
    # super().c_m()         #--runtime error #outside  method inside class
        
    @staticmethod
    # def c_s_method():     
    # super().__init__()  
    # super().i_m()   
    # super().s_m()   
    # super().c_m()     #runtime error 

if __name__ == '__main__':
    c = Child()
    c.c_s_method()
            
            
# o/p:
# runtime error

# using sm of cc we cannot access any attribute of parent class
# we cannot access c, im,sm,cm of parent class using sm of child class