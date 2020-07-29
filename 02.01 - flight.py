class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats() :
            return False
        self.passengers.append(name)
        return True
    
    def open_seats(self):
        return self.capacity - len(self.passengers)
    
flight_vistara2034 = Flight(3)
persons = ["Amit", "Suresh", "Nidhi", "Munish", "Varun"]

for passenger in persons:
    if  flight_vistara2034.add_passenger(passenger) :
        print (f"Added passenger {passenger} to flight.")
    else :
        print (f"Couldn't add passenger {passenger} to flight.")
