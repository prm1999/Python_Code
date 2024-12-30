from  item import Item


class Phone(Item): # inheritance of Item class
    all=[]
    def __init__(self, name:str,price:float,quantity=0,broken_phone=0 ):
        #Call to super function to have access to all the attribute and object from the parent class
        super().__init__(
            name,price,quantity
            )

        
        # Run validation to the recived argument
        assert broken_phone>=0 , f"Quantity {quantity} should be greater than zero"

        #Assign value to self -- Instance attribute 
        self.broken_phone= broken_phone
        #print(f"I am here created a new instance {name},{price},{quantity},{broken_phone}")

        # That will inherit from parent class
        #append all the instance-- Action to be created
        Phone.all.append(self)
    
# when you can access the class method then you will directly call the class from the function
phone1=Phone('Nokia',1000,5,1)
print(phone1.calculate_price())
print(Phone.all)




#Item.instantiate_from_csv()

#print(Item.all)
