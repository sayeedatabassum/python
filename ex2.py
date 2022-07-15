class Cricketer:
    def __init__(self, name, age, average):
        self.name = name
        self.age = age
        self.average = average
        
    #this function prints in output    
    def display(self):
        print(f'Name: {self.name}')
        print(f'Age : {self.age}')
        print(f'Average: {self.average}')
        
if __name__ == '__main__':
    C =Cricketer('Sayeeda', 50, 50.6)
    C.display()