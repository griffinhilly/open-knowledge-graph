---
id: overload-resolution-typing
title: Overload Resolution in Type Systems
domain: computer-science
course: compilers
prerequisites:
- id: type-systems-overview
  type: hard
- id: ad-hoc-polymorphism-overloading
  type: hard
tags:
- type-systems
- polymorphism
- overloading
stage: advanced
status: draft
---

# Overload Resolution in Type Systems

## Core Idea
Overload resolution selects the best-matching function among multiple declarations with the same name. It uses specificity rules (int matches int better than Object), type compatibility (subtype matches supertype), and tie-breaking by definition order, enabling elegant APIs where operations feel unified despite different implementations.

## Explainer

From your work on type systems and ad-hoc polymorphism, you know that overloading lets multiple functions share one name as long as their parameter types differ. The programmer writes `print(42)` and `print("hello")` without caring which implementation runs — but the compiler must decide. **Overload resolution** is the algorithm that makes that decision, and its complexity grows surprisingly fast as type systems become richer.

The resolution process begins with **candidate gathering**: the compiler collects every visible function declaration with the matching name. Next comes **applicability filtering** — each candidate is tested against the actual argument types at the call site. A candidate is applicable if every argument can be converted to the corresponding parameter type, either exactly, through implicit widening (like `int` to `long`), or through subtype relationships. If no candidate is applicable, the compiler reports an error. If exactly one survives, it wins. The interesting case is when multiple candidates remain.

When several candidates are all applicable, the compiler needs a **specificity ranking** to pick the best one. The core principle is that a more specific match beats a less specific one. If you call `f(5)` and both `f(int)` and `f(Object)` are candidates, `f(int)` wins because `int` is a tighter match — no conversion is needed. The ranking extends to multiple parameters: candidate A is more specific than candidate B if every parameter of A is at least as specific as the corresponding parameter of B, and at least one is strictly more specific. When neither candidate dominates the other across all parameters, the call is **ambiguous**, and the compiler must reject it rather than guess. Languages like Java and C# add further layers — autoboxing, varargs, and generic type argument inference each introduce additional resolution phases with carefully defined priority ordering.

The subtlety of overload resolution is that it interacts with nearly every other feature in the type system. Generic methods require the compiler to infer type arguments before comparing specificity. Implicit conversions widen the set of applicable candidates, sometimes in surprising ways. Subtype polymorphism means that a method inherited from a superclass competes with one defined in a subclass. Each language defines its own precedence rules to navigate these interactions, and getting them wrong produces confusing "ambiguous call" errors or, worse, silently selects the wrong overload. Understanding the resolution algorithm is essential for both compiler implementers who must get it right and library designers who want overloaded APIs to behave intuitively.
