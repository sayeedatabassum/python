#Creation of multiple objects with same name in python
class Student:
    
    #constructor
    def __init__(self, name, age, average):
        self.name = name
        self.age = age
        self.average = average
        
    #this function prints in output    
    def display(self):
        print(f'Name: {self.name}')
        print(f'Age : {self.age}')
        print(f'Average: {self.average}')

#main method        
if __name__ == '__main__':
    #here 's' is a reference variable 
    s1 = Student('Danish', 25, 76)
    s1.display()
    
    s2 = Student('Ayan', 25, 78)
    s2.display()