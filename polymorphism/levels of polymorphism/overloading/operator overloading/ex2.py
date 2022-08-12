<<<<<<< HEAD
class Book:
    def __init__(self,pages):
        self.pages = pages
        
if __name__ == '__main__':
    b1 = Book(pages = 200)
    b2 = Book(pages = 100)
    
    print(b1)   #address of book1
    print(b2)   #address of book2
    
#print(b1 + b2) -> Type error: Unsupported  operand type(5) for + : 'Book' and 'Book'

=======
class Book:
    def __init__(self,pages):
        self.pages = pages
        
if __name__ == '__main__':
    b1 = Book(pages = 200)
    b2 = Book(pages = 100)
    
    print(b1)   #address of book1
    print(b2)   #address of book2
    
#print(b1 + b2) -> Type error: Unsupported  operand type(5) for + : 'Book' and 'Book'

>>>>>>> 247dc86db755a35d94ee3603e150aa5a53c0b736
    print(b1.pages + b2.pages)  #300