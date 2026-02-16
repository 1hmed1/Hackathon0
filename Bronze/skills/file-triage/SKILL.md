# File Triage Skill

## Overview
This skill enables the AI employee to process incoming task documents in the form of markdown files, analyze their content, and appropriately categorize them based on actionability.

## Prerequisites
- Access to the vault file system
- Ability to read and write markdown files
- Basic natural language processing capabilities

## Process Flow

### Step 1: Read Incoming Task
1. Monitor the `vault/Inbox/` directory for new markdown (.md) files
2. When a new file appears, read its entire content
3. Extract the title (first H1 heading) and body content
4. Note the filename as the task identifier

### Step 2: Summarize the Task
1. Identify the main objective of the task
2. Extract key requirements or deliverables
3. Note any deadlines, priorities, or constraints mentioned
4. Create a brief summary (2-3 sentences) that captures the essence of the task
5. Format the summary as: "Task: [brief description]. Requires: [key elements]. Priority: [high/medium/low based on urgency cues]"

### Step 3: Decision Making
Evaluate the task using these criteria:

#### Route to Needs_Action if:
- The task requires multi-step execution
- Information gathering is needed
- External resources must be consulted
- The task involves creation, modification, or analysis
- Human approval is required before completion
- The task has dependencies

#### Route to Done if:
- The task is purely informational
- The task is already completed based on available information
- The task is invalid or spam
- The task is a duplicate of an existing entry
- The task is a simple acknowledgment that requires no follow-up

### Step 4: Write Output File
Based on your decision, create an output file in the appropriate directory:

#### For Needs_Action folder:
```
# [Original Title] - ACTION REQUIRED

## Summary
[Your summary from Step 2]

## Original Content
[Include the original content from the Inbox file]

## Recommended Actions
- [Action item 1]
- [Action item 2]
- [Action item 3]

## Estimated Time
[Time estimate based on complexity]

## Priority
[High/Medium/Low]
```

#### For Done folder:
```
# [Original Title] - COMPLETED/RESOLVED

## Summary
[Your summary from Step 2]

## Resolution
[Explanation of why this was categorized as Done]

## Original Content
[Include the original content from the Inbox file]
```

### Step 5: File Naming Convention
- Use the same base name as the original file
- Prepend "triaged_" to the filename
- Maintain the .md extension

## Quality Checks
- Ensure the summary accurately reflects the original content
- Verify the correct destination folder was chosen
- Confirm the output file follows the required format
- Check that no sensitive information was inadvertently included