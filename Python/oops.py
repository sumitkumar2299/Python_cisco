# oops in python 

# class: blueprint for creating objects.
# object: instance of an class 


class dog:
    def __init__(self,name):
        self.name = name
    
    def bark(self):
        print(f'{self.name} says woof');

dog1 = dog("buddy")
dog1.bark();




class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    
    def start(self):
        print(f"{self.brand} {self.model} is starting...")


# objects

car1 = Car("toyota","innova")
car2 = Car("tata","nexon")
# output : toyota innova is starting...
car1.start(); 
# output:tata nexon is starting...
car2.start() 

    

        
        