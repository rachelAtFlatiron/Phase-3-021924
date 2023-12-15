#Appointment has one and only one unique pet
#Appointment belongs to pet 
#INTERMEDIARY TABLE BETWEEN PET AND PROCEDURE
#join table
class Appointment:
    all = []

    #✅ 4. create relationship: appointment belongs to a pet
    #✅ 4a. use chatGPT to create instances
    #pet - an instance of pet
    def __init__(self, staff, pet=None, proc=None):
        self.staff = staff 
        self.pet = pet  #an instance of Pet class
        self.proc = proc
        Appointment.all.append(self)

    #✅ 7. Create a function that prints details for the appointment
    def print_details(self): 
        print(f'''
            Owner name: {self.pet.owner.name}
            Pet name: {self.pet.name}
            Pet breed: {self.pet.breed}
            Procedure Name: {self.proc.name}
            Doctor Name: {self.staff}
            Price: {self.proc.price}
        ''')
    #owner's name: self.pet.owner.name 
    #pet name: self.pet.name 
    #pet breed: self.pet.breed 
    #procedure name: self.proc.name
    #staff member: self.staff 
    #price of procedure: self.proc.price 

        
    #✅ 8. Create a class method for all unique clients of the clinic
    @classmethod 
    #cls is similar to self but refers to class in stead of instance
    def all_clients(cls): 
        clients = []
        #look at every single appointment
        #Appointments.all
        for app in cls.all:  
            #find owner of current appointment
            cur_owner = app.pet.owner
            #append to list
            clients.append(cur_owner)
        #return list of UNIQUE CLIENTS
        #multiple clients because client may have more than one appointment
        return list(set(clients))

    def __repr__(self):
        return f'''<Appointment Procedure={self.proc} >'''
    