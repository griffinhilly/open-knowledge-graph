---
id: scope-shadowing-and-lifetime
title: Scope, Shadowing, and Variable Lifetime
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: scope-binding-resolution
  type: hard
- id: variable-names-and-conventions
  type: soft
builds-toward:
- parameter-passing-value-vs-reference
tags:
- scope
- variables
- lifetime
stage: advanced
status: draft
---

# Scope, Shadowing, and Variable Lifetime

## Core Idea
Scope determines where a variable is accessible: local (inside a function), block (inside {…}), or global (everywhere). Shadowing occurs when a variable in inner scope hides one in outer scope. Variables exist from declaration to end of scope (lifetime).

## How It's Best Learned
Trace variable scope in code with multiple levels; deliberately shadow variables to see which one is used; print variable values to verify scope.

## Common Misconceptions
That global variables are accessible everywhere (scope rules apply); that local and global variables with the same name are the same (they're not—shadowing); that variables persist after their scope ends (they don't).

## Explainer

From your work on scope and binding resolution, you understand that a variable's name gets resolved to a specific storage location based on where it appears in the code. Now we examine three closely related concepts in more depth: the precise boundaries of **scope**, what happens when scopes overlap through **shadowing**, and when variables are actually created and destroyed — their **lifetime**.

**Scope** is the region of code where a variable is visible and can be referenced by name. Most languages define scope in terms of blocks (the code between `{` and `}`), functions, or modules. A variable declared inside a function is **local** to that function — code outside cannot see it. A variable declared at the top level of a program is **global** and can be accessed from anywhere (though this is rarely a good idea). Many languages also support **block scope**, where a variable declared inside an `if` or `for` block disappears the moment that block ends. The nesting of scopes creates a hierarchy: inner scopes can see variables from outer scopes, but not vice versa.

**Shadowing** occurs when you declare a variable in an inner scope with the same name as one in an outer scope. The inner declaration temporarily hides the outer one — within that inner scope, the name refers to the new, local variable. The outer variable still exists and is unaffected; it just cannot be reached by that name until the inner scope ends. For example, if you have a global `count = 10` and then declare `count = 0` inside a function, the function's `count` is a completely separate variable. Modifying it does not change the global `count`. This is a common source of bugs: you think you are updating the outer variable, but you are actually working with a shadow. Some languages issue warnings when shadowing occurs; in others, you must be vigilant yourself.

**Variable lifetime** is how long a variable's storage exists in memory. For local variables, lifetime matches scope: the variable is created when the declaration is reached and destroyed when execution leaves that scope. For global variables, lifetime spans the entire program. The distinction between scope and lifetime matters most when references to a variable outlive the scope — for example, returning a pointer to a local variable in C produces a dangling reference because the variable's storage is reclaimed. In languages with garbage collection (like Python or Java), objects can outlive the scope of the variable that created them if other references still point to them. Understanding lifetime is essential preparation for grasping how values are passed to functions — your next topic — because it determines whether the data a function receives still exists when the function tries to use it.
