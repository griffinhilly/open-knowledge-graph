---
id: switch-statements
title: Switch Statements and Case Selection
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: else-if-chains
  type: hard
tags:
- control-flow
- conditionals
- switch
stage: abstract-reasoning
status: draft
---

# Switch Statements and Case Selection

## Core Idea
A switch statement compares a value against multiple cases and jumps to the matching case. Fall-through behavior (without break) allows multiple cases to share code. Switch is cleaner than else-if for discrete value matching.

## How It's Best Learned
Convert an else-if chain to a switch. Test fall-through with and without break statements.

## Common Misconceptions
- Switch only works with numbers (many languages support strings and other types).
- Cases without break are always errors (fall-through can be intentional and useful).
