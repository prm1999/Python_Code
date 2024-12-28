#created a class and created   intance  and passed the reference
class Item():
    def calcualte_price(self,x,y):
        return x*y
        


item1=Item()
item1.name="Pen"
item1.price=100
item1.quantity=5
x=item1.calcualte_price(item1.price, item1.quantity)
print (x)
