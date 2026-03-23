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
stage: formal-systems
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

## Questions

```yaml
- question: "A program defines a global variable `score = 100`. Inside a function, the first line is `score = 0`. After the function is called and returns, what is the value of the global `score`?"
  type: multiple-choice
  options:
    - "0 — the function modified the global variable"
    - "100 — the function created a new local variable named `score` that shadowed the global; the global is unchanged"
    - "Undefined — the global was overwritten and then destroyed when the function exited"
    - "An error — you cannot use the same name for both a local and a global variable"
  answer: 1
  explanation: "This is exactly the shadowing scenario. When the function executes `score = 0`, it creates a new local variable named `score` in the function's scope — it does not modify the global. The local binding shadows the global for the duration of the function, but the global is independent. When the function returns, the local `score` is destroyed, and the global `score = 100` is untouched. Option A is the classic misconception: assuming that assigning to a name inside a function changes the variable of the same name in the outer scope."

- question: "Why is keeping variables as local as possible generally considered good programming practice?"
  type: multiple-choice
  options:
    - "Local variables are faster to access than global variables in most programming languages"
    - "Local variables make programs shorter because they don't need to be declared at the top"
    - "Local variables give each function an independent workspace, preventing one function from accidentally affecting another's state and making code easier to test and reason about"
    - "Global variables are not available in all programming languages, so local variables are more portable"
  answer: 2
  explanation: "The key benefit of local variables is isolation: each function call gets its own fresh set of variables, independent of every other call and of the global state. This means a function cannot accidentally corrupt variables used by another function, two simultaneous calls to the same function run with completely separate state, and you can test a function in isolation without worrying about what global state it might read or modify. Global variables create invisible dependencies between parts of the program, making bugs harder to trace. Minimizing globals reduces the surface area for these hidden interactions."

- question: "A local variable declared inside a function is destroyed when the function returns and cannot be accessed after the function exits."
  type: true-false
  answer: true
  explanation: "Local variables exist only within the scope of the function — they are created when the function is called and destroyed when it returns. This is what 'scope' means in the temporal sense: the variable lives only as long as its enclosing function is executing. If you try to access a local variable from outside the function, the language will either throw an error (because the name is not in scope) or, in some cases, access a completely different variable with the same name in the outer scope. This is also what makes each function call independent — there is no persistence of local state between calls."

- question: "When a function uses a variable name that also exists as a global variable, the function reads and potentially modifies the global variable."
  type: true-false
  answer: false
  explanation: "If the function declares or assigns to a variable with that name, it creates a local binding that shadows the global — it neither reads nor modifies the global. The local binding is a separate variable that happens to share a name. The global is hidden from within that function's scope for as long as the local binding exists. (Note: some languages provide explicit mechanisms to explicitly reference a global from within a function, like Python's `global` keyword — but simply using the name does not do this by default.) The language always resolves names by checking local scope first."

- question: "Explain why variable shadowing does not modify the outer variable, and what mechanism ensures this independence."
  type: short-answer
  answer: "When a local variable is declared with the same name as an outer variable, the language creates a new, separate binding in the local scope. Name lookup proceeds from innermost to outermost scope, so all references to that name within the function resolve to the local binding — the outer variable is hidden but not modified. The local binding is a distinct memory location; writing to it has no effect on the outer variable's location. When the function exits, the local binding is destroyed, and the outer variable remains exactly as it was."
  explanation: "The independence is guaranteed by the scope chain and the fact that declaration creates a new binding rather than overwriting an existing one. Each scope has its own namespace. When you write `x = 0` inside a function, you are creating an entry for `x` in the function's local namespace — not reaching out to find an existing `x` elsewhere. The outer `x` is in a different namespace and is unaffected. This is what makes functions safe to reuse: their local variables are their own private state, shielded from and shielding the rest of the program."
```

## Explainer

You already know how to declare variables and how to pass arguments into function parameters. Now the crucial question is: when your code refers to a variable name, how does the language decide *which* variable that name points to? This is the problem of **scope** and **binding** — scope defines where a name is visible, and binding is the act of associating a name with a specific value or memory location.

Think of your program as a building with rooms. Each function is a room, and the top-level code is the lobby. When you declare a variable inside a function, it is like placing a labeled box in that room — only people inside that room can see it. A **local variable** exists only within its function's scope. When the function finishes, the room is cleared and the box is gone. A **global variable** is a labeled box in the lobby — visible from every room. When code inside a function refers to a variable name, the language first checks the current room (local scope), and only if it finds nothing does it look in the lobby (global scope). This lookup order is what determines which value a name resolves to.

**Shadowing** is what happens when a local variable has the same name as a global one. Suppose you have a global variable `count = 10` and inside a function you write `count = 0`. You have not changed the global — you have created a brand-new local variable that happens to share the name. Within that function, every reference to `count` sees the local version (value `0`); outside the function, `count` is still `10`. The local binding **shadows** the global one, hiding it for the duration of that scope. This is a common source of confusion, but the rule is consistent: the most local binding always wins.

Understanding scope and binding is essential because it determines the independence of your functions. When you call a function, it gets its own fresh set of local variables. This means two calls to the same function run with completely separate local state — one call cannot accidentally corrupt the variables of another. This property is what makes functions safe to reuse and is foundational to recursion, where a function calls itself and each invocation needs its own independent workspace. The habit of keeping variables as local as possible — minimizing your use of globals — leads directly to code that is easier to reason about, test, and debug.
