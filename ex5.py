<<<<<<< HEAD
#Creation of multiple objects with same reference in python
class Student:
    
    #self is 1st parameter in both constructor and instance method
    #it is a region where address of self variable is stored
    
    #constructor
    def __init__(self, name, age, average):
        self.name = name
        self.age = age
        self.average = average
        
    #instance method and this function prints in output    
    def display(self):
        print(f'Name: {self.name}')
        print(f'Age : {self.age}')
        print(f'Average: {self.average}')

#main function    
if __name__ == '__main__':
    #here 's' is a reference variable 
    s1 = Student('Danish', 25, 76)
    s1.display()
    
    s1 = Student('Ayan', 25, 78)
=======
#Creation of multiple objects with same reference in python
class Student:
    
    #self is 1st parameter in both constructor and instance method
    #it is a region where address of self variable is stored
    
    #constructor
    def __init__(self, name, age, average):
        self.name = name
        self.age = age
        self.average = average
        
    #instance method and this function prints in output    
    def display(self):
        print(f'Name: {self.name}')
        print(f'Age : {self.age}')
        print(f'Average: {self.average}')

#main function    
if __name__ == '__main__':
    #here 's' is a reference variable 
    s1 = Student('Danish', 25, 76)
    s1.display()
    
    s1 = Student('Ayan', 25, 78)
>>>>>>> 247dc86db755a35d94ee3603e150aa5a53c0b736
    s1.display()