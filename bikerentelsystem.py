# bikerentelsystem.py
class bikeShop:
	def __init__(self,stock):
		self.stock = stock
	def displayBike(self):
		print("Total Bike",self.stock)

	def rentForBike(self,q):
		if q <= 0 :
			print("Enter positive value or greater then zero")
		elif q > self.stock:
			print("Enter the value (less then stock)")
		else:
			self.stock = self.stock-q
			print("Total price",q*100)
			print("Total Bike",self.stock)

while True:
	obj = bikeShop(100)
	uc = int(input('''
1 Display Stock
2 Rent a Bike
3 Exit
		'''))

	if uc == 1:
		obj.displayBike()
	elif uc == 2:
		n = int(input("Enter the qty:--"))
		obj.rentForBike(n)
	else:
		break