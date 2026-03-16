---
id: ad-hoc-polymorphism-overloading
title: Ad Hoc Polymorphism and Function Overloading
domain: computer-science
course: compilers
prerequisites:
- id: type-systems-overview
  type: hard
- id: symbol-tables-and-scope
  type: hard
builds-toward:
- overload-resolution-typing
tags:
- polymorphism
- type-systems
- overloading
stage: advanced
status: draft
---

# Ad Hoc Polymorphism and Function Overloading

## Core Idea
Ad hoc polymorphism (overloading) allows functions with the same name to behave differently for different argument types. Unlike parametric polymorphism which uses a single implementation, ad hoc polymorphism provides distinct code per type, selected at compile-time during overload resolution.

## Explainer

From your study of type systems, you know that types classify values and constrain the operations that can be performed on them. But consider the `+` operator: it adds integers, concatenates strings, and combines floating-point numbers. These are fundamentally different operations — integer addition uses an ALU instruction, float addition uses an FPU instruction, and string concatenation allocates memory and copies bytes. Yet the programmer writes the same symbol for all three. This is **ad hoc polymorphism**: the same name dispatches to entirely different implementations depending on the types of its arguments.

The term "ad hoc" contrasts with **parametric polymorphism**, where a single function works uniformly over all types. A parametric function like `identity(x) = x` does the same thing regardless of whether x is an integer, a string, or a list — it never inspects the type. Ad hoc polymorphism is the opposite: each type gets its own bespoke implementation. The compiler must determine *which* implementation to call, and it does so by examining the types of the arguments at the call site. This process is called **overload resolution**.

Overload resolution is where your knowledge of symbol tables and scope becomes critical. When the compiler encounters a call like `add(a, b)`, it looks up `add` in the symbol table and finds multiple entries — one for integers, one for floats, perhaps one for complex numbers. It then examines the types of `a` and `b` to select the best match. The rules governing this selection vary by language and can become surprisingly complex. C++ considers implicit conversions (int to float, for example), creating a ranking of matches from exact to promotion to conversion. If no single overload is strictly better than all others, the call is **ambiguous** and the compiler reports an error. Languages like Haskell take a different approach with **type classes**: a type class like `Num` declares an interface (including `+`), and each type provides its own instance, making overload resolution a matter of instance lookup rather than argument-type matching.

The compiler's implementation of ad hoc polymorphism is conceptually a dispatch table keyed by type signatures. At compile time, once overload resolution identifies the correct implementation, the call is bound to a specific function — there is no runtime overhead. This is in contrast to dynamic dispatch (as in virtual methods), where the target is resolved at runtime via a vtable. The distinction matters for performance and for the compiler's ability to inline and optimize: a statically resolved overloaded call is just a normal function call by the time code generation begins.
