<<<<<<< HEAD
#mro

class A:
    pass
        
class B:
    pass
        
class C:
    pass
        
class X(A, B):
    pass

class Y(B, C):
    pass

class P(X, Y, C):
    pass
        
if __name__ == '__main__':
    print(P.mro())  

# o/p
=======
#mro

class A:
    pass
        
class B:
    pass
        
class C:
    pass
        
class X(A, B):
    pass

class Y(B, C):
    pass

class P(X, Y, C):
    pass
        
if __name__ == '__main__':
    print(P.mro())  

# o/p
>>>>>>> 247dc86db755a35d94ee3603e150aa5a53c0b736
# [<class '__main__.P'>, <class '__main__.X'>, <class '__main__.A'>, <class '__main__.Y'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>]