from pydantic import BaseModel, Field, ConfigDict

class ProductCreate(BaseModel):
    name: str = Field(min_length=2,max_length=100)
    description: str = Field(min_legnth=2,max_length=100)
    price: float = Field(gt=0)
    quantity: int = Field(ge=0)

class ProductUpdate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    description: str = Field(min_length=2, max_length=500)
    price: float = Field(gt=0)
    quantity: int = Field(ge=0)

class ProductResponse(BaseModel):
    model_config= ConfigDict(from_attributes=True)
    id: int
    name: str
    description: str
    price: float
    quantity: int