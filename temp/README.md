# Task Priority Evaluation System

This system implements a sophisticated task prioritization flowchart that evaluates tasks based on multiple criteria including productivity, effectiveness, efficiency, importance, and urgency. The system assigns priorities ranging from P1 (highest) to WONT_DO based on the evaluation path.

## Overview

The system asks a series of questions about each task to determine:
1. Productivity (Are we doing anything?)
2. Effectiveness (Are we doing the right things?)
3. Efficiency (Are we doing things right?)
4. Importance (Are we doing important things?)
5. Urgency (Are we doing urgent things?)

Based on the answers, it assigns:
- A priority level (P1, P2A, P2B, P3, P4A, P4B, P5, or WONT_DO)
- A waste status (WASTE or NON_WASTE)
- Various other status indicators

## Priority Levels

- **P1**: Important and Urgent tasks
- **P2A**: Unimportant but Urgent tasks
- **P2B**: Important but Non-urgent tasks
- **P3**: Unimportant and Non-urgent tasks
- **P4A**: Effective and Efficient tasks (leads to importance/urgency evaluation)
- **P4B**: Ineffective but Efficient tasks
- **P5**: Either Ineffective & Inefficient OR Effective but Inefficient tasks
- **WONT_DO**: Non-productive tasks

## How to Use

1. Save the code in a file named `priority_flowchart.py`
2. [Run the code using Python 3](https://www.freecodecamp.org/news/run-python-script-how-to-execute-python-shell-commands-in-terminal/) (```$ python```):

```python
>>> from priority_flowchart import PriorityFlowchart

# Create a new flowchart instance
>>> flowchart = PriorityFlowchart()

# Add and evaluate a task
>>> task = flowchart.add_task("Complete quarterly report", "Financial report for Q3")

# Print the task's evaluation results
>>> flowchart.print_task_status(task)
```
3. Or run ```$ python App.py``` for a set of instructions.

## Example Tasks and Their Paths

### Example 1: High Priority Task (P1)
```python
# Task: "Handle customer data breach"
# Answers:
# - Are we doing anything? → yes (Productive)
# - Are we doing the right things? → yes (Effective)
# - Are we doing things right? → yes (Efficient)
# - Are we doing Important things? → yes (Important)
# - Are we doing urgent things? → yes (Urgent)
# Result: Priority P1, NON_WASTE
```

### Example 2: Medium Priority Task (P2A)
```python
# Task: "Fix minor UI bug before release"
# Answers:
# - Are we doing anything? → yes (Productive)
# - Are we doing the right things? → yes (Effective)
# - Are we doing things right? → yes (Efficient)
# - Are we doing Important things? → no (Unimportant)
# - Are we doing urgent things? → yes (Urgent)
# Result: Priority P2A, NON_WASTE
```

### Example 3: Strategic Task (P2B)
```python
# Task: "Develop 5-year strategic plan"
# Answers:
# - Are we doing anything? → yes (Productive)
# - Are we doing the right things? → yes (Effective)
# - Are we doing things right? → yes (Efficient)
# - Are we doing Important things? → yes (Important)
# - Are we doing urgent things? → no (Non-urgent)
# Result: Priority P2B, NON_WASTE
```

### Example 4: Low Priority Task (P3)
```python
# Task: "Reorganize old documentation"
# Answers:
# - Are we doing anything? → yes (Productive)
# - Are we doing the right things? → yes (Effective)
# - Are we doing things right? → yes (Efficient)
# - Are we doing Important things? → no (Unimportant)
# - Are we doing urgent things? → no (Non-urgent)
# Result: Priority P3, NON_WASTE
```

### Example 5: Efficient but Ineffective Task (P4B)
```python
# Task: "Optimize legacy system that's being replaced"
# Answers:
# - Are we doing anything? → yes (Productive)
# - Are we doing the right things? → no (Ineffective)
# - Are we doing things right? → yes (Efficient)
# Result: Priority P4B, WASTE
```

### Example 6: Inefficient Task (P5)
```python
# Task: "Manual data entry instead of automation"
# Answers:
# - Are we doing anything? → yes (Productive)
# - Are we doing the right things? → yes (Effective)
# - Are we doing things right? → no (Inefficient)
# Result: Priority P5, WASTE
```

### Example 7: Non-productive Task (WONT_DO)
```python
# Task: "Watch cat videos"
# Answers:
# - Are we doing anything? → no (Non-productive)
# Result: Priority WONT_DO, NON_WASTE
```

## Full Example Implementation

```python
from priority_flowchart import PriorityFlowchart

def run_example():
    flowchart = PriorityFlowchart()
    
    # Example of adding and evaluating a task
    task = flowchart.add_task(
        title="Implement new security feature",
        description="Add two-factor authentication to user login"
    )
    
    # Print the evaluation results
    flowchart.print_task_status(task)

if __name__ == "__main__":
    run_example()
```

## Understanding the Output

The `print_task_status()` method provides detailed information about the task evaluation:
- Title and Description
- Productivity Status
- Effectiveness Status
- Efficiency Status
- Waste Status
- Priority Level
- Importance Status
- Urgency Status
- Complete Decision Path

## Decision Path Visualization

The system includes a flowchart visualization that shows all possible paths a task can take through the evaluation process. This helps in understanding how different combinations of answers lead to different priority levels.

## Note

The evaluation process is interactive and requires user input for each question. Answer each question with 'yes'/'y' or 'no'/'n'. The system will guide you through the appropriate path based on your answers.
