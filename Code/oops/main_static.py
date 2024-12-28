class Item:
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


print(Item.is_integer(11.90))

    
