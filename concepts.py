class car:
    def __init__(self,make,model,mileage,year):
        self.make = make
        self.model = model
        self.mileage = mileage
        self.year = year
        
    
audicar = car('bmw','nexa',20,2021)
audicar.year = 2020
print(audicar.year,audicar.model)