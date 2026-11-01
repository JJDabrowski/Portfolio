---
name: iterate-table
description: Create a new iteration of the table based on user input.
---

# Iterate Table

Create a new iteration of a table per user-specified changes; write result to `result` folder.

## Process

1. Ask user for the specifications of the new table iteration.
2. Read the input table against those specifications.
3. Identify redundancy, buried key info, and unclear structure in the input.
4. Resolve ambiguities/inconsistencies between the data and the task with the user before changing anything.
5. Write the final result table to the `docs/result` folder.
6. Show a concise diff/summary of what changed and why.

## Principles

- If the user's spec is ambiguous, clarify before applying changes.
- Final table must accurately reflect the user's specifications.
- Maintain the original table's formatting: colors, comments, and alignment.

## Rules

- Treat the task prompt as complete context.
- No roleplay, no filler, no restating the task.
- Extremely concise and pragmatic.
- Never drop or alter original requirements/meaning.
