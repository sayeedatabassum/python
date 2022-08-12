<<<<<<< HEAD
#SUPER
#super can be used to call the present class variables, methods and constructor from child class

class Parent:
    a = 10
    
    def __init__(self):
        self.b = 20 #IV of parent class constructor
        
class Child(Parent):
    a = 888     #SV
    
    def __init__(self):
        print(self.a)   #--888
        # print(self.b)   #attribute error bcz parent cl constructor is not called
        self.b = 999
        print(self.b)   #--999
        
if __name__ == '__main__':
    c = Child()
    
# class obj isn't created so cannot access iv of parent class 
=======
#SUPER
#super can be used to call the present class variables, methods and constructor from child class

class Parent:
    a = 10
    
    def __init__(self):
        self.b = 20 #IV of parent class constructor
        
class Child(Parent):
    a = 888     #SV
    
    def __init__(self):
        print(self.a)   #--888
        # print(self.b)   #attribute error bcz parent cl constructor is not called
        self.b = 999
        print(self.b)   #--999
        
if __name__ == '__main__':
    c = Child()
    
 # class obj isn't created so cannot access iv of parent class 
>>>>>>> 247dc86db755a35d94ee3603e150aa5a53c0b736
