
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
        super().m1()    #D class method
        
        super(C,self).m1()  #B class method
        super(D,self).m1()  #C class method
        
        A.m1(self)  #A class method
        B.m1(self)  #B class method
        
if __name__ == '__main__':
    e = E()
    e.m1()
    
# o/p:
# D class method
# B class method
# C class method
# A class method 
# B class method

#syntax: super(cn,self).method
# --super(B,self).m1() method of Super class of B is " class A"

# syntax:   cn.method(self)
# --A.m1(self)
# it will call A class m1() method

