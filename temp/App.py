from dataclasses import dataclass
from enum import Enum
from typing import List, Optional, Dict

class Priority(Enum):
    P1 = 1      # For important and urgent tasks
    P2A = "2A"  # For unimportant but urgent tasks
    P2B = "2B"  # For important but non-urgent tasks
    P3 = 3      # For unimportant and non-urgent tasks
    P4A = "4A"  # Special priority for effective and efficient tasks
    P4B = "4B"  # Special priority for efficient but ineffective tasks
    P5 = 5      # For ineffective & inefficient tasks AND effective & inefficient tasks
    WONT_DO = 6 # Special category for non-productive tasks

class ProductivityStatus(Enum):
    PRODUCTIVE = "Productive"
    NON_PRODUCTIVE = "Non-productive"

class EffectivenessPath(Enum):
    EFFECTIVE = "Effective"
    INEFFECTIVE = "Ineffective"
    NOT_APPLICABLE = "N/A"  # For non-productive tasks

class EfficiencyStatus(Enum):
    EFFICIENT = "Efficient"
    INEFFICIENT = "Inefficient"
    NOT_APPLICABLE = "N/A"  # For cases where efficiency isn't evaluated

class WasteStatus(Enum):
    WASTE = "Waste"
    NON_WASTE = "Non-waste"
    NOT_YET_DETERMINED = "Not yet determined"

class ImportanceStatus(Enum):
    IMPORTANT = "Important"
    UNIMPORTANT = "Unimportant"
    NOT_APPLICABLE = "N/A"  # For tasks that don't reach importance evaluation

class UrgencyStatus(Enum):
    URGENT = "Urgent"
    NON_URGENT = "Non-urgent"
    NOT_APPLICABLE = "N/A"  # For tasks that don't reach urgency evaluation

@dataclass
class Task:
    title: str
    description: str
    priority: Optional[Priority] = None
    decision_path: List[str] = None
    productivity_status: Optional[ProductivityStatus] = None
    effectiveness_status: Optional[EffectivenessPath] = None
    efficiency_status: Optional[EfficiencyStatus] = None
    waste_status: Optional[WasteStatus] = None
    importance_status: Optional[ImportanceStatus] = None
    urgency_status: Optional[UrgencyStatus] = None
    
    def __post_init__(self):
        self.decision_path = ["Start"]
        self.waste_status = WasteStatus.NOT_YET_DETERMINED
        self.efficiency_status = EfficiencyStatus.NOT_APPLICABLE
        self.importance_status = ImportanceStatus.NOT_APPLICABLE
        self.urgency_status = UrgencyStatus.NOT_APPLICABLE

    def finish_evaluation(self):
        """Add the Finish marker to the decision path"""
        self.decision_path.append("Finish")

class PriorityFlowchart:
    def __init__(self):
        self.tasks: List[Task] = []
        
    def evaluate_task(self, task: Task) -> Priority:
        """
        Walks through the flowchart decision tree to determine task priority.
        """
        print("\nPriority Evaluation for task:", task.title)
        print("----------------------------------------")
        
        # First decision point - Productivity
        is_productive = self._ask_question(
            "For this task, are we doing anything?",
            task
        )
        
        if not is_productive:
            task.decision_path.append("Non-productive task - Won't do")
            task.productivity_status = ProductivityStatus.NON_PRODUCTIVE
            task.effectiveness_status = EffectivenessPath.NOT_APPLICABLE
            task.waste_status = WasteStatus.NON_WASTE
            task.decision_path.append("No time/resources invested - Classified as NON_WASTE")
            task.priority = Priority.WONT_DO
            task.finish_evaluation()
            return Priority.WONT_DO
            
        # Mark as productive
        task.productivity_status = ProductivityStatus.PRODUCTIVE
        task.decision_path.append("Task is productive")
        
        # Second decision point - Effectiveness
        is_effective = self._ask_question(
            "With this task, are we doing the right thing(s)?",
            task
        )
        
        if not is_effective:
            task.decision_path.append("Task is ineffective")
            task.effectiveness_status = EffectivenessPath.INEFFECTIVE
            
            # Third decision point for ineffective tasks - Efficiency
            is_efficient = self._ask_question(
                "With this task, are we doing the thing(s) right?",
                task
            )
            
            if is_efficient:
                task.efficiency_status = EfficiencyStatus.EFFICIENT
                task.decision_path.append("Task is efficient but ineffective")
                task.priority = Priority.P4B
                task.waste_status = WasteStatus.WASTE
                task.decision_path.append("Classified as WASTE due to being ineffective despite efficiency")
                task.finish_evaluation()
                return Priority.P4B
            else:
                task.efficiency_status = EfficiencyStatus.INEFFICIENT
                task.decision_path.append("Task is inefficient and ineffective")
                task.priority = Priority.P5
                task.waste_status = WasteStatus.WASTE
                task.decision_path.append("Classified as WASTE due to being ineffective and inefficient")
                task.finish_evaluation()
                return Priority.P5
        else:
            # Effective path
            task.decision_path.append("Task is effective")
            task.effectiveness_status = EffectivenessPath.EFFECTIVE
            
            # Check efficiency for effective tasks
            is_efficient = self._ask_question(
                "With this task, are we doing the thing(s) right?",
                task
            )
            
            if is_efficient:
                task.efficiency_status = EfficiencyStatus.EFFICIENT
                task.decision_path.append("Task is effective and efficient")
                task.priority = Priority.P4A
                task.waste_status = WasteStatus.NON_WASTE
                task.decision_path.append("Classified as NON_WASTE due to being effective and efficient")
                
                # Importance decision point
                is_important = self._ask_question(
                    "With this task, are we doing the Important Thing(s)?",
                    task
                )
                
                if is_important:
                    task.importance_status = ImportanceStatus.IMPORTANT
                    task.decision_path.append("Task is Important")
                    
                    # Urgency check for important tasks
                    is_urgent = self._ask_question(
                        "With this task, are we doing the urgent thing(s)?",
                        task
                    )
                    
                    if is_urgent:
                        task.urgency_status = UrgencyStatus.URGENT
                        task.decision_path.append("Task is Urgent")
                        task.priority = Priority.P1
                        task.waste_status = WasteStatus.NON_WASTE
                        task.decision_path.append("Classified as NON_WASTE")
                    else:
                        task.urgency_status = UrgencyStatus.NON_URGENT
                        task.decision_path.append("Task is Non-urgent")
                        task.priority = Priority.P2B
                        task.waste_status = WasteStatus.NON_WASTE
                        task.decision_path.append("Classified as NON_WASTE")
                else:
                    task.importance_status = ImportanceStatus.UNIMPORTANT
                    task.decision_path.append("Task is Unimportant")
                    
                    # Urgency check for unimportant tasks
                    is_urgent = self._ask_question(
                        "With this task, are we doing the urgent thing(s)?",
                        task
                    )
                    
                    if is_urgent:
                        task.urgency_status = UrgencyStatus.URGENT
                        task.decision_path.append("Task is Urgent")
                        task.priority = Priority.P2A
                        task.waste_status = WasteStatus.NON_WASTE
                        task.decision_path.append("Classified as NON_WASTE")
                    else:
                        task.urgency_status = UrgencyStatus.NON_URGENT
                        task.decision_path.append("Task is Non-urgent")
                        task.priority = Priority.P3
                        task.waste_status = WasteStatus.NON_WASTE
                        task.decision_path.append("Classified as NON_WASTE")
                
                task.finish_evaluation()
                return task.priority
            else:
                task.efficiency_status = EfficiencyStatus.INEFFICIENT
                task.decision_path.append("Task is effective but inefficient")
                task.priority = Priority.P5
                task.waste_status = WasteStatus.WASTE
                task.decision_path.append("Classified as WASTE due to being inefficient despite effectiveness")
                task.finish_evaluation()
                return Priority.P5
    
    def _ask_question(self, question: str, task: Task) -> bool:
        """
        Asks a yes/no question and returns the response.
        Records the question and answer in the task's decision path.
        """
        while True:
            response = input(f"{question} (yes/no): ").lower().strip()
            if response in ['yes', 'y']:
                task.decision_path.append(f"Q: {question} - A: Yes")
                return True
            elif response in ['no', 'n']:
                task.decision_path.append(f"Q: {question} - A: No")
                return False
            else:
                print("Please answer 'yes' or 'no'")
    
    def add_task(self, title: str, description: str = "") -> Task:
        """Creates a new task and evaluates its priority."""
        if not title.strip():
            raise ValueError("Task title cannot be empty")
        task = Task(title=title, description=description)
        priority = self.evaluate_task(task)
        self.tasks.append(task)
        return task
    
    def print_task_status(self, task: Task):
        """Prints the current status of a task including its decision path."""
        print("\nTask Status:")
        print(f"Title: {task.title}")
        if task.description:
            print(f"Description: {task.description}")
        print(f"Productivity: {task.productivity_status.value if task.productivity_status else 'Not yet determined'}")
        print(f"Effectiveness: {task.effectiveness_status.value if task.effectiveness_status else 'Not yet determined'}")
        print(f"Efficiency: {task.efficiency_status.value}")
        print(f"Waste Status: {task.waste_status.value}")
        print(f"Priority: {task.priority.name if task.priority else 'Not yet determined'}")
        print(f"Importance: {task.importance_status.value}")
        print(f"Urgency: {task.urgency_status.value}")
        print("\nDecision Path:")
        for i, step in enumerate(task.decision_path, 1):
            print(f"{i}. {step}")

if __name__ == "__main__":
    flowchart = PriorityFlowchart()
    task = flowchart.add_task("Example Task", "Description of the task")
    flowchart.print_task_status(task)
