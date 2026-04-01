---
id: operational-semantics
title: Operational Semantics
domain: computer-science
course: formal-methods
prerequisites:
- id: programming-language-semantics
  type: hard
- id: predicate-logic
  type: hard
- id: set-theory-basics
  type: soft
builds-toward: []
tags:
- small-step
- big-step
- structural-operational-semantics
- transition-rules
- evaluation-judgments
- sos
stage: expert
status: validated
---

# Operational Semantics

## Core Idea
Operational semantics defines the meaning of programs by specifying how they execute, step by step. **Small-step** (structural) operational semantics defines a transition relation that reduces a program configuration by one computational step at a time, making evaluation order and intermediate states explicit. **Big-step** (natural) operational semantics defines a relation that maps a program directly to its final result, abstracting away intermediate steps. Both are formalized as inference rules that inductively define the evaluation relation. Operational semantics provides the rigorous mathematical foundation upon which Hoare logic, type soundness proofs, and abstract interpretation are built -- without a formal definition of what programs mean, reasoning about program correctness is informal at best.

## Questions

```yaml
- question: "What is the key structural difference between small-step and big-step operational semantics?"
  type: multiple-choice
  options:
    - "Small-step semantics can only handle terminating programs, while big-step handles non-termination"
    - "Small-step defines a single transition (one computation step) and iterates it, while big-step relates a program directly to its final value in one judgment"
    - "Small-step is more expressive because it supports more language features"
    - "Big-step semantics is more formal because it uses inference rules while small-step does not"
  answer: 1
  explanation: "Small-step semantics defines a relation config -> config' that takes one atomic step (e.g., reducing 2+3 to 5 within a larger expression). Full evaluation is the transitive closure ->* of this relation. Big-step semantics defines a relation config => value that directly gives the final result, with the derivation tree capturing the entire computation. Both use inference rules. The practical difference: small-step makes intermediate states observable (important for concurrency, interleaving, and non-termination -- a diverging program takes infinite steps but never produces a big-step derivation). Big-step is often simpler for deterministic, terminating computations and maps naturally to interpreters."

- question: "In small-step operational semantics, non-terminating programs are modeled as infinite sequences of transitions rather than as a special 'diverge' outcome."
  type: true-false
  answer: true
  explanation: "This is a fundamental advantage of small-step semantics over big-step. A non-terminating program like 'while true do skip' generates an infinite chain of configurations: config_0 -> config_1 -> config_2 -> ... that never reaches a final state. There is no finite derivation tree, which matches the intuition that the program runs forever. In big-step semantics, non-termination is problematic: the evaluation relation simply has no derivation for the diverging program. The program's meaning is 'undefined' in the relation, but this is indistinguishable from a stuck program (one that reaches an error). Small-step semantics cleanly distinguishes divergence (infinite transitions) from getting stuck (no transition available from a non-final configuration)."

- question: "Write the small-step rule for the if-then-else construct: if the condition is 'true', the entire expression steps to the 'then' branch."
  type: short-answer
  answer: "if true then e1 else e2 -> e1. This is an axiom (no premises needed). The companion rule is: if false then e1 else e2 -> e2. A third congruence rule handles the case where the condition is not yet a value: if e0 -> e0', then (if e0 then e1 else e2) -> (if e0' then e1 else e2). This congruence rule specifies that the condition is evaluated first."
  explanation: "These three rules together completely specify the evaluation of conditionals. The two axioms handle the base cases (condition already reduced to a Boolean value). The congruence rule ensures the condition is fully evaluated before the branch is selected -- it encodes left-to-right evaluation order. This pattern of axiom rules for computed values plus congruence rules for sub-expression evaluation is the hallmark of structural operational semantics (SOS), formalized by Plotkin (1981)."

- question: "Why is operational semantics considered a prerequisite for formal program verification rather than an alternative to it?"
  type: short-answer
  answer: "Hoare logic, weakest preconditions, abstract interpretation, and type systems all reason about program behavior. But what does a program 'do'? Operational semantics provides the mathematical definition: the transition relation IS the program's meaning. Hoare logic's soundness theorem says that if {P} C {Q} is derivable, then for every state satisfying P, the operational execution of C from that state (if it terminates) yields a state satisfying Q. Without operational semantics, soundness is circular -- you would be verifying programs against an informal notion of what they compute. The semantics is the ground truth against which all verification techniques are proven correct."
  explanation: "This foundational role is why operational semantics appears in any rigorous treatment of programming languages and formal methods. The standard proof technique for type soundness, for instance, is 'progress and preservation': progress says well-typed programs can always take a step (using the small-step transition relation), and preservation says each step preserves typedness. Both are stated and proved with respect to the operational semantics."
```

## Explainer

Programming languages need precise definitions of what their programs mean. Informal English descriptions are ambiguous -- does `x++ + x++` in C evaluate left-to-right, right-to-left, or is it undefined? **Operational semantics** answers such questions by defining a mathematical relation that specifies exactly how programs execute. There are two main styles, both formalized as sets of inference rules.

**Small-step operational semantics** (also called structural operational semantics or SOS, after Plotkin's 1981 framework) defines a transition relation `->` on configurations. A configuration pairs a program fragment with a state (variable assignments, heap, etc.). Each rule specifies one atomic computation step. For example, the rule for addition says: if both operands are integer values n1 and n2, then `n1 + n2 -> n` where n is their sum. If the left operand is not yet a value, a congruence rule says `e1 + e2 -> e1' + e2` whenever `e1 -> e1'`, specifying left-to-right evaluation order. Full program execution is the reflexive-transitive closure `->*` of the single-step relation: starting from the initial configuration, repeatedly apply transition rules until no rule applies (the program is stuck or has produced a final value).

**Big-step operational semantics** (also called natural semantics, after Kahn's 1987 formulation) defines an evaluation relation `=>` that maps a configuration directly to a final value. The rule for addition says: if `e1 => n1` and `e2 => n2`, then `e1 + e2 => n1 + n2`. The derivation tree for a big-step judgment mirrors the recursive call structure of an interpreter. Big-step semantics is often more concise and intuitive for deterministic, terminating languages -- it reads almost like a recursive interpreter specification. However, it cannot naturally express non-termination (there is simply no derivation for a diverging program) or distinguish stuck programs from diverging ones. It also struggles with concurrency and interleaving, where intermediate states matter.

The choice between small-step and big-step depends on what you need to reason about. Small-step is essential when **intermediate states** are observable or important: concurrency (interleaving of steps from different threads), type soundness proofs (progress: "well-typed programs can always take a step"), and reasoning about non-termination. Big-step is preferred for simple languages or when you only care about input-output behavior. Many formalizations use both: big-step for the deterministic core language, small-step for the concurrency and control-flow extensions. The two styles can be shown equivalent for terminating, deterministic programs: if `e =>* v` in big-step, then `e ->* v` in small-step, and vice versa.

Operational semantics is not just a theoretical exercise -- it is the **foundation** on which formal verification rests. Hoare logic's soundness theorem is stated with respect to the operational semantics: `{P} C {Q}` means that for all states sigma satisfying P, if `(C, sigma) ->* (skip, sigma')`, then sigma' satisfies Q. Abstract interpretation's soundness is proved by showing the abstract transfer functions over-approximate the concrete transitions defined by the operational semantics. Type soundness (via progress and preservation) is entirely a statement about the operational transition relation. Without a formal semantics, verification is informal reasoning about an informal object -- operational semantics makes it rigorous mathematics about a mathematical object. This is why Plotkin's SOS framework is one of the most cited papers in programming language theory: it gave the field its mathematical foundation.
