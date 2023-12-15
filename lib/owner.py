# Stretch Goal: Build Out Corresponding Owner Class Methods
from pet import Pet
class Owner:

    def __init__(self, name, phone="", email=""):
        self.name = name 
        self.phone = phone 
        self.email = email 

    #✅ 3. create relationship: owner has many pets
    def pets(self):
    # let owner, return array of pets that match owner's name 
    # loop through all pets
    # CHECK PET.OWNER AGAINST SELF - TAKES INTO ACCOUNT THE ENTIRETY OF THE INSTANCE, NOT JUST ONE RANDOM ATTRIBUTE

        pets = [] 
        for pet in Pet.all:
            if pet.owner == self:
                pets.append(pet)

        return [pet for pet in Pet.all if pet.owner == self]


    def __repr__(self):
        return f'''<Owner {self.name} >'''
    
    #✅ 9. create a function for the total bill of the owner
    #✅ 9a. create helper method for all appointments of owner (owner has many appointments through pets)
    #owner's pet (self.pets)
    #all of the appointments (in Pet class)
    def owner_appointments(self):
        apps = []
        for pet in self.pets():
            apps = apps + pet.appointments()
        return apps
    #all of the procedures (in Appointment class)
    def owner_procedures(self):
        procs = []
        #loop through all owner_appointments
        for app in self.owner_appointments():
            #add appointments.proc to list
            procs.append(app.proc)
        return procs 
    #price of a procedure (in Procedure class)
    def total_bill(self):
        total = 0
        for proc in self.owner_procedures():
            total += proc.price 
        return total
    
    # Owner.pet -> Pet.appointments() -> Appointments.proc -> Procedure.price
    # - what connections do I have to each class
    # - how do I access those connections (.all or .some_attribute or some_method())
    # - do I need to create any other connections

    