class Student:
    
    #self is 1st parameter in both constructor and instance method
    #it is a region where address of self variable is stored
    #instead of self u can also use any name
    
    #constructor
    def __init__(sayeeda, name, age, average):
        sayeeda.name = name
        sayeeda.age = age
        sayeeda.average = average
        #address of self
        print(id(sayeeda))
    
#main function    
if __name__ == '__main__':
    #here 's' is a reference variable 
    s1 = Student('Danish', 25, 76)
    print(id(s1))