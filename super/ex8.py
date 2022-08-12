<<<<<<< HEAD

class A:
    def m1(self):
        print ('A class method')
        
class B(A):
    def m1(self):
        print('B class method')
        
class C(B):
    def m1(self):
        print('C class method')

class D(C):
    def m1(self):
        print('D class method')

class E(D):
    def m1(self):
        print('E class method')
        
if __name__ == '__main__':
    e = E()
    e.m1()
    
# o/p:
=======

class A:
    def m1(self):
        print ('A class method')
        
class B(A):
    def m1(self):
        print('B class method')
        
class C(B):
    def m1(self):
        print('C class method')

class D(C):
    def m1(self):
        print('D class method')

class E(D):
    def m1(self):
        print('E class method')
        
if __name__ == '__main__':
    e = E()
    e.m1()
    
# o/p:
>>>>>>> 247dc86db755a35d94ee3603e150aa5a53c0b736
# E class method