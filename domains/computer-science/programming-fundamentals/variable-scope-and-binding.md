---
id: variable-scope-and-binding
title: Variable Scope and Variable Binding
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: variable-declaration-syntax
  type: hard
- id: parameters-and-arguments
  type: hard
builds-toward:
- recursion-and-recursive-calls
tags:
- scope
- binding
- variables
stage: abstract-reasoning
status: draft
---

# Variable Scope and Variable Binding

## Core Idea
A variable's scope is the region of code where it can be accessed. Local variables (in functions) exist only within their scope; global variables exist throughout. Shadowing occurs when an inner scope defines a variable with the same name as an outer scope.

## How It's Best Learned
Create local and global variables. Try accessing variables outside their scope (observe errors). Create variable shadowing and trace which variable is referenced.

## Common Misconceptions
- Local and global variables with the same name are the same (they're distinct; the inner one shadows the outer).
- A local variable persists after the function returns (local variables are destroyed when the function exits).
