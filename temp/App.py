from priority_flowchart import PriorityFlowchart

# Create a new flowchart instance
flowchart = PriorityFlowchart()

# Add and evaluate a task
task = flowchart.add_task("Complete quarterly report", "Financial report for Q3")

# Print the task's evaluation results
flowchart.print_task_status(task)
