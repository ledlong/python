class Car:
    def __init__(self,model,color,fuel,maxspeed,type,year):
        self.model = model
        self.color = color
        self.fuel = fuel
        self.maxspeed = maxspeed
        self.type = type
        self.year = year

class Customer:
    def __init__(self,name,age,job,address):
        self.name = name
        self.age = age
        self.job = job
        self.address = address

class Contract(Car,Customer):
    def __init__(self,id,dealerID,name,age,job,address,model,color,fuel,maxspeed,type,year):
        self.id = id
        self.dealID = dealerID
        Car.__init__(self,model,color,fuel,maxspeed,type,year)
        Customer.__init__(self,name,age,job,address)

firstContract = Contract("123456","9876","Long Le",32,"Scientist","14h Street E Saskatoon SK","Saturn ION","gray","gas",220,"Sedan",2003)