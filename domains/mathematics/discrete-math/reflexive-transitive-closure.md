---
id: reflexive-transitive-closure
title: Reflexive and Transitive Closure
domain: mathematics
course: discrete-math
prerequisites:
- id: transitive-closure-relations
  type: hard
tags:
- relations
- closure
- properties
stage: formal-systems
status: draft
---

# Reflexive and Transitive Closure

## Core Idea
The reflexive transitive closure adds both reflexive and transitive properties to a relation. It is the smallest relation containing the original relation, the identity relation, and all compositions. This is essential for modeling reachability with self-loops and finding strongly connected components.

## Explainer

You already know the **transitive closure** R⁺ of a relation R: it connects a to b whenever there is a directed path of one or more steps from a to b. The **reflexive transitive closure** R* adds one more layer — every element is also related to itself, capturing the idea that each node can "reach itself" in zero steps. R* is to R⁺ what "zero or more" is to "one or more."

Formally, R* is the smallest relation on A that contains R, is reflexive (a R* a for all a ∈ A), and is transitive (if a R* b and b R* c then a R* c). It can be built by taking the transitive closure R⁺ and adding the diagonal {(a, a) : a ∈ A} — or equivalently, it is R⁰ ∪ R¹ ∪ R² ∪ …, where R⁰ is the identity relation (the diagonal) and Rⁿ denotes "reachable in exactly n steps." The identity relation R⁰ is what makes R* reflexive and what makes the zero-step path meaningful.

The practical reading is **reachability including the trivial case**: a R* b means you can get from a to b in zero or more steps. This matters in contexts where you want to ask "can a reach b?" without assuming a ≠ b. In compiler theory, the variable-influence relation uses R* so that a variable trivially influences itself (any assignment to x certainly affects x). In formal language theory, the **Kleene star** L* (strings formed from zero or more concatenations of strings in L) is the direct linguistic analogue of the reflexive transitive closure of a step relation.

The contrast between R⁺ and R* is small but consequential: R* includes the diagonal; R⁺ does not. In many contexts — program analysis, type-system rules, closure operators in order theory — you encounter both, and confusing them causes subtle errors. As a rule of thumb: if "reaching yourself" should be trivially true, use R*; if a genuine one-step connection is required, use R⁺.
