---
id: parameter-passing-value-vs-reference
title: 'Parameter Passing: Value vs. Reference'
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: function-parameters-passing-data
  type: hard
- id: scope-shadowing-and-lifetime
  type: soft
builds-toward:
- function-design-and-contracts
tags:
- functions
- parameters
- memory
stage: abstract-reasoning
status: draft
---

# Parameter Passing: Value vs. Reference

## Core Idea
Pass-by-value creates a copy; changes inside the function don't affect the original. Pass-by-reference passes the actual variable; changes are visible outside. Some languages default to one, others allow choosing (ref, &). Understanding which applies prevents bugs.

## How It's Best Learned
Modify parameters inside functions and check if the original changed; test with different types (primitives vs objects); use language-specific tools to track memory.

## Common Misconceptions
That all languages use the same passing strategy (they don't); that pass-by-reference is always better (pass-by-value is safer); that objects and primitives follow the same rules (often they don't).

## Explainer

From your work with function parameters, you know that functions receive data through their parameter list. But what exactly happens when you pass a variable to a function? Does the function get its own copy, or does it get access to the original? The answer determines whether changes made inside the function are visible to the caller, and getting this wrong is one of the most common sources of subtle bugs.

**Pass-by-value** means the function receives a *copy* of the argument's value. The parameter inside the function is a completely independent variable that happens to start with the same value. If the function modifies its parameter, the original variable in the caller is unaffected. Think of it like photocopying a document and handing someone the copy — they can scribble all over it, and your original is untouched. In C, all parameters are passed by value by default. In Python, integers and strings behave this way because they are immutable — the function cannot modify the original object even though it has a reference to it.

**Pass-by-reference** means the function receives a direct handle to the original variable, not a copy. Any changes the function makes to the parameter are immediately visible to the caller. In C++, you opt into this with the `&` syntax: `void increment(int &x) { x++; }` will actually modify the caller's variable. This is powerful — it lets functions return multiple results by modifying their parameters, and it avoids the cost of copying large data structures. But it is also dangerous, because any function call might silently change your variables. When debugging, pass-by-reference means you cannot assume a variable's value is unchanged after a function call without checking.

Many languages use a third strategy that confuses beginners: **pass-by-object-reference** (sometimes called pass-by-sharing). In Python and Java, when you pass a list or object, the function receives a copy of the *reference* (pointer) to the object, not a copy of the object itself. This means the function can modify the object's contents (append to a list, change a field), and the caller sees those changes. But if the function reassigns the parameter to a completely new object, the caller's variable still points to the original. This is why `def f(lst): lst.append(1)` modifies the caller's list, but `def f(lst): lst = [1, 2, 3]` does not. Understanding this distinction — "the reference is copied, but the object is shared" — resolves most of the confusion about parameter passing in modern languages.
