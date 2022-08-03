class Dog:
    def bark(self):
        print('bow bow....')
        
class Cat:
    def talk(self):
        print('meow meow....')
        
class Duck:
    def sound(self):
        print('Quack quack....')
        
if __name__ == '__main__':
    def call_instance_method(objectreference):
        if hasattr(objectreference,'bark'):
            objectreference.bark()
        
        elif hasattr(objectreference,'talk'):
            objectreference.talk()
        else:
            objectreference.sound()
            
        animal = [Dog(), Cat(), Duck()]
        
        for objectreference in animal:
            call_instance_method(objectreference)