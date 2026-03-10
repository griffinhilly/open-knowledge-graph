---
id: debugging-basics
title: Debugging Basics
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: functions-defining-calling
  type: soft
- id: conditional-statements
  type: soft
builds-toward:
- error-handling-exceptions
- algorithm-design-basics
tags:
- debugging
- errors
- tracing
- print debugging
- breakpoints
stage: abstract-reasoning
status: draft
---

# Debugging Basics

## Core Idea
Debugging is the systematic process of identifying and fixing errors (bugs) in code. Syntax errors prevent the program from running and are reported by the interpreter or compiler with a location. Runtime errors occur during execution (e.g., division by zero, index out of bounds). Logic errors produce wrong output without crashing. Effective debugging strategies include reading error messages carefully, adding print statements to inspect values, tracing execution by hand, and using a debugger with breakpoints.

## How It's Best Learned
Deliberately introduce errors into working programs and practice diagnosing them. Use a debugger to step through code line by line. Practice reading stack traces to locate the source of runtime errors.

## Common Misconceptions
- Reading only the last line of an error traceback — often the most useful context is earlier in the stack.
- Randomly changing code hoping to fix a bug rather than forming a hypothesis and testing it.
- Assuming the line the interpreter reports as an error is always where the logical mistake is.
