
from pydantic import BaseModel, Field , field_validator, model_validator


class CreateUser(BaseModel):
    email: str
    password: str
    confirm_password: str

    @field_validator("email") # field_validator is a decorator that is used to validate a specific field in the model. It takes the name of the field as an argument.
    def validate_email(cls, value):
        if "admin" in value:
            raise ValueError("Email cannot contain 'admin'")
        return value
    
    @model_validator(mode="after") # model_validator is a decorator that is used to validate the entire model. It takes no arguments.
    def validate_passwords(self):
        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match")
        return self
    
user = CreateUser(email="hello@gmail.com",password= "wefef",confirm_password="rfsf")
print(user)


# In Pydantic
# model_validator(mode="before")
# ➡ Runs before Pydantic parses the data, so it receives the raw input dictionary.
# Example:
# from pydantic import BaseModel, model_validator

# class User(BaseModel):
#     name: str

#     @model_validator(mode="before")
#     def rename_field(cls, values):
#         if "username" in values:
#             values["name"] = values.pop("username")
#         return values

# User(username="Josh")
# model_validator(mode="after")
# ➡ Runs after the model is created, so it works with the validated model object (self).
# Example:
# from pydantic import BaseModel, model_validator

# class User(BaseModel):
#     password: str
#     confirm_password: str

#     @model_validator(mode="after")
#     def check_password(self):
#         if self.password != self.confirm_password:
#             raise ValueError("Passwords do not match")
#         return self
# ✅ One-line memory trick
# before → raw input dict
# after  → validated model object