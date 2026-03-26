---
id: scope-shadowing-and-lifetime
title: Scope, Shadowing, and Variable Lifetime
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: scope-binding-resolution
  type: hard
- id: variables-and-assignment
  type: soft
builds-toward:
- parameter-passing-value-vs-reference
tags:
- scope
- variables
- lifetime
stage: formal-systems
status: validated
---
# Scope, Shadowing, and Variable Lifetime

## Core Idea
Scope determines where a variable is accessible: local (inside a function), block (inside {…}), or global (everywhere). Shadowing occurs when a variable in inner scope hides one in outer scope. Variables exist from declaration to end of scope (lifetime).

## How It's Best Learned
Trace variable scope in code with multiple levels; deliberately shadow variables to see which one is used; print variable values to verify scope.

## Common Misconceptions
That global variables are accessible everywhere (scope rules apply); that local and global variables with the same name are the same (they're not—shadowing); that variables persist after their scope ends (they don't).

## Questions

```yaml
- question: "A global variable count = 10 exists. Inside a function, you write count = 0 (declaring a new local variable with the same name). After the function runs, what is the value of the global count?"
  type: multiple-choice
  options:
    - "0 — the function modified the global variable"
    - "10 — the function created a shadow variable; the global was unaffected"
    - "Undefined — the global was destroyed when the function ran"
    - "0 — inner scope variables always update the outer scope version"
  answer: 1
  explanation: "Shadowing creates a completely new, independent variable in the inner scope that happens to share the same name as the outer one. Modifying the shadow does NOT affect the original. The global count = 10 survives the function call unchanged. Option A is the classic bug that shadowing causes — programmers mistakenly believe they are modifying the outer variable when they are only modifying a local shadow."

- question: "Consider a variable x declared inside an if-block in a language with block scope. After the if-block ends, which statement is correct?"
  type: multiple-choice
  options:
    - "x is still accessible but its value is undefined"
    - "x no longer exists — both its scope and lifetime have ended"
    - "x still exists in memory but cannot be accessed by name"
    - "x is accessible only from the enclosing function, not globally"
  answer: 1
  explanation: "For a local variable declared inside a block, both scope (visibility) and lifetime (memory existence) end when the block ends. The variable is both inaccessible AND destroyed. Option A is wrong — the language does not merely make the value undefined, the name binding ceases to exist. Option C conflates scope with lifetime — for stack-allocated locals, both end together. Option D describes the behavior of a function-scoped variable, not a block-scoped one."

- question: "A variable's scope and its lifetime are generally identical — they both start and end at the same points in program execution."
  type: true-false
  answer: false
  explanation: "Scope and lifetime can diverge. In garbage-collected languages, an object's lifetime can extend beyond the scope of the variable that created it — as long as other references to it exist, the object persists. Conversely, in C, returning a pointer to a local variable creates a situation where the pointer variable (in the caller) is in scope, but the object it references has been destroyed (its lifetime ended when the callee returned). These are classic examples of scope-lifetime divergence."

- question: "In languages with lexical (static) scoping, an inner scope can read variables from all enclosing outer scopes unless shadowed."
  type: true-false
  answer: true
  explanation: "Lexical scoping defines the scope hierarchy based on where code is written: inner scopes can see all names in their enclosing scopes unless a shadow hides them. This is the standard model in most languages (C, Java, Python, JavaScript). The inner scope 'inherits' visibility from all outer scopes, climbing the nesting hierarchy outward until a match is found. If a shadow exists at an inner scope level, that shadow is found first, preventing access to the outer variable by that name."

- question: "Why is it important to distinguish between a variable's scope and its lifetime, and give a concrete example where they differ?"
  type: short-answer
  answer: "Scope is the region of code where a variable's name is valid and can be used; lifetime is how long the variable's storage actually exists in memory. They differ when references outlive the original variable. Example: in Python, assigning obj = MyClass() creates a reference whose scope is the current block, but if obj is passed to another function or stored in a list, the object's lifetime extends as long as any reference to it exists. In C, returning a pointer to a stack-allocated local variable is the reverse: the pointer is in scope but points to destroyed storage."
  explanation: "This distinction matters for memory safety. In C/C++, using a pointer after the pointed-to variable's lifetime ends is undefined behavior (dangling pointer). In GC languages, objects can persist longer than expected, causing memory leaks if unintended references keep them alive. Scope tells you about name resolution; lifetime tells you about memory validity."
```

## Explainer

From your work on scope and binding resolution, you understand that a variable's name gets resolved to a specific storage location based on where it appears in the code. Now we examine three closely related concepts in more depth: the precise boundaries of **scope**, what happens when scopes overlap through **shadowing**, and when variables are actually created and destroyed — their **lifetime**.

**Scope** is the region of code where a variable is visible and can be referenced by name. Most languages define scope in terms of blocks (the code between `{` and `}`), functions, or modules. A variable declared inside a function is **local** to that function — code outside cannot see it. A variable declared at the top level of a program is **global** and can be accessed from anywhere (though this is rarely a good idea). Many languages also support **block scope**, where a variable declared inside an `if` or `for` block disappears the moment that block ends. The nesting of scopes creates a hierarchy: inner scopes can see variables from outer scopes, but not vice versa.

**Shadowing** occurs when you declare a variable in an inner scope with the same name as one in an outer scope. The inner declaration temporarily hides the outer one — within that inner scope, the name refers to the new, local variable. The outer variable still exists and is unaffected; it just cannot be reached by that name until the inner scope ends. For example, if you have a global `count = 10` and then declare `count = 0` inside a function, the function's `count` is a completely separate variable. Modifying it does not change the global `count`. This is a common source of bugs: you think you are updating the outer variable, but you are actually working with a shadow. Some languages issue warnings when shadowing occurs; in others, you must be vigilant yourself.

**Variable lifetime** is how long a variable's storage exists in memory. For local variables, lifetime matches scope: the variable is created when the declaration is reached and destroyed when execution leaves that scope. For global variables, lifetime spans the entire program. The distinction between scope and lifetime matters most when references to a variable outlive the scope — for example, returning a pointer to a local variable in C produces a dangling reference because the variable's storage is reclaimed. In languages with garbage collection (like Python or Java), objects can outlive the scope of the variable that created them if other references still point to them. Understanding lifetime is essential preparation for grasping how values are passed to functions — your next topic — because it determines whether the data a function receives still exists when the function tries to use it.
