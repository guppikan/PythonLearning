
#  Author : Guru prasad Raju 
# Self Key word in python 

# Class name 
class Human():

	def __init__(self,name,age):

		# Self keyword defines instance of class. 
		# By using 'Self' keyword we can access the attribute and method of class
		self.name=name
		self.age=age



human = Human('test',33)

print(human.name)
print(human.age)




