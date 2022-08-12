<<<<<<< HEAD
#Accessing c,im,is,sm,cm of parent class within child class outside class

class Parent:
    def __init__(self):
        print('Parent class constuctor')
        
    def i_m(self):
        print('parent class im')
        
    @staticmethod
    def s_m():
        print('parent class sm')
        
    @classmethod
    def c_m(cls):
        print('parent class cm')
        
class Child(Parent):
    
    def c_i_m(self):
        super().__init__()  #Parent class Constructor
        super().i_m()   #parent class im
        super().s_m()   #parent class sm
        super().c_m()   #parent class cm
        
if __name__ == '__main__':
    c = Child()
    c.c_i_m()
 
# O/p:   
# Parent class constuctor
# Parent class constuctor
# parent class im
# parent class sm
# parent class cm

# we can access c,im,sm,cm of parent class using im of child class
=======
#Accessing c,im,is,sm,cm of parent class within child class outside class

class Parent:
    def __init__(self):
        print('Parent class constuctor')
        
    def i_m(self):
        print('parent class im')
        
    @staticmethod
    def s_m():
        print('parent class sm')
        
    @classmethod
    def c_m(cls):
        print('parent class cm')
        
class Child(Parent):
    
    def c_i_m(self):
        super().__init__()  #Parent class Constructor
        super().i_m()   #parent class im
        super().s_m()   #parent class sm
        super().c_m()   #parent class cm
        
if __name__ == '__main__':
    c = Child()
    c.c_i_m()
 
# O/p:   
# Parent class constuctor
# Parent class constuctor
# parent class im
# parent class sm
# parent class cm

# we can access c,im,sm,cm of parent class using im of child class
>>>>>>> 247dc86db755a35d94ee3603e150aa5a53c0b736
