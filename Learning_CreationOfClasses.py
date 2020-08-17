# This file describe different ways to create a class 


# method1 -creation 

class A(object):
	def __init(self):
		pass 




#method2 

class B(object):
	def __call(cls,*args, **kwargs):
		return super(B,cls).__call__(cls,*args,**kwargs)




#method3 

class C(object):
	def __new__(cls,*args, **kwargs):
		return super(B,cls).__call__(cls,*args,**kwargs)
