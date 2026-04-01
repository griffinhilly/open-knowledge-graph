---
id: linear-types
title: Linear Types
domain: computer-science
course: formal-methods
prerequisites:
- id: type-systems-overview
  type: hard
- id: curry-howard-correspondence
  type: soft
builds-toward:
- session-types
tags:
- linear-logic
- affine-types
- resource-management
- ownership
- rust-borrow-checker
stage: expert
status: validated
---
# Linear Types

## Core Idea
Linear types enforce that values are used exactly once: they cannot be duplicated (used twice) or discarded (unused). This discipline, rooted in Girard's linear logic, treats values as consumable resources rather than freely copyable data. Linear types statically guarantee resource management properties — file handles are closed exactly once, memory is freed exactly once, protocol steps are followed in order. Rust's ownership and borrow-checking system is the most commercially successful application of linear (specifically, affine) type discipline, preventing use-after-free, double-free, and data races at compile time.

## Questions

```yaml
- question: "A value with a linear type must be used exactly once. What does 'used' mean in this context?"
  type: multiple-choice
  options:
    - "The value must appear exactly once in the source code text"
    - "The value must be consumed by exactly one operation at runtime — it cannot be passed to two different functions (duplication) or ignored without being consumed (discarding)"
    - "The value must be of a primitive type"
    - "The value must be immutable"
  answer: 1
  explanation: "Linear usage means the value is consumed exactly once along every execution path. If you have a linear file handle, you must eventually close it (consume it) — not closing it is a type error (discard). You cannot pass it to two functions that both try to close it (duplication). The type system tracks this statically, ensuring that resources are managed correctly regardless of which branches or loops execute."

- question: "Rust's ownership system is based on affine types, not strictly linear types. What is the difference?"
  type: short-answer
  answer: "Affine types allow values to be used AT MOST once (can be discarded but not duplicated), while linear types require values to be used EXACTLY once (no discarding, no duplication). Rust is affine: you can let an owned value go out of scope without explicitly consuming it (the destructor runs automatically). A strictly linear system would require explicit consumption, making it harder to use in practice."
  explanation: "The distinction matters for resource management. In a linear system, a file handle MUST be explicitly closed — the type system forces you to call close(). In Rust's affine system, the handle is closed when dropped (by the destructor), which happens automatically at scope exit. This is more ergonomic while still preventing duplication (which would cause double-close bugs). Rust adds borrowing on top of affine ownership to allow temporary shared access without consuming the value."

- question: "How do linear types prevent data races in concurrent programs?"
  type: short-answer
  answer: "If a mutable value has a linear type, it can be owned by exactly one thread at a time — the type system prevents two threads from simultaneously holding a reference to the same mutable data. To share data between threads, you must explicitly transfer ownership (consuming the value in the sender and creating it in the receiver) or use a synchronization primitive. Since data races require two threads accessing the same memory with at least one writing, and linear types prevent shared mutable access, data races are ruled out by construction."
  explanation: "This is the insight behind Rust's concurrency safety guarantees ('fearless concurrency'). The borrow checker ensures that mutable references are unique (at most one &mut T) and shared references are immutable (multiple &T, no mutation). This is a form of affine discipline applied to references: a mutable reference is used linearly (exactly one owner), preventing concurrent mutation. The safety guarantee is static — no runtime overhead, no data race possible in safe Rust."

- question: "Linear types are connected to Girard's linear logic through the Curry-Howard correspondence."
  type: true-false
  answer: true
  explanation: "Just as the Curry-Howard correspondence connects intuitionistic logic to simply-typed lambda calculus, it connects linear logic to linear type theory. In linear logic, hypotheses must be used exactly once — you cannot reuse a premise without the explicit 'of course' modality (!A). Under Curry-Howard, this translates to: values of linear type must be consumed exactly once, and values that can be freely copied require a special 'unrestricted' (non-linear) type. This logical foundation gives linear type systems their clean theoretical properties."
```

## Explainer

In conventional type systems, values can be freely copied and discarded. You can pass the same variable to multiple functions, bind it to several names, or simply ignore it. This works for pure data (integers, strings) but is problematic for **resources** — entities whose lifecycle must be carefully managed. A file handle must be closed exactly once: failing to close it leaks the resource; closing it twice causes a runtime error. A memory allocation must be freed exactly once: forgetting causes a leak; freeing twice corrupts the heap. **Linear types** enforce this discipline statically by requiring that every value is consumed exactly once.

The theoretical foundation is **Girard's linear logic** (1987), which treats logical hypotheses as resources that are consumed by use. In classical logic, you can use a premise as many times as you like; in linear logic, each premise is available for exactly one use unless explicitly marked as reusable (with the ! modality). Through the **Curry-Howard correspondence**, this gives rise to linear type theory: values of linear type cannot be duplicated (used more than once) or weakened (discarded without use). The type system statically tracks that every linear value has exactly one consumer.

**Affine types** relax the constraint to "at most once" — values can be discarded but not duplicated. **Relevant types** enforce "at least once" — values cannot be discarded but can be duplicated. Linear is the intersection: exactly once. In practice, affine types are more ergonomic than strictly linear types because they allow values to go out of scope (with automatic cleanup via destructors), and this is the variant most languages adopt.

**Rust** is the most commercially successful application of these ideas. Rust's ownership system is affine: each value has exactly one owner, and when the owner goes out of scope, the value is dropped (its destructor runs). Ownership can be transferred (moved) but not copied (for non-Copy types). Rust adds **borrowing** — temporary references that do not transfer ownership — with the constraint that you can have either multiple shared immutable borrows (&T) or one exclusive mutable borrow (&mut T), but not both simultaneously. This combination prevents use-after-free, double-free, and data races at compile time, with zero runtime overhead.

Beyond memory safety, linear types enable **protocol enforcement**. A session type (a closely related concept) describes the sequence of operations on a communication channel; linearity ensures the protocol is followed step by step. A typestate system uses linear types to track object state (file open vs. closed, connection established vs. disconnected) and prevent invalid operations (reading from a closed file). Linear types also enable safe **manual memory management** without a garbage collector: since the type system ensures every allocation has exactly one owner and is freed exactly once, memory safety is guaranteed statically. This is the core value proposition of Rust and similar systems.
