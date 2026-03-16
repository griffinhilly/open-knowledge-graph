---
id: variable-scope
title: Variable Scope
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: functions-defining-calling
  type: hard
- id: return-values
  type: soft
builds-toward:
- recursion-basics
- intro-to-classes
tags:
- scope
- local
- global
- namespace
- encapsulation
stage: abstract-reasoning
status: validated
---

# Variable Scope

## Core Idea
Scope defines where in a program a variable is visible and accessible. Local variables exist only inside the function where they are created; global variables are accessible throughout the program. Each function call creates its own local scope (a new set of variable bindings), which is discarded when the function returns. Limiting the scope of variables reduces unintended interactions between parts of a program and makes code easier to reason about.

## How It's Best Learned
Write functions that use the same variable name as a global and observe which takes precedence. Use a debugger or print statements to show variable values at different points in the call stack.

## Common Misconceptions
- Assuming a variable created inside a function is accessible outside it.
- Using global variables when a parameter would be cleaner and safer.
- Confusing the value of a variable at definition time with its value at call time.

## Explainer

When you started writing functions, you learned that parameters become local variables inside the function body. **Variable scope** generalizes this idea: it defines the boundaries of where each variable exists and can be accessed. Think of scope as walls around your variables — code inside the walls can see and use the variable, but code outside cannot. This boundary system is what keeps large programs manageable, because it prevents one function from accidentally interfering with another's data.

A **local variable** is any variable created inside a function (including its parameters). It comes into existence when the function is called and is destroyed when the function returns. If you define `x = 10` inside a function called `calculate()`, that `x` does not exist anywhere outside `calculate()` — trying to use it elsewhere raises a `NameError`. Critically, each *call* to a function gets its own fresh set of local variables. If `calculate()` calls itself recursively (which you'll learn about soon), each invocation has its own independent `x`. This isolation is what makes functions reliable: you can call them from anywhere without worrying about what variable names they use internally.

A **global variable** is one defined at the top level of your program, outside any function. Global variables are visible everywhere — any function can read them. However, if a function tries to *assign* to a global variable, Python creates a new local variable with the same name instead, which shadows the global. To actually modify the global, you'd need the `global` keyword — but this is almost always a sign of poor design. The problem with relying on globals is that any function can change them at any time, making it hard to predict your program's behavior. When a bug appears, you'd have to check every function in the program to figure out what changed the global.

The practical rule is straightforward: **pass data into functions as arguments and get results back through return values**. This keeps each function self-contained — its behavior depends only on its inputs, not on hidden external state. When you encounter code where a function reads and modifies global variables, the function becomes unpredictable: its behavior depends on when it's called and what other functions have run before it. Scope discipline — keeping variables as local as possible — is one of the foundational habits that separates clean, debuggable code from tangled, fragile code. This same principle of isolating state will reappear when you learn about classes and encapsulation.
