# Sequence Types
# docs: 
# https://docs.python.org/3/tutorial/datastructures.html
import ipdb

#lists, tuples, dictionaries, and sets are all individual data types that are used to store collections of data.  they each have their own unique properties/behaviors.  a lot of those behaviors overlap

# Creating Lists
#✅ 1. Create a list of 10 pet names
villains = ["Bane", "Joker", "Angelica", "Shark", "Asteroids", "Loki", "Dinosaurs", "Tom"]

#------------------------ Reading Information from Lists
#✅ 1a. Return the first pet name 
villains[0] #Bane

#✅ 1b. Return the last value
villains[-1] #Tom  
villains[-2] #Dinosaurs

#✅ 1c. Return all pet names beginning from the 3rd index
#inclusive (3, end]
villains[3:] #omitted value refers to end of list

#✅ 1d. Return all pet names before the 3rd index
#exclusive [start, 3)
villains[:3] #bane, joker, angelica 

#✅ 1e. Return all pet names beginning from the 3rd index and up to (exclusive of) the 7th
villains[3:7]

#✅ 1f. Find the index of a given element
villains.index("Shark") #3

#✅ 1g. Reverse the original list
# mutate our list, destructive
# does not return anything
villains.reverse()

villains = ["Bane", "Joker", "Angelica", "Shark", "Asteroids", "Loki", "Dinosaurs", "Tom", "Joker", "Joker"]


#✅ 1h. Return the frequency of a given element 
villains.count("Joker") #3

#---------------------------------- Updating Lists
#✅ 1i. Change the first element to all uppercase
villains[0] = villains[0].upper() #BANE

#---------------------------------- Adding items to list
#✅ 1j. Append a new name to the list
#mutates list
villains.append("Godzilla")

#✅ 1k. Add a new name at a specific index
villains.insert(0, "Hades") #front of list 
villains.insert(1, "Thanos") #moves everything else over 
villains.insert(-2, "Ursula")


heroes = ["Hercules", "Jerry", "Batman"]

#✅ 1l. Add two lists together 
villains_and_heroes = villains + [heroes]

#---------------------------------- Removing 
#✅ 1m. Removes and returns the final element from the list
villains.pop() #Godzilla 

#✅ 1n. Remove element by specific index
villains.pop(3) #Joker

#✅ 1o. Remove a the first instance of a specific element 
villains.remove("Joker") #last Joker is still in list

#✅ 1p. Remove all pet names from the list
villains.clear()

#---------------------------------- Tuple 
# can't mutate tuples
# can have repeats
#🛑 Using a trailing comma for a singleton tuple: a, or (a,)
#✅ 2. Create a Tuple of pet 10 ages 
numbers = (3, 2, 6, 43, 7, 2, 3, 73, 5)



#✅ 2a. Print the first pet age
numbers[0] #3

#---------------------------------- Testing Changeability 
#✅ 2b. Attempt to remove an element with .pop (should error)
#numbers.pop()
#our attribute, pop(), happens to be a method
#AttributeError: 'tuple' object has no attribute 'pop'

#✅ 2c. Attempt to change the first element (should error)
#numbers[0] = 10
#TypeError: 'tuple' object does not support item assignment

#---------------------------------- Tuple Methods
#✅ 2d. Return the frequency of a given element
numbers.count(3) #2

#✅ 2e. Return the index of first matching element 
numbers.index(43) #3

#---------------------------------- Demo Sets
#✅ 3. Create a set of 3 pet foods
food_list = ['pasta', 'pasta', 'pasta', 'bread', 'cheese']
foods_from_list = set(food_list)
foods = {"pasta", "bread", "cheese"}



# Demo Dictionaries 
#---------------------------------- Creating 
#✅ 4. Create a dictionary of pet information with the keys name, age and breed
# KEYS AS STRINGS KEYS AS STRINGS 
hero_vil = {
    'thanos': 'guardians',
    'hades': 'hercules', 
    'tom': 'jerry', 
    'asteroid': 'humanity'
}

#✅ 4a.  Use dict to create a dictionary of pet information with the keys name, age and breed
hero_vil_from_constructor = dict(thanos='guardians', hades='hercules', asteroid='humanity')

#---------------------------------- Reading
#✅ 4b. Print the pet attribute of name using bracket notation
hero_vil['thanos'] #guardians
#if pair does not exist: *** KeyError: 'sldkfj'

#✅ 4c. Print the pet attribute of age using .get
hero_vil.get('thanos')
#if pair does not exist nothing happens

#---------------------------------- Updating 
#✅ 4d. Update the pets age to 12
hero_vil['asteroid'] = 'earth'

#✅ 4e. Update the other pets age to 26
hero_vil.update({'hades': 'people'})

#---------------------------------- Deleting
#✅ 4f. Delete a pets age using the del keyword 
del hero_vil['asteroid'] #returns nothing

#✅ 4g. Delete the other pets age using the .pop, returns removed value
hero_vil.pop('thanos') #returns 'guardians', deletes key value pair

#✅ 4h. Delete the last item in the pet dictionary using popitem()
hero_vil.popitem() #('tom', 'jerry'), both key/value

#---------------------------------- Demo Loops 
pet_info = [
    {
        'name':'rose',
        'age':11,
        'breed': 'domestic long-haired',
    }, 
    {
        'name':'spot',
        'age':25,
        'breed': 'boxer',
    },
    {
        'name':'Meow Meow Beans',
        'age':2,
        'breed': 'domestic long-haired',
    }
]
#✅ 5. loop through a range of 10 and print every number within the range

#✅ 5a. loop through a range between 50 and 60 that iterates by 2 and print every number

#✅ 5b. Loop through the pet_info list and print every dictionary  

#✅ 6. Create a function that takes a list as an argument. 
    # The function should use a for loop to loop through the list and print every item in the list 
    # Invoke the function and pass it pet_names as an argument

#✅ 7. Create a function that takes a list as an argument.(simple example) 
    # The function should define a counter and set it to 0
    # Create a while loop 
        # The loop will continue as long as the counter is less than the length of the list
        # Every loop should increase the count by 1
    # return the counter 

#✅ 8. Create a function that updates the age of a given pet
        # The function should take a list of dicts, name and age as parameters 
        # Create a index variable and set it to 0
        # Create a while loop. 
            # The loop will continue so long as the list does not contain a name matching the name param and the index is less then the length of the list
            # Every list will increase the index by 1
        # If the dict containing a matching name is found update the items age with the new age 
        # else return 'pet not found'

# map like 
#✅ 9. Use list comprehension to return a list containing every pet name from pet_info changed to uppercase

# find like
#✅ 9a. Use list comprehension to find a pet named spot

# filter like
#✅ 9b. Use list comprehension to find all of the pets under 3 years old

#✅ 9c. Create a generator expression matching the filter above. Compare and contrast the generator to the list comprehension. 
