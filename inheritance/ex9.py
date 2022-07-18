#Cyclic level inheritance

class Parent(Child):
    pass

class Child(Parent):
    pass

if __name__ == '__main__':
    c = Child()
    # p = Parent()
    
# o/p
# Name error