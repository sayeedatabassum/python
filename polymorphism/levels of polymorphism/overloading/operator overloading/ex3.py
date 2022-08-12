<<<<<<< HEAD
class Book:
    def __init__(self,pages):
        self.pages = pages
        
    def __add__(self,other):
        return self.pages + other.pages
    
if __name__ == '__main__':
    b1 = Book(pages = 200)
    b2 = Book(pages = 100)
    
    print(b1 + b2)  #operator overloading
    
#o/p
#300
=======
class Book:
    def __init__(self,pages):
        self.pages = pages
        
    def __add__(self,other):
        return self.pages + other.pages
    
if __name__ == '__main__':
    b1 = Book(pages = 200)
    b2 = Book(pages = 100)
    
    print(b1 + b2)  #operator overloading
>>>>>>> 247dc86db755a35d94ee3603e150aa5a53c0b736
