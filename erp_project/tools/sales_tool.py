from crewai.tools import BaseTool


from db.mongo import inventory_collection, orders_collection
from pydantic import BaseModel, Field
from typing import Type

class SalesOrderTool(BaseTool):
    name = "SalesOrderTool"
    description = "Tool to process sales order and update stock"

    async def _arun(self, data: dict) -> str:
        customer = data["customer"]
        items = data["items"]

        for item in items:
            existing = await inventory_collection.find_one({"product": item["product"]})
            if not existing or existing["quantity"] < item["quantity"]:
                return f"Not enough stock for {item['product']}"
            await inventory_collection.update_one(
                {"product": item["product"]},
                {"$inc": {"quantity": -item["quantity"]}}
            )

        await orders_collection.insert_one({"customer": customer, "items": items})
        return "Sales order processed"