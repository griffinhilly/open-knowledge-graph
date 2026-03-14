---
id: call-stack-and-function-calls
title: Call Stack and Function Call Execution
domain: computer-science
course: programming-fundamentals
prerequisites:
- variable-scope-and-binding
builds-toward:
- recursion-and-recursive-calls
tags:
- functions
- call-stack
- execution
stage: abstract-reasoning
status: draft
---

# Call Stack and Function Call Execution

## Core Idea
When a function is called, a new stack frame is created containing the function's parameters and local variables. The call stack tracks active function calls in order. When a function returns, its frame is removed. Understanding the call stack explains variable scope and function behavior.

## How It's Best Learned
Trace function calls step-by-step, noting when stack frames are created and destroyed. Use a debugger to visualize the call stack.

## Common Misconceptions
- The call stack is unlimited (it has finite size; deep recursion can overflow the stack).
- All variables are on the call stack (some are on the heap or in registers, depending on the implementation).
