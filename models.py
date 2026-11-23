from pydantic import BaseModel

class product(BaseModel):
    id: int
    description: str
    price: float
    name:str
    quantity:int
    
        