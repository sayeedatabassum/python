#Hybrid inheritance

class A:
    def m1(self):
        print('class A method')
        
class B(A):
    def m1(self):
        print('class B method')
        
class C(A):
    def m1(self):
        print('class C method')
        
class D(B, C):
    def m1(self):
        print('class D method')
        
if __name__ == '__main__':
    #mro is method resolution order, it's mro algorithm (DLR)
    d = D()
    d.m1()  # class D method
    print(D.mro()) #[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
    print(B.mro())  #[<class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
    print(A.mro())  #[<class '__main__.A'>, <class 'object'>]

# o/p
# class D method
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]