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
- testing-and-validation-basics
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

## Questions

```yaml
- question: "A Python program crashes with 'IndexError: list index out of range' on line 47. A student goes directly to line 47 and fixes the index access, but the bug persists. What is the most likely explanation?"
  type: multiple-choice
  options:
    - "The student forgot to save the file before re-running"
    - "IndexError cannot be fixed by changing the index — a different data structure is needed"
    - "The error message is unreliable and the real crash site is elsewhere"
    - "Line 47 is where bad data arrived and crashed, but the bug that created the bad data is earlier in the code"
  answer: 3
  explanation: "Runtime error messages point to where the program crashed, not necessarily where the bug originated. Bad data can be created many lines or function calls earlier and only cause a crash when it's finally used in an incompatible way. Reading the full stack trace — which shows the chain of calls leading to the crash — and forming a hypothesis about where the corrupted value was first produced is more effective than patching only the crash site."

- question: "A programmer's function produces wrong output. She adds a print statement just before the function returns and sees the value looks correct at that point. What should she conclude?"
  type: multiple-choice
  options:
    - "The function's algorithm is definitely wrong and needs to be rewritten"
    - "The print confirms the bug is in this function; she should add more prints inside it"
    - "The function appears correct; the bug is likely in how the return value is used downstream"
    - "Print debugging is unreliable and she should switch to a debugger immediately"
  answer: 2
  explanation: "Print debugging works by narrowing down where the discrepancy first appears. If the value is correct at the return point, the function is not corrupting it — the bug is downstream, in whoever calls this function and uses its result. The print has successfully ruled out this function as the source. The next step is to check how the return value is handled by the calling code."

- question: "When reading a Python stack trace, the most useful information about the root cause is usually found on the last line printed."
  type: true-false
  answer: false
  explanation: "The last line shows the error type and the crash site — what went wrong and where execution stopped. But the earlier lines in the traceback show the chain of function calls that led there. The real bug is often several calls back, where bad data was first created and then passed along until it eventually caused a crash. Reading only the last line is one of the most common beginner debugging mistakes: it addresses the symptom but misses the cause."

- question: "A logic error is harder to detect than a syntax error because the program runs to completion and only reveals itself through wrong output, not a crash."
  type: true-false
  answer: true
  explanation: "Syntax errors are caught before the program even runs — the interpreter refuses to execute. Runtime errors crash the program and produce an error message pointing to the failure. Logic errors are the sneakiest: the program executes successfully from start to finish and produces output, but the output is wrong. There is no error message, no crash, and no obvious indicator of where the reasoning went astray. Detecting them requires knowing what the correct output should be and systematically tracing where the program's actual behavior diverges from expected behavior."

- question: "Why is forming a hypothesis before changing code the habit that separates effective debugging from ineffective debugging?"
  type: short-answer
  answer: "Without a hypothesis, code changes are random guesses — they might accidentally fix a symptom while leaving the root cause intact, or introduce new bugs. A hypothesis ('I think the loop runs one extra iteration because the condition should be < not <=') is a testable prediction: if it's correct, I'd expect the variable to equal X at this breakpoint. When confirmed, you've found the bug and understand why the fix works. When refuted, you've learned something and can form a better hypothesis. Random changes teach you nothing about your program and often make things worse."
  explanation: "The scientific method — observe, hypothesize, test, revise — maps directly onto debugging. Good debuggers form explicit predictions and then design tests (print statements, breakpoints, edge-case inputs) that would confirm or disprove them. This systematic approach converts an intimidating problem ('my program is wrong somewhere') into a series of focused, answerable questions about specific variables at specific points in execution."
```

## Explainer

Every programmer spends significant time debugging, and the difference between a frustrating hour and a productive five minutes usually comes down to approach. Debugging is not random guessing — it is a systematic process that resembles the scientific method. You observe a symptom (wrong output, a crash, unexpected behavior), form a **hypothesis** about what is causing it, design a test to confirm or refute that hypothesis, and repeat until you find the root cause. The worst debugging habit is changing code at random hoping something will work. The best habit is asking: "What do I *expect* to happen at this line, and what is *actually* happening?"

The first skill is **reading error messages carefully**. A syntax error message tells you what the interpreter expected and where it got confused. A runtime error like `IndexError: list index out of range` tells you both the type of problem (you accessed a position that does not exist) and the exact line it occurred on. A **stack trace** shows you the chain of function calls that led to the error — read it from bottom to top. The bottom line shows *what* went wrong; the lines above show *how the program got there*. Often the real bug is not at the crash site but several function calls earlier, where bad data was created and then passed along.

**Print debugging** is the simplest and most universally available technique. When you do not understand what your code is doing, add print statements to display variable values at key points: before and after a loop, at the start of a function, right before the line that crashes. Compare what the variables *actually contain* to what you *expected*. This narrows the problem from "somewhere in my program" to "between line 14 and line 22, the variable `total` becomes negative when it should not." Once you have found the mismatch between expectation and reality, the fix is usually clear.

For more complex programs, a **debugger** is far more powerful than print statements. A debugger lets you set **breakpoints** — lines where execution pauses so you can inspect every variable in scope, step through code one line at a time, and watch how state changes. Most IDEs have built-in debuggers with graphical interfaces. Learning to set a breakpoint and step through a loop iteration by iteration transforms your understanding of how code executes. Combined with the habit of forming hypotheses ("I think the loop runs one extra time"), the debugger lets you verify or disprove your theory in seconds rather than peppering your code with print statements and re-running it repeatedly.
