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

## Questions

```yaml
- question: "A function contains the line count = 0. There is also a global variable named count with a value of 10. After calling the function, what is the value of the global count?"
  type: multiple-choice
  options:
    - "0, because the function's assignment overwrites the global"
    - "10, because the function creates its own local count that is completely independent of the global"
    - "An error is raised because count is already defined globally"
    - "Undefined, because the function destroys the global when it creates a local with the same name"
  answer: 1
  explanation: "When a function assigns to a name, Python creates a new local variable — it does not modify any global with the same name. The global count remains 10, completely untouched. The function's local count (set to 0) exists only during that function call and is discarded when the function returns. This is why relying on globals for shared state creates bugs: you might call a function expecting it to change a global, and nothing happens to it."

- question: "The same function is called twice in a row: process(5) then process(10). What is true about the local variables inside process()?"
  type: multiple-choice
  options:
    - "Both calls share the same local variables, so the second call can see values left by the first"
    - "Each call gets its own fresh, independent set of local variables"
    - "The second call inherits the local variable values from the first call"
    - "Local variables are only created on the first call; subsequent calls reuse them"
  answer: 1
  explanation: "Each function call creates its own scope — a fresh, independent set of variable bindings. The second call to process() has no awareness of what the first call did to its locals. This isolation is fundamental: it's what makes functions reusable and predictable. If calls shared state, calling a function from two different places could produce different results depending on the order of calls, making the program extremely difficult to reason about."

- question: "A local variable x defined inside function_a and a local variable x defined inside function_b refer to the same memory location."
  type: true-false
  answer: false
  explanation: "They are completely separate variables that happen to share a name. Each function has its own scope, and x in function_a is entirely independent of x in function_b. This is the entire point of scope: functions can use whatever variable names make sense internally without worrying about name collisions with other functions. If they did share memory, calling any function that used the name x would corrupt the x in every other function currently executing."

- question: "A function that reads and modifies a global variable is harder to debug than a function that only uses parameters and return values."
  type: true-false
  answer: true
  explanation: "A function's behavior depends on its inputs. If those inputs are only the parameters, you can understand the function by reading it in isolation. If the function also reads or modifies globals, its behavior depends on the entire history of what every other function has done to those globals before this one was called. To debug a bug in that function, you'd have to trace all possible execution paths that could have changed the global. Local-only functions are self-contained: same inputs always produce same outputs, making both testing and debugging straightforward."

- question: "Why does limiting variable scope — keeping variables as local as possible — make programs easier to debug and reason about?"
  type: short-answer
  answer: "When a variable is local to a function, its entire existence is confined to that function's body. You can understand its full lifecycle — where it's created, what changes it, where it's used — by reading only that function. By contrast, a global variable can be read or written by any code in the entire program at any time, so debugging a problem with it requires searching everywhere. Local scope reduces the search space for bugs to a bounded region. It also makes functions predictable: given the same arguments, a function with only local variables always returns the same result, regardless of what other functions have run."
  explanation: "This principle — minimize scope — is one reason object-oriented programming and functional programming both emphasize encapsulation and pure functions respectively. The goal is the same: limit the number of things that can affect a variable's value, so that the programmer can hold the relevant context in their head when reading any given piece of code."
```

## Explainer

When you started writing functions, you learned that parameters become local variables inside the function body. **Variable scope** generalizes this idea: it defines the boundaries of where each variable exists and can be accessed. Think of scope as walls around your variables — code inside the walls can see and use the variable, but code outside cannot. This boundary system is what keeps large programs manageable, because it prevents one function from accidentally interfering with another's data.

A **local variable** is any variable created inside a function (including its parameters). It comes into existence when the function is called and is destroyed when the function returns. If you define `x = 10` inside a function called `calculate()`, that `x` does not exist anywhere outside `calculate()` — trying to use it elsewhere raises a `NameError`. Critically, each *call* to a function gets its own fresh set of local variables. If `calculate()` calls itself recursively (which you'll learn about soon), each invocation has its own independent `x`. This isolation is what makes functions reliable: you can call them from anywhere without worrying about what variable names they use internally.

A **global variable** is one defined at the top level of your program, outside any function. Global variables are visible everywhere — any function can read them. However, if a function tries to *assign* to a global variable, Python creates a new local variable with the same name instead, which shadows the global. To actually modify the global, you'd need the `global` keyword — but this is almost always a sign of poor design. The problem with relying on globals is that any function can change them at any time, making it hard to predict your program's behavior. When a bug appears, you'd have to check every function in the program to figure out what changed the global.

The practical rule is straightforward: **pass data into functions as arguments and get results back through return values**. This keeps each function self-contained — its behavior depends only on its inputs, not on hidden external state. When you encounter code where a function reads and modifies global variables, the function becomes unpredictable: its behavior depends on when it's called and what other functions have run before it. Scope discipline — keeping variables as local as possible — is one of the foundational habits that separates clean, debuggable code from tangled, fragile code. This same principle of isolating state will reappear when you learn about classes and encapsulation.
