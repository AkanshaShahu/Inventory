from crewai.tools import Tool

from db.mongo import inventory_collection
from pydantic import BaseModel, Field
from typing import Type

class InventoryTool(Tool):
    name = "InventoryTool"
    description = "Tool to update inventory data"

    async def _arun(self, data: dict) -> str:
        for item in data.get("items", []):
            existing = await inventory_collection.find_one({"product": item["product"]})
            if existing:
                await inventory_collection.update_one(
                    {"product": item["product"]},
                    {"$inc": {"quantity": item["quantity"]}, "$set": {"price": item["price"]}}
                )
            else:
                await inventory_collection.insert_one(item)
        return "Inventory updated"