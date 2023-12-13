#!/usr/bin/env python3
# Class Attributes and Methods 
import ipdb
#✅ 5. Import the pet and cat class to use in debug.py
class Pet:
    #✅ 6. Keep track of the total number of Pets created
    #✅ 6a. Create a class attribute
    total_pets = 0

    def __init__(self, name, age, breed="", temperament="", image_url=""):
        self.name = name
        self.age = age
        self.breed = breed
        self.temperament = temperament
        self.image_url = image_url
        #✅ 6b. Update class attribute whenever an instance is initialized
        #Pet.total_pets += 1        
        Pet.increase_pets() 
        #✅ 6c. Create a class method increase_pets that will increment total_pets
    
    @classmethod
    def increase_pets(cls): #cls refers to THIS entire class 
        cls.total_pets += 1 #cls.total_pets OR Pet.total_pets 

    #create property
    @property 
    def name(self):
        return self._name 
    #create property's getter 
    @name.getter
    def name(self):
        return self._name 
    #create property's setter 
    @name.setter 
    def name(self, val):
        if(isinstance(val, str)):
            self._name = val 
        else: 
            print("name must be string")

    def print_pet_details(self):
        print(f'''
            name:{self.name}
            age:{self.age}
            breed:{self.breed}
            temperament:{self.temperament}
            image_url:{self.image_url}
        ''')

#create instances here so I don't have to keep recreating them every time I enter ipdb

