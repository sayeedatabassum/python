class Parent:
    a = 10     #sv
    
    def __init__(self):
        self.b = 20     #IV available in parent class constructor
        
class Child(Parent):
    a = 888     #SV
    
    def __init__(self):
        super().__init__()        #calling parent class constructor using super()
        print(self.b)               #--20
        
        print(self.a)               #--888
        
        self.b = 40 
        print(self.b)               #--40
        
        self.a = 999                
        print(self.a)               #--999
        
        print(Child.a)              #--888
        
if __name__ == '__main__':
    c = Child()
        
 # if iv and sv are in same name, then using self if we try to access then iv data would be fetched
