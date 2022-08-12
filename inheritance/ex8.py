<<<<<<< HEAD
#Multiple level inheritance

class Father:
    #specialized method
    def order(self):
        print('Father order')
        
class Mother:
    #specialized method
    def order(self):
        print('Mother')

class Child(Father, Mother):
        pass
        
if __name__ == '__main__':
    c = Child()     #creating child object
    c.order()

# o/p:
=======
#Multiple level inheritance

class Father:
    #specialized method
    def order(self):
        print('Father order')
        
class Mother:
    #specialized method
    def order(self):
        print('Mother')

class Child(Father, Mother):
        pass
        
if __name__ == '__main__':
    c = Child()     #creating child object
    c.order()

# o/p:
>>>>>>> 247dc86db755a35d94ee3603e150aa5a53c0b736
# Father order