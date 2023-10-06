'''
Make a class called User . Create two attributes called first_name and last_name, 
and then create several other attributes that are typically stored in a user 
profile . Make a method called describe_user() that prints a summary of the 
user's information. Make another method called greet_user() that prints a 
personalized greeting to the user .
Create several instances representing different users, and call both methods 
for each user .
'''

class User():
    import random
    def __init__(self, first_name, last_name, email, hair_color, eye_color, user_id):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.hair_color = hair_color
        self.eye_color = eye_color
        self.user_id = user_id
    
    def describe_user(self):
        print(f'\nUser ID: {self.user_id}')
        print(f'Name:  {self.first_name.title()} {self.last_name.title()}\nEmail: {self.email}')
        print(f'Hair: {self.hair_color}\nEyes: {self.eye_color}\n')

    def greet_user(self):
        print(f'\nHello {self.first_name.title()}, how are you today? What lovely {self.eye_color} eyes you have!\n')


henry = User('Henry', 'Argentis', 'H.Arg@jaxis.com', 'brown', 'dark brown', 89)
haerdal = User('haerdal', 'ontis', 'h.ontis@jaxis.com', 'blond', 'blue', 17)
janet = User('janet', 'kent', 'janet.kent@jaxis.com', 'red', 'grey', 39)
maeve = User('Maeve', 'Wiley', 'go_away@jazix.com','black', 'brown', 43)

henry.describe_user()
henry.greet_user()
haerdal.describe_user()
haerdal.greet_user()
janet.describe_user()
janet.greet_user()
maeve.describe_user()
maeve.greet_user()
