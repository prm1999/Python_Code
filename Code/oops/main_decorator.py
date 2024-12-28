import csv

class Item:
    pay_rate=0.8 # That is class attribute
    all=[] # Empty list for all the instnce we have created 
    
    def __init__(self, name,price,quantity=0 ):
        # Run validation to the recived argument
        assert price>=0 ,f"Price{rice}should be greater than zero"
        assert quantity>=0 , f"Quantity {quantity} should be greater than zero"

        #Assign value to self -- Instance attribute 
        self.name =name
        self.price=price
        self.quantity=quantity   #consructor
        print(f"I am here created a new instance {name},{price},{quantity}")

        #append all the instance-- Action to be created
        Item.all.append(self)

    def calculate_price(self):
        return self.price * self.quantity# using data from init class


    def discount_price(self): # for muliple discount 
        self.price=self.price* self.pay_rate # if attribute  cant find the disount at instance they will find it at the  class level

    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity})"


