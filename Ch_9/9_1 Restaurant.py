

class Restaurant():
    '''
    9-1. Restaurant: Make a class called Restaurant . The __init__() method for 
    Restaurant should store two attributes: a restaurant_name and a cuisine_type . 
    Make a method called describe_restaurant() that prints these two pieces of 
    information, and a method called open_restaurant() that prints a message indi- 
    cating that the restaurant is open .
    Make an instance called restaurant from your class . Print the two attributes 
    individually, and then call both methods .
    '''

    def __init__(self, restaurant_name,cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        print(f'\nOur restaurant is {self.name} and serves {self.cuisine} food.')
    
    def open_restaurant(self):
        print(f'\n{self.name} is now open! Come in for the best {self.cuisine} food in town!')
    

restaurant = Restaurant("Gaelfs", "Elven")

print(f'The new restaurant is called {restaurant.name} and serves {restaurant.cuisine} food.')

restaurant.describe_restaurant()
restaurant.open_restaurant()