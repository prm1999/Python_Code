import csv

class Item:
    pay_rate=0.8 # That is class attribute
    all=[] # Empty list for all the instnce we have created 
    
    def __init__(self, name:str,price:float,quantity=0 ):
        # Run validation to the recived argument
        assert price>=0 ,f"Price{rice}should be greater than zero"
        assert quantity>=0 , f"Quantity {quantity} should be greater than zero"

        #Assign value to self -- Instance attribute 
        self.name =name
        self.price=price
        self.quantity=quantity   #consructor
        #print(f"I am here created a new instance {name},{price},{quantity}")

        #append all the instance-- Action to be created
        #Item.all.append(self)

    def calculate_price(self):
        return self.price * self.quantity# using data from init class


    def discount_price(self): # for muliple discount 
        self.price=self.price* self.pay_rate # if attribute  cant find the disount at instance they will find it at the  class level

    #decorator is used to  chnage the behivour of the function. 
    @classmethod
    def instantiate_from_csv(cls):
                #context manager is used to read the file 

        with open('data.csv','r') as f: #open csv file
            reader=csv.DictReader(f) #convert object into dict
            items=list(reader)# convert dict as list 

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=float(item.get('quantity')),
                 )
    @staticmethod # static method 
    def is_integer(num):
            # we will count out the floats are zero
            #for i.e 5.0 10.0
        if isinstance(num, float):
                #Count out the float that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else :
            return False
            
            

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}',{self.price},{self.quantity})"
    #self.__class__.__name__ is used to check the correct class name
    




#Inheritance of class
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





