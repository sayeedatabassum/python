class Parent:
    a = 10     #sv
    
    def __init__(self):
        self.b = 20     #IV available in parent class constructor
        
class Child(Parent):
    a = 888     #SV
    
    def __init__(self):
        super().__init__()        #calling parent class constructor using super()
        print(super().a)    #calling variable using super()   #--10               
        # print(super().b)    #attribute error    
        
        print(Child.a)   #--888
        print(self.a)   #---888       
        print(Parent.a) #---10  
        print(self.b)   #---20s
                            
if __name__ == '__main__':
    c = Child()
    
# using super() we cannot access the iv of parent class (attribute error), however we can access the sv
        