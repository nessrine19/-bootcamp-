class vehicle :
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
    
    def vehicle_method(self):
        print("bus name :",self.name,"\n","speed :",self.max_speed,"\n","mileage :",self.mileage)

class bus(vehicle):
    pass
my_bus=bus("meymey",180,2000)
my_bus.vehicle_method()
