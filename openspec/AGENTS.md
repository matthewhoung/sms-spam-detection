# OpenSpec Agent Workflow Guide

## Introduction

This document describes how to work with AI coding agents (like Claude Code) on the SMS Spam Detection project using OpenSpec methodology. OpenSpec provides a structured, specification-driven approach to software development that enables clear communication between humans and AI agents.

## What is OpenSpec?

OpenSpec is a lightweight documentation framework that uses:
- **YAML-based change proposals** for tracking features and fixes
- **Schema definitions** for data structures
- **Project-level specifications** for architecture and conventions
- **Agent-friendly workflows** for collaborative development

### Benefits
- Clear change history and feature tracking
- Structured proposals that AI agents can understand
- Self-documenting codebase
- Easy collaboration between developers and AI

## Core Concepts

### 1. Change Proposals

Every feature, bug fix, or enhancement starts with a **change proposal** - a YAML file that describes:
- **What** is being changed
- **Why** it's needed
- **How** it's implemented
- **Status** of the change

### 2. Change Lifecycle

```
proposed → in_progress → implemented → (optional) deprecated
```

- **proposed:** Change is documented but not started
- **in_progress:** Currently being worked on
- **implemented:** Completed and merged into codebase
- **deprecated:** Feature removed or replaced (keep for history)

### 3. Directory Structure

```
openspec/
├── project.md                    # Master project documentation
├── AGENTS.md                     # This file (agent workflow guide)
├── changes/                      # All change proposals
│   ├── add-spam-detector/        # Example implemented change
│   │   ├── change.yaml           # Change specification
│   │   └── (optional) notes.md   # Additional context
│   └── add-batch-upload/         # Example new feature
│       └── change.yaml
├── schemas/                      # Data structure definitions
│   └── prediction.yaml           # Spam prediction response schema
└── templates/                    # Reusable templates
    └── change-template.yaml      # Template for new changes
```

## Working with AI Agents

### Step 1: Propose a Change

When you want to add a feature or fix a bug, create a change proposal.

**Example Request to Agent:**
```
"I want to add a batch upload feature for CSV files.
Please create an OpenSpec change proposal for this."
```

**Agent Will:**
1. Create directory: `openspec/changes/add-batch-upload/`
2. Write `change.yaml` with structured specification
3. Mark status as `proposed`
4. Ask for clarification if needed

### Step 2: Review and Refine

Review the generated change proposal and discuss with the agent:

```
"Can you add support for Excel files too?"
"What about error handling for malformed files?"
```

Agent will update the proposal before implementation.

### Step 3: Implement the Change

Once you approve the proposal:

```
"Please implement the batch upload feature as proposed."
```

**Agent Will:**
1. Update change status to `in_progress`
2. Create/modify necessary files
3. Follow coding conventions from `project.md`
4. Test the implementation
5. Update status to `implemented`

### Step 4: Document and Close

After successful implementation:
- Agent marks change as `implemented` in YAML
- Updates any affected schemas
- May suggest related follow-up changes

## Change Proposal Template

Every change proposal should include:

```yaml
title: Short descriptive title
type: feature | bugfix | enhancement | refactor | docs
status: proposed | in_progress | implemented | deprecated
created: YYYY-MM-DD
author: Your Name

description: |
  Detailed description of what this change does and why it's needed.
  Can span multiple lines.

components:
  - name: ComponentName
    type: module | class | function | file
    file: path/to/file.py
    description: What this component does

features:  # For new features
  - Feature point 1
  - Feature point 2

changes:  # For modifications
  - What changed in component A
  - What changed in component B

dependencies:  # Optional
  - New library dependencies
  - Changed requirements

testing:  # Optional
  - How to test this change
  - Expected behavior

notes: |  # Optional
  Additional context, decisions, or future considerations
```

## Common Workflows

### Adding a New Feature

```markdown
You: "I want to add an API endpoint for spam detection"

Agent: Creates proposal at openspec/changes/add-api-endpoint/change.yaml

You: Reviews and approves

Agent:
1. Updates status to 'in_progress'
2. Creates new file (e.g., api/endpoints.py)
3. Updates dependencies if needed
4. Tests the endpoint
5. Marks as 'implemented'

You: Verifies the implementation
```

### Fixing a Bug

```markdown
You: "The confidence score shows wrong percentage. Please create a fix proposal"

Agent: Creates openspec/changes/fix-confidence-calculation/change.yaml
        with type: bugfix, describes the issue

You: "Looks good, please fix it"

Agent: Implements the fix and updates status to 'implemented'
```

### Refactoring Code

```markdown
You: "Let's refactor the model loading logic into a separate module"

Agent: Creates proposal with type: refactor

You: Approves

Agent:
1. Creates new module (e.g., utils/model_loader.py)
2. Moves logic
3. Updates imports
4. Ensures no functionality breaks
```

## Agent Interaction Tips

### Be Specific
Good: "Add CSV batch upload with error handling and progress bar"
Bad: "Make it better"

### Reference Existing Docs
Good: "Following the conventions in project.md, add feature X"
Bad: "Add feature X" (agent may not follow conventions)

### Ask for Proposals First
Good: "Create a change proposal for feature X, let me review before implementing"
Bad: "Just add feature X" (agent might miss important considerations)

### Use Change Status
Good: "Show me all 'proposed' changes and let's prioritize them"
This helps track what's planned vs. what's done.

### Request Context
Good: "Read openspec/project.md and then propose a new feature that fits our architecture"
Agent will align with existing patterns.

## Best Practices

### 1. One Change Per Proposal
Don't combine multiple unrelated changes in one proposal. Better to have:
- `add-batch-upload/change.yaml`
- `add-export-results/change.yaml`

Rather than:
- `multiple-features/change.yaml`

### 2. Update Status Promptly
Keep change statuses current:
- Mark `in_progress` when starting work
- Mark `implemented` immediately after completion
- Never leave stale `in_progress` changes

### 3. Use Descriptive Names
Good: `add-model-retraining-ui`
Bad: `feature-1`, `new-stuff`

### 4. Reference Related Changes
In your change YAML:
```yaml
related_changes:
  - changes/add-batch-upload  # Builds on this
  - changes/fix-confidence-calculation  # Required for this to work
```

### 5. Keep Schemas Updated
When you change data structures, update corresponding schema files:
- `openspec/schemas/prediction.yaml`
- `openspec/schemas/batch_result.yaml` (if added)

### 6. Archive Old Changes
Don't delete deprecated changes - they're part of your project history:
```yaml
status: deprecated
deprecated_date: 2025-11-01
replaced_by: changes/add-new-batch-system
reason: Performance issues, replaced with async version
```

## Example Agent Commands

### View Project Status
```
"Show me all implemented changes"
"What features are currently in progress?"
"List all proposed changes so I can prioritize"
```

### Create Changes
```
"Create a change proposal for adding user authentication"
"Propose a fix for the memory leak in model loading"
"Draft a refactoring proposal for the preprocessing pipeline"
```

### Implement Changes
```
"Implement the change in openspec/changes/add-batch-upload/"
"Start working on the proposed API endpoint feature"
```

### Update Documentation
```
"Update project.md with the new batch processing architecture"
"Add the new BatchResult schema to openspec/schemas/"
```

## Schema Definitions

Schemas in `openspec/schemas/` define data structures using OpenAPI-like YAML:

```yaml
name: SpamPrediction
description: SMS spam prediction response
type: object
properties:
  text:
    type: string
    description: Input SMS message
  prediction:
    type: string
    enum: [spam, ham]
  spam_probability:
    type: number
    minimum: 0
    maximum: 1
required:
  - text
  - prediction
```

**When to Create Schemas:**
- API request/response formats
- Database models
- Configuration structures
- Complex data objects passed between modules

## Continuous Improvement

The OpenSpec system itself can evolve:

```
"I think we should add a 'priority' field to change proposals.
Can you update the template and AGENTS.md?"
```

Agent will:
1. Update `templates/change-template.yaml`
2. Update this `AGENTS.md` documentation
3. Optionally backfill existing changes if requested

## Troubleshooting

### Agent Not Following Conventions
→ Explicitly reference: "Following conventions in openspec/project.md, please..."

### Change History Getting Messy
→ Periodically review and archive: "Move all implemented changes from before 2025-10 to an archive/"

### Agent Forgets Context
→ Always reference the relevant change: "Implement the feature described in openspec/changes/add-batch-upload/change.yaml"

### Conflicting Changes
→ Use `related_changes` field to track dependencies and order

## Quick Reference

| Task | Command Example |
|------|----------------|
| Propose feature | "Create OpenSpec proposal for [feature]" |
| View changes | "List all changes in openspec/changes/" |
| Implement | "Implement the [name] change proposal" |
| Update docs | "Update project.md with [new info]" |
| Create schema | "Define a schema for [data structure]" |
| Get status | "What's the status of [change]?" |

---

## Getting Started Checklist

- [x] Read `openspec/project.md` to understand the codebase
- [x] Review example change in `openspec/changes/add-spam-detector/`
- [x] Check existing schemas in `openspec/schemas/`
- [ ] Create your first change proposal using the template
- [ ] Get agent feedback on the proposal
- [ ] Approve and implement the change
- [ ] Mark as implemented and test

## Additional Resources

- **Project Specification:** [project.md](./project.md)
- **Change Template:** [templates/change-template.yaml](./templates/change-template.yaml)
- **Example Change:** [changes/add-spam-detector/change.yaml](./changes/add-spam-detector/change.yaml)
- **Main README:** [../README.md](../README.md)

---

**Last Updated:** 2025-10-27
**Maintained By:** Matthew Hong

**Questions?** Ask your AI agent: "Explain the OpenSpec workflow from openspec/AGENTS.md"
