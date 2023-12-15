#!/usr/bin/env python3
#✅ import owner, pet, and appointments
from owner import Owner 
from pet import Pet 
from appointments import Appointment
from procedure import Procedure


owner1 = Owner("John Doe", "555-1234", "john@example.com")
owner2 = Owner("Alice Smith", "555-5678", "alice@example.com")
owner3 = Owner("Bob Johnson", "555-9876", "bob@example.com")
owner4 = Owner("Eva Williams", "555-4321", "eva@example.com")
owner5 = Owner("Charlie Brown", "555-8765", "charlie@example.com")
owner6 = Owner("Charlie Brown", "000-0000", "charlie@example.com")

pet1 = Pet("Buddy", 3, "Golden Retriever", owner2)
pet2 = Pet("Max", 2, "German Shepherd", owner2)
pet3 = Pet("Luna", 5, "Labrador", owner3)
pet4 = Pet("Milo", 1, "Poodle", owner4)
pet5 = Pet("Coco", 4, "Bulldog", owner5)
pet6 = Pet("Bailey", 2, "Beagle", owner5)
pet7 = Pet("Rocky", 6, "Rottweiler", owner2)
pet8 = Pet("Charlie", 3, "Husky", owner3)
pet9 = Pet("Daisy", 7, "Yorkshire Terrier", owner4)
pet10 = Pet("Lucy", 2, "Dachshund", owner5)
pet11 = Pet("Angela", 3, "Dog", owner6)

proc1 = Procedure("Checkup", 30)
proc2 = Procedure("Vaccination", 0)
proc3 = Procedure("Surgery", 100)
proc4 = Procedure("Dental Cleaning", 40)
proc4.price = 80 

appointment1 = Appointment("Dr. Smith", pet2, proc1)
appointment2 = Appointment("Dr. Johnson", pet2, proc2)
appointment3 = Appointment("Dr. Williams", pet3, proc3)
appointment4 = Appointment("Dr. Brown", pet4, proc1)
appointment5 = Appointment("Dr. Davis", pet5, proc4)
appointment6 = Appointment("Dr. Smith", pet6, proc2)
appointment7 = Appointment("Dr. Martinez", pet7, proc1)
appointment8 = Appointment("Dr. Garcia", pet8, proc1)
appointment9 = Appointment("Dr. Williams", pet9, proc3)
appointment10 = Appointment("Dr. Smith", pet10, proc1)
appointment11 = Appointment("Dr. Johnson", pet10, proc2)
appointment12 = Appointment("Dr. Lee", pet2, proc1)
appointment13 = Appointment("Dr. Harris", pet3, proc4)
appointment14 = Appointment("Dr. Clark", pet4, proc1)
appointment15 = Appointment("Dr. Brown", pet5, proc3)
appointment16 = Appointment("Dr. Thomas", pet6, proc1)
appointment17 = Appointment("Dr. Martin", pet7, proc2)
appointment18 = Appointment("Dr. Davis", pet8, proc1)
appointment19 = Appointment("Dr. White", pet9, proc4)
appointment20 = Appointment("Dr. Adams", pet10, proc1)

#owner has many appointments
#owner has many pets

#pet belongs to owner
#pet belongs to appointment

#appointment belongs to pet
#appointment belongs to owner through pet (can't import owner due to circular import)

#✅ 2. use chatGPT to create owners and pets

import ipdb; ipdb.set_trace()
