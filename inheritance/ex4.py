<<<<<<< HEAD
class Human:
    Corona_medicine = 'stayhome' #SV
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
class Employee(Human):
    def __init__(self, name, age, company):
        super().__init__(name,age) #calling parent class constructor using super class
        self.company = company
        print(f' name of employee:{self.name}')     #iv
        print(f'employee should {Employee.corona_medicine}')    #sv
        
class Cricketer(Human):
    def __init__(self, name, age, department):
        super().__init__(name, age) #calling parent class constructor using super class
        self.department = department
        print(f' Name of cricketer:{self.name}')    #iv
        print(f' cricketer should {Human.Corona_medicine}') #sv
        
class FootballPlayer(Human):
    def __init__(self, name, age, country):
        super().__init__(name, age) #calling parent class constructor using super class
        self.country = country
        print(f' name of footballPlayer: {self.name}')  #iv
        print(f' footballplayer should {Human.Corona_medicine}')    #sv
        
if __name__ == '__main__':
    e = Employee(name ='suhas', age = 25, company = 'Infosys')
    c = Cricketer(name = 'sachin', age = 42, department = 'batting')
=======
class Human:
    Corona_medicine = 'stayhome' #SV
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
class Employee(Human):
    def __init__(self, name, age, company):
        super().__init__(name,age) #calling parent class constructor using super class
        self.company = company
        print(f' name of employee:{self.name}')     #iv
        print(f'employee should {Employee.corona_medicine}')    #sv
        
class Cricketer(Human):
    def __init__(self, name, age, department):
        super().__init__(name, age) #calling parent class constructor using super class
        self.department = department
        print(f' Name of cricketer:{self.name}')    #iv
        print(f' cricketer should {Human.Corona_medicine}') #sv
        
class FootballPlayer(Human):
    def __init__(self, name, age, country):
        super().__init__(name, age) #calling parent class constructor using super class
        self.country = country
        print(f' name of footballPlayer: {self.name}')  #iv
        print(f' footballplayer should {Human.Corona_medicine}')    #sv
        
if __name__ == '__main__':
    e = Employee(name ='suhas', age = 25, company = 'Infosys')
    c = Cricketer(name = 'sachin', age = 42, department = 'batting')
>>>>>>> 247dc86db755a35d94ee3603e150aa5a53c0b736
    f = FootballPlayer(name = 'messi', age = 32, country = 'Argentina')