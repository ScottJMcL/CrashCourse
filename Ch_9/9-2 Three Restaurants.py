'''
Three Restaurants: Start with your class from Exercise 9-1 . Create three 
different instances from the class, and call describe_restaurant() for each 
instance .
'''

class Restaurant():

    def __init__(self, restaurant_name,cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        print(f'\nOur restaurant is {self.name} and serves {self.cuisine} food.')
    
    def open_restaurant(self):
        print(f'\n{self.name} is now open! Come in for the best {self.cuisine} food in town!')
    

restaurant = Restaurant("Gaelfs", "Elven")

Bobs_Universe = Restaurant("Bob's Universe", "virtual")
GreenRoom = Restaurant("RreegRoom", "American")
Initea = Restaurant("Initea", "Boba Tea")

Bobs_Universe.describe_restaurant()
GreenRoom.describe_restaurant()
Initea.describe_restaurant()

