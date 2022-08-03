# Accessing the cm, im, sm, cm of parent class using cm of child class

from distutils import ccompiler


class Parent:
    
    a = 100
    def __init__(self):
        print('parent class constructor')
        
    def i_m(self):
        print('parent class im')
        
    @staticmethod
    def s_m():
        print('parent class sm')
        
    @classmethod
    def c_m(cls):
        print('parent class cm')
        
class Child(Parent):
    @classmethod
    def c_c_m(cls):
        #super().__init__() #--type error
        #super().i_m()  #--type error
        super().s_m()
        print(super().a)
        
if __name__ == '__main__':
    c = Child()
    c.c_c_m()
    
# o/p:
# parent class constructor
# parent class sm
# 100

# we cannot access c,im using cm in cc (type error), we can access am and cm using super