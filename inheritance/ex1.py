class Parent:
    def __init__(self):
        print('Inside Parent class')
        
class Child(Parent):
    #inherits the features of parent
    pass
    #default Constructor
    # '''def __init__(self):
    #             Super() __init__()'''
                
if __name__ == '__main__':
    c = Child()