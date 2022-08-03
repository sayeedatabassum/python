class Dog:
    def sounds(self):
        print('bow bow....')
        
class Cat:
    def sounds(self):
        print('meow meow....')
        
class Duck:
    def sounds(self):
        print('Quack quack....')
        
if __name__ == '__main__':
    def call_instance_method(objectreference):
        objectreference.sounds()
        animal = [Dog(), Cat(), Duck()]
        
        for objectreference in animal:
            call_instance_method(objectreference)