class Dog:
    def bark(self):
        print('bow bow....')
        
class Cat:
    def talk(self):
        print('meow meow....')
        
class Duck:
    def sounds(self):
        print('Quack quack....')
        
if __name__ == '__main__':
    def call_instance_method(objectreference):
        objectreference.bark()
        
        animal = [Dog(), Cat(), Duck()]
        
        for objectreference in animal:
            call_instance_method(objectreference)