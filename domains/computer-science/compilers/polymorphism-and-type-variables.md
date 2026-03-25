---
id: polymorphism-and-type-variables
title: Polymorphism and Type Variables
domain: computer-science
course: compilers
prerequisites:
- id: type-checking-bidirectional
  type: hard
- id: hindley-milner-type-system
  type: soft
builds-toward:
- intermediate-code-representation
tags:
- type-systems
- generics
- polymorphism
stage: advanced
status: validated
---

# Polymorphism and Type Variables

## Core Idea
Parametric polymorphism allows functions and data structures to work with multiple types. This is more general than ad-hoc polymorphism (overloading). Implementing polymorphism requires careful handling of type variables, instantiation, and specialization.

## How It's Best Learned
Implement parametric polymorphism using type variables and instantiation. Study how Java generics and C++ templates compile differently.

## Common Misconceptions
Type variables are just placeholders (they are constraints on valid operations). Polymorphism requires runtime type checking (parametric polymorphism can be fully static).

## Questions

```yaml
- question: "Inside a polymorphic function `reverse : ∀α. List α → List α`, what operations on the elements of type α can the function legally perform?"
  type: multiple-choice
  options:
    - "Any operation, because the function will be type-checked at each call site with a concrete type"
    - "Only operations defined for all types — the function can rearrange elements but cannot inspect, compare, or compute with their values"
    - "Any operation that the most common concrete type (e.g., Int) supports"
    - "Operations determined at runtime by inspecting the actual type of α"
  answer: 1
  explanation: "Parametric polymorphism means the type variable α is universally quantified: the function must work correctly for every possible type substitution. Inside the function, the only thing you can do with an element of type α is treat it as an opaque value — you can pass it around, put it in a list, return it, but you cannot add it, compare it, or call type-specific methods on it, because those operations are not defined for all types. This restriction is what makes the function genuinely generic. Option A describes ad-hoc polymorphism (overloading), which is a different mechanism."

- question: "A team is choosing between Java-style type erasure and C++/Rust-style monomorphization for compiling a generic container library. Which tradeoff is correct?"
  type: multiple-choice
  options:
    - "Monomorphization produces smaller binaries because it avoids storing type information at runtime"
    - "Type erasure produces faster code because it avoids boxing overhead, while monomorphization uses more memory"
    - "Monomorphization produces faster, specialized code but larger binaries; type erasure produces smaller binaries but may incur boxing overhead"
    - "Both approaches produce identical machine code; the difference is only in compile-time checking"
  answer: 2
  explanation: "Monomorphization generates a separate specialized copy of each function for each concrete type it is called with (e.g., List_int, List_string). Each copy is highly optimized for its specific type with no boxing — faster at runtime. But the binary grows with each new instantiation. Type erasure compiles a single version of the code using a uniform representation (typically boxed pointers), keeping the binary small but requiring indirection at runtime. Neither approach is universally better; the tradeoff is speed vs. binary size and compile time."

- question: "Parametric polymorphism can be fully enforced at compile time — no runtime type inspection is required to maintain type safety."
  type: true-false
  answer: true
  explanation: "This is one of the key distinguishing features of parametric polymorphism. Because the type variable is universally quantified and the function is restricted to operations valid for all types, the compiler can check type safety once at definition time and at each instantiation call site — all statically. The Hindley-Milner type inference system demonstrates this: it infers polymorphic types and all instantiations without any runtime type tags. This contrasts with Java's pre-generics approach (using Object with runtime casts) or Python's duck typing, which rely on runtime type information."

- question: "A type variable like `α` in `identity : ∀α. α → α` is essentially just a placeholder for 'any type' — the function can be specialized to perform type-specific operations when called with a concrete type."
  type: true-false
  answer: false
  explanation: "Type variables in parametric polymorphism are universal constraints, not merely labels. The function body must be written without assuming anything about α — it cannot perform any α-specific operation. 'Specialization' in parametric polymorphism (whether via type erasure or monomorphization) does not add new operations; it only fills in the type at the call site for the same generic behavior. If you want type-specific behavior, you need ad-hoc polymorphism (overloading) or type classes/traits, which are different mechanisms that explicitly list which operations each type supports."

- question: "Why can a parametrically polymorphic function `identity : ∀α. α → α` not simply add 1 to its argument, even if every actual call site passes an integer?"
  type: short-answer
  answer: "The type checker evaluates the function body under the assumption that α is an arbitrary, unknown type — not an integer. Addition is not defined for all types (you cannot add two strings, two booleans, or two functions), so the type checker rejects it as invalid for type α. The function must be written to work for every possible α simultaneously, not just for the types it happens to be called with today. If the programmer wants an integer-specific increment, they must give the function a monomorphic type `Int → Int`."
  explanation: "This is the key restriction that makes parametric polymorphism safe and predictable. Because the function is universally quantified, the type checker enforces that every operation in the body is valid for all types — including types the programmer hasn't thought of yet. The payoff is that a caller can safely instantiate the function with any type, confident the body cannot do anything unexpected with their value. Allowing type-specific operations inside a supposedly polymorphic function would break this guarantee and require runtime type inspection — converting parametric into ad-hoc polymorphism."
```

## Explainer

From your work with type checking, you know that a type checker walks the AST and ensures that every operation receives operands of the correct type. But what happens when you write a function like `identity(x) = x` that works for any type? Without polymorphism, you would need to write a separate version for integers, strings, booleans, and every other type — or abandon type safety entirely by using a universal "any" type. **Parametric polymorphism** solves this by introducing **type variables** — placeholders like `α` or `T` that stand for "some type, to be determined later" — allowing a single function definition to be type-safe across all types.

The key insight is that a type variable is not a concrete type but a **universally quantified** constraint. When you write `identity : ∀α. α → α`, you are saying: "for any type `α` you choose, this function takes an `α` and returns an `α`." The type checker enforces this contract: inside `identity`, the only thing you can do with `x` is treat it as an opaque value of type `α`. You cannot add to it, print it, or call methods on it — because those operations are not defined for all possible types. This restriction is what makes parametric polymorphism safe. If you could inspect or operate on `x` based on its runtime type, you would have **ad-hoc polymorphism** (overloading or type classes), which is a different mechanism with different implementation requirements.

When a polymorphic function is actually called — say `identity(42)` — the type checker performs **instantiation**: it substitutes the type variable `α` with the concrete type `int`, producing the specialized type `int → int` for this particular call. If you also call `identity("hello")`, a separate instantiation yields `string → string`. The Hindley-Milner system you have encountered automates this process through **type inference**: the compiler deduces both the polymorphic type of the definition and the instantiation at each call site, without requiring explicit type annotations from the programmer.

How this plays out in compiled code varies significantly across languages. In **type erasure** implementations (like Java generics and most ML compilers), the compiler verifies type safety at compile time and then generates a single version of the code that works with a uniform representation — typically pointers or boxed values. The type variables vanish entirely from the runtime code. In **monomorphization** implementations (like C++ templates and Rust generics), the compiler generates a separate specialized copy of the function for each concrete type it is called with — `identity_int`, `identity_string`, and so on. Monomorphization produces faster code (no boxing overhead) at the cost of larger binaries and longer compile times. Understanding this distinction matters when you move to intermediate code generation, because the IR must either represent polymorphic operations abstractly or the polymorphism must be resolved before IR generation.
