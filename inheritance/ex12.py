<<<<<<< HEAD
#mro
class D:
    pass
        
class E:
    pass
        
class F:
    pass
        
class B(D, E):
    pass

class C(D, F):
    pass

class A(B, C):
    pass
        
if __name__ == '__main__':
    print(A.mro())  

# o/p
# [<class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.D'>, <class '__main__.E'>, <class '__main__.F'>, <class 'object'>]
=======
#mro
class D:
    pass
        
class E:
    pass
        
class F:
    pass
        
class B(D, E):
    pass

class C(D, F):
    pass

class A(B, C):
    pass
        
if __name__ == '__main__':
    print(A.mro())  

# o/p
# [<class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.D'>, <class '__main__.E'>, <class '__main__.F'>, <class 'object'>]
>>>>>>> 247dc86db755a35d94ee3603e150aa5a53c0b736
