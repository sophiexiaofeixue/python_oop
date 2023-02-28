class BouncyBall:
 
	def __init__(self, price, size, brand):
		self._price = price 
		self._size = size 
		self._brand = brand
	
	def get_price(self):
		return self._price
	
	def set_price(self, new_price):
		if isinstance(new_price, float) and new_price > 0:
			self._price = new_price
		else:
			print('please provide a valid price')
	
	price = property(get_price, set_price)
	def get_size(self):
		return self._size
	def set_size(self, new_size):
		if new_size in ['small', 'medium', 'large']:
			self._size = new_size
	size = property(get_size, set_size)
	def get_brand(self):
		return self._brand
	def set_brand(self, new_brand):
		if isinstance(new_brand, str) and new_brand:
			self._brand = new_brand
	brand = property(get_brand, set_brand)
	

	
class BouncyBall:
 
	def __init__(self, price, size, brand):
		self._price = price 
		self._size = size 
		self._brand = brand
	
	@property
	def price(self):
		return self._price
	
	@price.setter
	def price(self, new_price):
		if isinstance(new_price, float) and new_price > 0:
			self._price = new_price
		else:
			print('please provide a valid price')
#with property syntax, you can access a non-public attribute
#with the same syntax that you used when attribute was public
#because the name of the attribute is available if you wish
#to use the same name
#properties have the adv of adding intermediaries to get
#and set the value of an attribute, so the value is not accessed
#directly and it can be validated before it is assigned