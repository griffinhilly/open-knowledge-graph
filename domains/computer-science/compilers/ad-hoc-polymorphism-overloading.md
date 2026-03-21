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

## Questions

```yaml
- question: "A function `length` works on strings, lists, and arrays using a single uniform implementation that counts elements without inspecting type. A function `add` has one implementation for integers (ALU instruction) and a separate implementation for strings (memory allocation and copying). Which is ad hoc polymorphism?"
  type: multiple-choice
  options:
    - "Both `length` and `add` — any function that works across multiple types is ad hoc polymorphic"
    - "`length` only — uniform behavior across types is the defining feature of ad hoc polymorphism"
    - "`add` only — separate implementations per type is the defining feature of ad hoc polymorphism"
    - "Neither — ad hoc polymorphism requires runtime dispatch to be valid"
  answer: 2
  explanation: "`add` is ad hoc polymorphism: the same name dispatches to fundamentally different code depending on argument types. `length` is parametric polymorphism: a single uniform implementation works for any container type without inspecting type information. The distinction is whether one implementation suffices for all types or whether each type gets its own bespoke code."

- question: "The compiler encounters `foo(a, b)` where `foo` has overloads for (int, int) and (float, float). Both `a` and `b` are declared as `int`. The language allows implicit int-to-float promotion. How does overload resolution proceed?"
  type: multiple-choice
  options:
    - "The call is ambiguous because both overloads could apply after promotion"
    - "The (int, int) overload is selected as an exact match, with no promotion needed"
    - "The (float, float) overload is selected because float is the default numeric type"
    - "The call fails — ad hoc polymorphism does not permit implicit conversions"
  answer: 1
  explanation: "Overload resolution ranks matches: an exact type match beats any match requiring implicit promotion. Since (int, int) matches exactly, it is selected without ambiguity. The ambiguity in option A would arise only if two overloads tied in ranking (e.g., one requires int→float promotion on the first arg and the other on the second). Exact matches always take priority."

- question: "Overload resolution for ad hoc polymorphism is performed at compile time, not at runtime."
  type: true-false
  answer: true
  explanation: "This is a defining property of ad hoc polymorphism: the compiler determines which implementation to call based on the static (compile-time) types of the arguments. Once resolved, the call is bound to a specific function — there is no runtime overhead for dispatch. This distinguishes overloading from dynamic dispatch (virtual functions), where the target is determined at runtime via a vtable lookup."

- question: "Ad hoc polymorphism and parametric polymorphism both use a single implementation shared across all applicable types."
  type: true-false
  answer: false
  explanation: "This is the exact opposite of what distinguishes them. Parametric polymorphism uses one uniform implementation for all types without inspecting type information (e.g., `identity(x) = x`). Ad hoc polymorphism provides a distinct, bespoke implementation for each type — integer addition and string concatenation are fundamentally different operations even if both are spelled `+`."

- question: "Explain why overload resolution can become ambiguous in a language that permits implicit type conversions, and how languages typically handle this."
  type: short-answer
  answer: "When implicit conversions are allowed, multiple overloads may be reachable from the same call site by applying different conversions. If no single overload is strictly better than all others (matches at least as well on every argument and strictly better on at least one), the compiler cannot choose and reports an ambiguity error. Languages like C++ rank candidates by conversion quality (exact match > promotion > standard conversion) and declare ambiguity only when two candidates tie at the top rank."
  explanation: "The problem is inherent to combining overloading with implicit conversion. For example, if `foo` has overloads (int, double) and (double, int), calling `foo(1, 2)` requires one implicit conversion for each — neither overload is strictly better. Rather than silently guessing, the compiler rejects the call as ambiguous. This is why language designers must carefully specify conversion rules and overload ranking to make resolution predictable."
```

## Explainer

From your study of type systems, you know that types classify values and constrain the operations that can be performed on them. But consider the `+` operator: it adds integers, concatenates strings, and combines floating-point numbers. These are fundamentally different operations — integer addition uses an ALU instruction, float addition uses an FPU instruction, and string concatenation allocates memory and copies bytes. Yet the programmer writes the same symbol for all three. This is **ad hoc polymorphism**: the same name dispatches to entirely different implementations depending on the types of its arguments.

The term "ad hoc" contrasts with **parametric polymorphism**, where a single function works uniformly over all types. A parametric function like `identity(x) = x` does the same thing regardless of whether x is an integer, a string, or a list — it never inspects the type. Ad hoc polymorphism is the opposite: each type gets its own bespoke implementation. The compiler must determine *which* implementation to call, and it does so by examining the types of the arguments at the call site. This process is called **overload resolution**.

Overload resolution is where your knowledge of symbol tables and scope becomes critical. When the compiler encounters a call like `add(a, b)`, it looks up `add` in the symbol table and finds multiple entries — one for integers, one for floats, perhaps one for complex numbers. It then examines the types of `a` and `b` to select the best match. The rules governing this selection vary by language and can become surprisingly complex. C++ considers implicit conversions (int to float, for example), creating a ranking of matches from exact to promotion to conversion. If no single overload is strictly better than all others, the call is **ambiguous** and the compiler reports an error. Languages like Haskell take a different approach with **type classes**: a type class like `Num` declares an interface (including `+`), and each type provides its own instance, making overload resolution a matter of instance lookup rather than argument-type matching.

The compiler's implementation of ad hoc polymorphism is conceptually a dispatch table keyed by type signatures. At compile time, once overload resolution identifies the correct implementation, the call is bound to a specific function — there is no runtime overhead. This is in contrast to dynamic dispatch (as in virtual methods), where the target is resolved at runtime via a vtable. The distinction matters for performance and for the compiler's ability to inline and optimize: a statically resolved overloaded call is just a normal function call by the time code generation begins.
