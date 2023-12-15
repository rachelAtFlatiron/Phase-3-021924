#!/usr/bin/env python3
# Class Attributes and Methods 
import ipdb
from appointments import Appointment
class Pet:

    all = []
    
    #✅ 1. create relationship: pet belongs to an owner
    #✅ 2. use chatGPT to create owners and pets in debug.py
    #✅ 2a. create __repr__ function to more easily read output
    def __init__(self, name="", age=0, breed="", owner=None): #owner has default None, because owner is meant to be instance of Owner class
        self.name = name
        self.age = age
        self.breed = breed
        self.owner = owner #an instance of owner class 
         #add new pet to list of all pets
        Pet.all.append(self)
        #self.all.append(self)


    #✅ 5. create relationship: pet has many appointments
    def appointments(self):
        #use Appointment.all
        #find Appointments, where appointment.pet == self
        apps = [] 
        for app in Appointment.all:
            if app.pet == self: 
                apps.append(app)

        return [appointment for appointment 
                in Appointment.all 
                if appointment.pet == self]
    
    #get all doctor's that have worked with current pet (self)
    #to appointments
    def doctors(self):
        doctors = [] 
        for app in self.appointments():
            doctors.append(app.staff)
        #[app.staff for app in self.appointments()]
        return doctors

    #✅ 6. create relationship: pet has many procedures (but make it unique)
    #self -> self.appointments() -> appointments.proc -> proc.name 
    #through appointment to procedures
    def procedures(self):
        procs = [] 
        for appointment in self.appointments():
            procs.append(appointment.proc.name)
        #BELOW IS FOR DEMONSTRATION PURPOSES ONLY
        #turn to set to remove duplicates
        #turn back into list (if you want) 
        return procs
        #[appointment.proc.name for appointment in self.appointments()]



    def print_pet_details(self):
        return(f'''
            name:{self.name}
            age:{self.age}
            breed:{self.breed}
        ''')


    #built in function that you can override to display your instane how you want
    #default is: <__main__.Pet object at 0x1059a0940>
    def __repr__(self):
        return f'''<Pet {self.name} >'''
