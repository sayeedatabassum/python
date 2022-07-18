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
# Father order