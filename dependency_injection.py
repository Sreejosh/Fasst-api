from fastapi import FastAPI, Depends, HTTPException, status


#Dependency Injection is a design pattern that allows us to inject dependencies into our functions or classes. 
# It is a way to decouple the code and make it more modular and reusable. 
# In FastAPI, we can use the Depends function to inject dependencies into our routes.


app = FastAPI(title="Dependency Injection Example", version="0.1.0")


blogs = {
    "1": {"name": "First Blog"},
    "2": {"name": "Second Blog"},
    "3": {"name": "Third Blog"}
}

users = {
    "1": {"name": "Alice"},
    "2": {"name": "Bob"},
    "3": {"name": "Charlie"}
}



def get_blog_name(blog_id: str):
        blog = blogs.get(blog_id)
        if not blog:
              raise HTTPException(f"Blog with {blog_id} not found",status_code=status.HTTP_404_NOT_FOUND)
        return blog


#now instead of geting only for blog, we can also use it to get other resources like user, comments etc. by just changing the function and the resource we want to get. 
# This is the power of dependency injection, we can reuse the same function to get different resources by just changing the parameters and the resource we want to get.


def get_object(model: dict, object_id: str): # In this parameteized dependency, If i use this, i need to pass in the model and the object_id every time i want to get a resource, which is not efficient.
        obj = model.get(object_id)
        if not obj:
              raise HTTPException(detail=f"Object with {object_id} not found",status_code=status.HTTP_404_NOT_FOUND)
        return obj

class GetorObject404: # In this parameteized dependency, the model is stored in the class and we can reuse the same class to get different resources by just changing the model we want to use.
      def __init__(self, model:dict):
            self.model = model

      def __call__(self, object_id: str):
        obj = self.model.get(object_id)
        if not obj:
              raise HTTPException(detail=f"Object with {object_id} not found",status_code=status.HTTP_404_NOT_FOUND)
        return obj
       
blog_dependency = GetorObject404(blogs)
# since we are using a single class for getting both blog and user, and more if we want, to , when we are geting from the app.get() we should refer to Object_id
@app.get("/blog/{object_id}")
def get_blog(blog = Depends(blog_dependency)):
    return blog


user_depedency = GetorObject404(users)
@app.get("/user/{object_id}")
def get_user(user = Depends(user_depedency)):
    return user



# A function dependency runs logic directly, while a class dependency (with __call__) can store state and be reused with different configurations.
# Example
# Function dependency
# def get_object(model: dict, object_id: str):
#     return model.get(object_id)
# Usage (must pass model each time):
# Depends(lambda object_id: get_object(blogs, object_id))
# Class dependency
# class GetObject:
#     def __init__(self, model: dict):
#         self.model = model

#     def __call__(self, object_id: str):
#         return self.model.get(object_id)
# Usage (model stored once):
# blog_dependency = GetObject(blogs)

# @app.get("/blog/{object_id}")
# def get_blog(blog = Depends(blog_dependency)):
#     return blog
# Key idea:
# Function = simple logic
# Class = reusable dependency with stored configuration.