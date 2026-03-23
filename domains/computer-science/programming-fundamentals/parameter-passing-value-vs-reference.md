---
id: parameter-passing-value-vs-reference
title: "Parameter Passing: Value vs. Reference"
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: parameters-and-arguments
  type: hard
- id: scope-shadowing-and-lifetime
  type: soft
builds-toward:
- function-design-and-contracts
tags:
- functions
- parameters
- memory
stage: formal-systems
status: validated
---
# Parameter Passing: Value vs. Reference

## Core Idea
Pass-by-value creates a copy; changes inside the function don't affect the original. Pass-by-reference passes the actual variable; changes are visible outside. Some languages default to one, others allow choosing (ref, &). Understanding which applies prevents bugs.

## How It's Best Learned
Modify parameters inside functions and check if the original changed; test with different types (primitives vs objects); use language-specific tools to track memory.

## Common Misconceptions
That all languages use the same passing strategy (they don't); that pass-by-reference is always better (pass-by-value is safer); that objects and primitives follow the same rules (often they don't).

## Questions

```yaml
- question: "In Python, `def f(lst): lst.append(99)` is called with `mylist = [1, 2, 3]; f(mylist)`. What does `mylist` contain after the call?"
  type: multiple-choice
  options:
    - "[1, 2, 3] — Python uses pass-by-value, so the function received a copy of the list"
    - "[1, 2, 3, 99] — the function mutated the shared object through the copied reference"
    - "It depends on whether mylist was declared global inside the function"
    - "[99] — appending inside a function replaces the original list"
  answer: 1
  explanation: "Python passes a copy of the *reference* (pointer) to the list, not a copy of the list itself. Both `lst` inside the function and `mylist` in the caller point to the same list object in memory. When `lst.append(99)` mutates that object, the change is visible through both references. This is 'pass-by-object-reference': the reference is copied, but the object is shared. Note that option A is wrong because Python does NOT copy the list — only the reference to it is copied."

- question: "In Python, `def g(lst): lst = [10, 20, 30]` is called with `mylist = [1, 2, 3]; g(mylist)`. What does `mylist` contain after the call?"
  type: multiple-choice
  options:
    - "[10, 20, 30] — reassignment inside the function replaces the caller's list"
    - "[1, 2, 3] — reassignment rebinds only the local parameter; the caller's reference is unaffected"
    - "[] — reassignment always clears the original list before binding to the new one"
    - "[1, 2, 3, 10, 20, 30] — reassignment concatenates to the original list"
  answer: 1
  explanation: "This is the essential contrast with the previous scenario. When the function executes `lst = [10, 20, 30]`, it rebinds the local parameter `lst` to point at a new list object. This only changes where the function's local copy of the reference points — the caller's `mylist` variable still points at the original list [1, 2, 3], which is unchanged. The key distinction: mutating an object (append, in-place modification) affects the caller; reassigning the parameter does not."

- question: "In pass-by-value, modifying the parameter variable inside the function changes the original variable in the caller."
  type: true-false
  answer: false
  explanation: "Pass-by-value means the function receives an independent copy of the argument's value. The parameter and the caller's variable are completely separate — they happen to start with the same value, but modifications to one do not affect the other. This is like photocopying a document: writing on the copy leaves the original untouched. In C, all primitive parameters are passed by value. In Python, immutable objects like integers behave analogously — you cannot change a 5 to a 6 by modifying the function's copy."

- question: "In Python and Java, when an object is passed to a function, the reference to that object is passed by value — meaning the function can mutate the object's contents but cannot redirect the caller's variable to a different object."
  type: true-false
  answer: true
  explanation: "This is the defining characteristic of 'pass-by-object-reference' (also called 'pass-by-sharing'). The function receives a copy of the pointer/reference to the object. Because both the caller and the function hold references to the same object, mutations through either reference are visible to both. But if the function rebinds its local parameter to point at a new object, it is only changing its own copy of the reference — the caller's variable still points at the original. This explains why `lst.append(1)` modifies the caller's list but `lst = []` does not."

- question: "Explain the difference between mutating an object and reassigning a parameter in Python. Why does one affect the caller but not the other?"
  type: short-answer
  answer: "In Python, a function parameter receives a copy of the reference (pointer) to the object, not a copy of the object itself. If the function mutates the object through that reference — by calling a method like append() or modifying an attribute — both the function and the caller see the change, because they share the same underlying object. But if the function reassigns the parameter to a new object (e.g., lst = []), it only redirects its own local copy of the reference. The caller's variable still points at the original object, which is unmodified. The rule: shared object, copied reference."
  explanation: "This distinction is the source of most parameter-passing confusion in Python. The mental model to internalize: Python always passes the reference by value. 'By value' means the reference copy is independent of the caller's variable — reassignment doesn't propagate back. 'Shared object' means mutations through the reference do propagate back, because both sides are looking at the same memory location."
```

## Explainer

From your work with function parameters, you know that functions receive data through their parameter list. But what exactly happens when you pass a variable to a function? Does the function get its own copy, or does it get access to the original? The answer determines whether changes made inside the function are visible to the caller, and getting this wrong is one of the most common sources of subtle bugs.

**Pass-by-value** means the function receives a *copy* of the argument's value. The parameter inside the function is a completely independent variable that happens to start with the same value. If the function modifies its parameter, the original variable in the caller is unaffected. Think of it like photocopying a document and handing someone the copy — they can scribble all over it, and your original is untouched. In C, all parameters are passed by value by default. In Python, integers and strings behave this way because they are immutable — the function cannot modify the original object even though it has a reference to it.

**Pass-by-reference** means the function receives a direct handle to the original variable, not a copy. Any changes the function makes to the parameter are immediately visible to the caller. In C++, you opt into this with the `&` syntax: `void increment(int &x) { x++; }` will actually modify the caller's variable. This is powerful — it lets functions return multiple results by modifying their parameters, and it avoids the cost of copying large data structures. But it is also dangerous, because any function call might silently change your variables. When debugging, pass-by-reference means you cannot assume a variable's value is unchanged after a function call without checking.

Many languages use a third strategy that confuses beginners: **pass-by-object-reference** (sometimes called pass-by-sharing). In Python and Java, when you pass a list or object, the function receives a copy of the *reference* (pointer) to the object, not a copy of the object itself. This means the function can modify the object's contents (append to a list, change a field), and the caller sees those changes. But if the function reassigns the parameter to a completely new object, the caller's variable still points to the original. This is why `def f(lst): lst.append(1)` modifies the caller's list, but `def f(lst): lst = [1, 2, 3]` does not. Understanding this distinction — "the reference is copied, but the object is shared" — resolves most of the confusion about parameter passing in modern languages.
