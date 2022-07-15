#Creation of objects in python
class Student:
    
    #constructor
    def __init__(self):
        self.name = 'sayeeda'
        self.age = 50
        self.average = 75
        
    #this function prints in output    
    def display(self):
        print(f'Name: {self.name}')
        print(f'Age : {self.age}')
        print(f'Average: {self.average}')

#main method        
if __name__ == '__main__':
    #here 's' is a reference variable 
    s = Student()
    s.display()