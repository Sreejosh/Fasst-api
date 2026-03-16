# The core concept of Pydantic is "Data Parsing, not just Validation."
# In a normal Python script, if you pass a string to something expecting a number, the code might crash later. Pydantic acts like a bouncer at the door: it checks the data the moment it arrives. If the data looks okay but is the wrong type (like the string "10" instead of the integer 10), Pydantic cleans/converts it. If it’s total junk, it refuses entry.
# The Concept in FastAPI
# When you use Pydantic in FastAPI, you define a Schema (a class). FastAPI uses that schema to:
# Read the incoming JSON.
# Validate that all required fields are there.
# Convert the data into a Python object you can actually use.
# Code Example
# Here is how you define a model and use it in a FastAPI route:
# python
# from fastapi import FastAPI
# from pydantic import BaseModel, EmailStr

# app = FastAPI()

# # 1. Define the "Shape" of your data (The Concept)
# class UserSignup(BaseModel):
#     username: str
#     age: int
#     email: EmailStr  # Pydantic even checks if it's a real email format

# # 2. Use it in a route
# @app.post("/register")
# def create_user(user: UserSignup):
#     # By the time the code gets here, Pydantic has already 
#     # verified that 'user' is valid and 'age' is a real integer.
#     return {"message": f"User {user.username} created!"}
# Use code with caution.

# Why this is a big deal:
# Without Pydantic: You’d have to manually write if type(age) != int or if "@" not in email for every single piece of data.
# With Pydantic: You just define the class once, and FastAPI handles the headache. If a user sends {"age": "twenty"}, FastAPI automatically sends back a 422 Unprocessed Entity error before your function even runs.


from pydantic import BaseModel , Field
from typing import Optional , List
from datetime import datetime
from enum import Enum

class language(str, Enum):
    PY = "python"
    JAVA = "java"
    GO = "go"

    # Nested Pydantics

class Comments(BaseModel):
    text : Optional[str] = None

class Blog(BaseModel):
    title : str = Field(min_length=10)
    desc : Optional[str] = None
    number : int
    is_active : bool
    lang : language= language.GO # Default value
    # date : datetime = datetime.now() # datetime.now() is executed only once when the class is defined, not when each object is created.
# So both objects will get the same timestamp, even though you added time.sleep(5). 
# We can do this instead by using a default_factory which is a function that will be called to generate a default value for the field when an object is created without providing a value for that field.

    date : datetime = Field(default_factory = datetime.now)
    comments : Optional[List[Comments]] = None # Nested Pydantic model

first_blog = Blog(title="My First Blog", number=1, is_active=True, comments=[{"text":"Great blog!"}]) # Even if we give dict in comments, it will be converted to Comments object because of the type hinting and the nested Pydantic model.
print(first_blog)


import time
time.sleep(5)

second_blog = Blog(title="My Second Blog", number=2, is_active=True)
print(second_blog)

print(first_blog.model_dump()) # returns the blog object as a dictionary , dict is deprecated in pydantic v2, we can use model_dump() instead
print(first_blog.model_dump_json()) # returns the blog object as a JSON string, json is deprecated in pydantic v2, we can use model_dump_json() instead
print(first_blog.model_json_schema()) # returns the schema of the blog object as a dictionary, schema is deprecated in pydantic v2, we can use model_json_schema() instead