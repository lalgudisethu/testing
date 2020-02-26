class Circle:
	def __init__(self,x,y,rad):
		self.x=x
		self.y=y
		self.rad=rad
		self.l1=[]
		self.l1.append(x)
		self.l1.append(y)
		self.l1.append(rad)
	def show(self):
		print(self.x,self.y,self.rad)
		print(self.l1)

class Square:
	def __init__(self,x1,y1,x2,y2):
		self.x1=x1
		self.y1=y1
		self.x2=x2
		self.y2=y2
	def show(self):
		print(self.x1,self.y1,self.x2,self.y2)	

class Combine(Circle,Square):
	def __init__(self,x,y,rad,x1,y1,x2,y2,p,q,r):
		Circle.__init__(self,x,y,rad)
		Square.__init__(self,x1,y1,x2,y2)
		self.p=p
		self.q=q
		self.r=r

	def show(self):
		Circle.show(self)
		Square.show(self)
		print(self.p,self.q,self.r)

c=Combine(10,20,30,1,2,3,4,8,9,10)
c.show()

d1=Circle(4,5,6)
d1.show()

d2=Circle(7,8,9)
d2.show()
