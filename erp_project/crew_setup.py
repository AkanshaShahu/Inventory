from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, task, crew
from .tools.inventory_tool import InventoryTool
from .tools.sales_tool import SalesOrderTool

@CrewBase
class InventoryProject:
    """Crew to manage inventory and sales operations"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    inventory_tool = InventoryTool()
    sales_tool = SalesOrderTool()

    @agent
    def inventory_manager(self) -> Agent:
        return Agent(
            config=self.agents_config["InventoryManager"],
            tools=[self.inventory_tool],
            verbose=True
        )

    @agent
    def sales_manager(self) -> Agent:
        return Agent(
            config=self.agents_config["SalesManager"],
            tools=[self.sales_tool],
            verbose=True
        )

    @task
    def inventory_update_task(self) -> Task:
        return Task(
            config=self.tasks_config["InventoryUpdate"]
        )

    @task
    def sales_order_task(self) -> Task:
        return Task(
            config=self.tasks_config["SalesOrder"]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Inventory Management Crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
