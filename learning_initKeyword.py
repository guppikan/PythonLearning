
# Author : Guru Prasad Raju


# Class name 
class Car():
    
    # def __init__() fuctions is called constructor function.
    # This will initalize calss car with name and color parameters
	def __init__(self,name,color):
		self.name=name
		self.colo=color



# Creating instance of class 
car =Car('maruti','red')

# Printing the instance of call with name
print(car.name)