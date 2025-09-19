# Context
Task file name: 2025-09-19_8_base-learning
Created at: 2025-09-19_03:07:30
Created by: fireos
Main branch: main
Task Branch: task/base-learning_2025-09-19_8
AUTO-RUN MODE: on

# Task Description
[A detailed description based on the [TASK] given by the user.]

# Project Overview
[A detailed overview of the project based on the [PROJECT OVERVIEW] given by the user.]

# Original Execution Protocol
> NOTE: Do not edit/remove.
```
Execution Protocol:
1. Git Branch Creation
Create a new task branch from MAIN BRANCH:
git checkout -b task/[TASK_IDENTIFIER]_[TASK_DATE_AND_NUMBER]
Add the branch name to the [TASK FILE] under "Task Branch."
Verify the branch is active:
git branch --show-current

2. Task File Creation
Create the [TASK FILE], naming it [TASK_FILE_NAME]_[TASK_IDENTIFIER].md and place it in the .tasks directory at the root of the project.
The [TASK FILE] should be implemented strictly using the "Task File Template" below. a. Start by adding the contents of the "Task File Template" to the [TASK FILE]. b. Adjust the values of all placeholders based on the "User Input" and placeholder terminal commands.
Make a visible note in the [TASK FILE] that the "Execution Protocol" and its content should NEVER be removed or edited
<<< HALT IF NOT AUTO-RUN MODE: Before continuing, wait for the user to confirm the name and contents of the [TASK FILE] >>>

3. Task Analysis
Examine the TASK by looking at related code and functionality step-by-step to get a birds eye view of everything. It is important that you do the following, in that specific order, one step at a time: a. Find out the core files and implementation details involved in the TASK.
Store what you've found under the "Task Analysis Tree" of the [TASK FILE]. b. Branch out
Analyze what is currently in the "Task Analysis Tree" of the [TASK FILE].
Look at other files and functionality related to what is currently in the "Task Analysis Tree", by looking at even more details, be throrough and take your time.
Togehter with what you have previously entered under the "Task Analysis Tree" merge and add the newly gathered information. c. Repeat b until you have a full understanding of everything that might be involved in solving the task.
Do NOT stop until you can't find any more details that might be relevant to the TASK.
Double check everything you've entered in the "Task Analysis Tree" of the [TASK FILE]
Look through everything in the "Task Analysis Tree" and make sure you weed out everything that is not essential for solving the TASK.
<<< HALT IF NOT AUTO-RUN MODE: Before continuing, wait for user confirmation that your analysis is satisfactory, if not, iterate on this >>>

4. Iterate on the Task
Analyze code context fully before changes.
Analyze updates under "Task Progress" in the [TASK FILE] to ensure you don't repeat previous mistakes or unsuccessful changes.
Make changes to the codebase as needed.
Update any progress under "Task Progress" in the [TASK FILE].
For each change:
Seek user confirmation on updates.
Mark changes as SUCCESSFUL or UNSUCCESSFUL in the log after user confirmation.
Optional, when apporopriate (determined appropriate by you), commit code:
git add --all -- ':!./.tasks'
git commit -m "[COMMIT_MESSAGE]"
<<< HALT IF NOT AUTO-RUN MODE: Before continuing, confirm with the user if the changes where successful or not, if not, iterate on this execution step once more >>>

5. Task Completion
After user confirmation, and if there are changes to commit:
Stage all changes EXCEPT the task file:
git add --all -- ':!./.tasks'
Commit changes with a concise message:
git commit -m "[COMMIT_MESSAGE]"
<<< HALT IF NOT AUTO-RUN MODE:: Before continuing, ask the user if the [TASK BRANCH] should be merged into the MAIN BRANCH, if not, proceed to execution step 8 >>>

6. Merge Task Branch
Confirm with the user before merging into MAIN BRANCH.
If approved:
Checkout MAIN BRANCH:
git checkout [MAIN BRANCH]
Merge:
git merge -
Confirm that the merge was successful by running:
git log [TASK BRANCH]..[MAIN BRANCH] | cat

7. Delete Task Branch
Ask the user if we should delete the [TASK BRANCH], if not, proceed to execution step 8
Delete the [TASK BRANCH]:
git branch -d task/[TASK_IDENTIFIER]_[TASK_DATE_AND_NUMBER]
<<< HALT IF NOT AUTO-RUN MODE:: Before continuing, confirm with the user that the [TASK BRANCH] was deleted successfully by looking at git branch --list | cat >>>

8. Final Review
Look at everything we've done and fill in the "Final Review" in the [TASK FILE].
<<< HALT IF NOT AUTO-RUN MODE:: Before we are done, give the user the final review >>>
```

# Task Analysis
- Purpose of the [TASK].
- Issues identified.
- Implementation details and goals.

# Task Analysis Tree
- (fill during analysis)

# Steps to take
- (list actionable steps)

# Current execution step: 1

# Important Notes
- NEVER REMOVE THIS SECTION

# Task Progress
- 2025-09-19_03:07:30 — (pending)

# Final Review
- (fill when complete)
