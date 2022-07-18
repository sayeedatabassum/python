#accessing c,im,is,cm of parent class using constructor of child class

class Parent:
    def __init__(self):
        print('Parent class Constructor')
        
    def  i_m(self):
        print('parent class im')
        
    @staticmethod
    def s_m():
        print('parent class sm')
        
    @classmethod
    def c_m(cls):
        print('parent class cm')
        
class Child(Parent):
    def __init__(self):
        super().__init__()  #Parent class Constructor
        super().i_m()   #parent class im
        super().s_m()   #parent class sm
        super().c_m()   #parent class cm
        
if __name__ == '__main__':
    c = Child()