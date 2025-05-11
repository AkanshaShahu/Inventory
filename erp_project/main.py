from fastapi import FastAPI
from erp_project.crew_setup import InventoryProject
import sys

app = FastAPI()
erp_crew = InventoryProject()

@app.get("/")
async def root():
    return {"message": "Welcome to the ERP Inventory & Sales System"}

@app.post("/run-crew")
async def run_crew():
    result = erp_crew.crew().kickoff()
    return {"result": result}
