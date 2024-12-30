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


item1=Item("Laptop",10,5) #created an instance for class
item2=Item("Phone",1000,3) #created an instance for class 
item3=Item("car",13000,1) #created an instance for class
item4=Item("Pen",70,6) #created an instance for class
item5=Item("Keyboard",10,4) #created an instance for class
item6=Item("Mourse",80,3) #created an instance for class


print(Item.all)# will print all the instnce

"""
# print the things which is required 
for i in  Item.all:
    print(i.name)

# price before the discount
print(item1.price)    
#First apply discount then ask the price
item1.discount_price() # discount applied 
print(item1.price)


# using slef at the class attribute while calling  at the intance

item2.pay_rate=0.7 # Discount assign here --> at the instnce we are accesing the discount 
item2.discount_price()
print(item2.price)


'''
item1=Item("Laptop",10,500) #created an instance for class 
item2=Item("Phone",40,10)

print(item1.calculate_price()) # printing data for calculator 
print(item2.calculate_price())


print(item1.name)




print(item2.name)'''

"""


"""
        @property
        #Property Decorator use only for the  Read only
        def name(self):
            return self.__name

        @name.setter
        def name(self,vale):
            if len(value>10):
                raise Exception("leng is greater than expected")
            else:
                self.___name= value
"""
