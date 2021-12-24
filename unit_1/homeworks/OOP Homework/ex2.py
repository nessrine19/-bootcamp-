class vehicle :
    def __init__(self,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage

my_car=vehicle(180,2000)
print(my_car.max_speed,my_car.mileage)
