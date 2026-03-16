from typing import List, Dict, Tuple,  Union, Any

# Type hints for variables and functions can be used to indicate the expected type of a variable or the return type of a function. 
# This can help with code readability and can also be used by static type checkers to catch potential type errors.

price : List[float] = [1.0, 2.5, 3.75]
price1: Tuple[float, float, float] = (1.0, 2.5, 3.75)
product_info: Dict[str, float] = {
    "apple": 1.0,
    "banana": 0.5}

def type_hint_Check(value:float) -> Union[float, None]:
    try:
        conversion_fac = 75
        value = value/conversion_fac
        return value
    except TypeError:
        return None

#Custom type hint (Image is an list of integers representing pixel values)

Image = List[List[int]]

def image_detail(pic :Image) -> List:
    flat_list = []
    for sublist in pic:
        for item in sublist:
            flat_list.append(item)
    return flat_list

Image1: Image = [[23,45,67],[12,34,67]]


# Iterators __iter__() and __next__()

class InfiniteNumber():
    def __init__(self):
        self.num = 0

    def __iter__(self): #dunder method for making the class an iterator
        return self
    def __next__(self): # for the next element in the iterator
        num = self.num
        self.num += 1
        return num
    
value = InfiniteNumber()
for i in range(1, 10):
    print(next(value))

list1 = [1,2,3,4,5]
list_iter = list1.__iter__()
print(next(list_iter)) #prints 1 and if we keep calling next(list_iter) it will print the next element in the list until it reaches the end of the list and raises StopIteration error.

#Instead of all this, we can simply create a generator ( its a special type iterator) using a generator expression or a generator function.

def return_value():
    yield 1
    yield 2
    yield 3
    yield "four"


value = return_value()
print(value.__next__()) #prints 1 and if we keep calling next(value) it will print the next element in the generator until it reaches the end of the generator and raises StopIteration error.


def even_numbers():
    # generate  the even_numbers < 20
    for i in range(0,20):
        if i%2 == 0:
            yield i

for value in even_numbers():
    print(value)


# Pydantic models are used to define the structure of data and to validate the data. 
# They are used in FastAPI to define the request and response models. They are also used to define the models for the database.
#  Pydantic models are defined using the BaseModel class from the pydantic library. 
# They can be used to define the fields of the model and their types. They can also be used to define default values for the fields and to define validators for the fields.

#Multiple Inheritance in Python is a feature that allows a class to inherit from multiple parent classes.

class Pydantic:
    def isvalid(self,text):
        if "admin" in text:
            return False
        return True

class Starlette:
    def isvalid(self,text):
        return True

class FastAPI(Pydantic, Starlette):
    pass

f = FastAPI()
print(FastAPI.__mro__) #prints the method resolution order of the FastAPI class, which is the order in which the methods are called when we call a method on an instance of the FastAPI class.
print(f.isvalid("admin")) #prints False because the isvalid method of the Pydantic class is called first because of the order of inheritance. 
#If we change the order of inheritance to
        