class Item:
    pay_rate=.08 # That is class attribute
    def __init__(self, name,price,quantity=0 ):
        # Run validation to the recived argument
        assert price>=0 ,f"Price{rice}should be greater than zero"
        assert quantity>=0 , f"Quantity {quantity} should be greater than zero"

        #Assign value to self -- Instance attribute 
        self.name =name
        self.price=price
        self.quantity=quantity   #consructor
        print(f"I am here created a new instance {name},{price},{quantity}")

    def calculate_price(self):
        return self.price * self.quantity    # using data from init class

item1=Item("Laptop",10,500) #created an instance for class 
item2=Item("Phone",40,-1)

print(item1.calculate_price()) # printing data for calculator 
print(item2.calculate_price())
'''print(item1.name)
print(item2.name)'''
