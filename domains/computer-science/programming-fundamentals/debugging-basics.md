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
status: validated
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

## Explainer

Every programmer spends significant time debugging, and the difference between a frustrating hour and a productive five minutes usually comes down to approach. Debugging is not random guessing — it is a systematic process that resembles the scientific method. You observe a symptom (wrong output, a crash, unexpected behavior), form a **hypothesis** about what is causing it, design a test to confirm or refute that hypothesis, and repeat until you find the root cause. The worst debugging habit is changing code at random hoping something will work. The best habit is asking: "What do I *expect* to happen at this line, and what is *actually* happening?"

The first skill is **reading error messages carefully**. A syntax error message tells you what the interpreter expected and where it got confused. A runtime error like `IndexError: list index out of range` tells you both the type of problem (you accessed a position that does not exist) and the exact line it occurred on. A **stack trace** shows you the chain of function calls that led to the error — read it from bottom to top. The bottom line shows *what* went wrong; the lines above show *how the program got there*. Often the real bug is not at the crash site but several function calls earlier, where bad data was created and then passed along.

**Print debugging** is the simplest and most universally available technique. When you do not understand what your code is doing, add print statements to display variable values at key points: before and after a loop, at the start of a function, right before the line that crashes. Compare what the variables *actually contain* to what you *expected*. This narrows the problem from "somewhere in my program" to "between line 14 and line 22, the variable `total` becomes negative when it should not." Once you have found the mismatch between expectation and reality, the fix is usually clear.

For more complex programs, a **debugger** is far more powerful than print statements. A debugger lets you set **breakpoints** — lines where execution pauses so you can inspect every variable in scope, step through code one line at a time, and watch how state changes. Most IDEs have built-in debuggers with graphical interfaces. Learning to set a breakpoint and step through a loop iteration by iteration transforms your understanding of how code executes. Combined with the habit of forming hypotheses ("I think the loop runs one extra time"), the debugger lets you verify or disprove your theory in seconds rather than peppering your code with print statements and re-running it repeatedly.
