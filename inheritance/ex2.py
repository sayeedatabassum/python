<<<<<<< HEAD
class Parent:
    #specialized method
    def m1(self):
        print('Inside instance method of Parent class')
        
class Child(Parent):
    #specialized method
    def m2(self):
        print('Inside instance method of child class')
                
if __name__ == '__main__':
    c = Child() #creation of child object
    c.m1() #calling specialized method of parent class
    c.m2() #calling specialized method of child class
    
# o/p
# Inside instance method of Parent class
=======
class Parent:
    #specialized method
    def m1(self):
        print('Inside instance method of Parent class')
        
class Child(Parent):
    #specialized method
    def m2(self):
        print('Inside instance method of child class')
                
if __name__ == '__main__':
    c = Child() #creation of child object
    c.m1() #calling specialized method of parent class
    c.m2() #calling specialized method of child class
    
# o/p
# Inside instance method of Parent class
>>>>>>> 247dc86db755a35d94ee3603e150aa5a53c0b736
# Inside instance method of child class