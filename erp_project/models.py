from pydantic import BaseModel
from typing import List
from crewai.tools import BaseTool
class InventoryItem(BaseModel):
    product: str
    quantity: int
    price: float

class InventoryInput(BaseModel):
    items: List[InventoryItem]

class SalesItem(BaseModel):
    product: str
    quantity: int
    price: float

class SalesOrderInput(BaseModel):
    customer: str
    items: List[SalesItem]