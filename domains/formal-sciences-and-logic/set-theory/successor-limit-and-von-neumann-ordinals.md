---
id: successor-limit-and-von-neumann-ordinals
title: Successor Ordinals, Limit Ordinals, and Von Neumann Construction
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: ordinal-numbers-definition-and-order
  type: hard
- id: von-neumann-ordinals
  type: soft
builds-toward:
- ordinal-arithmetic-operations-and-exponentiation
tags:
- successor
- limit-ordinal
- von-neumann
- ordinal-construction
stage: formal-systems
status: draft
---

# Successor Ordinals, Limit Ordinals, and Von Neumann Construction

## Core Idea
Von Neumann's construction defines each ordinal as the set of all smaller ordinals: 0 = ∅, S(α) = α ∪ {α}. Successor ordinals extend the count; limit ordinals (like ω) have no immediate predecessor and represent suprema of smaller ordinals. This construction embeds ordinals entirely within pure set theory.

## Questions

```yaml
- question: "According to the Von Neumann construction, what is the ordinal 3?"
  type: multiple-choice
  options:
    - "The number that comes after 2, with no further set-theoretic definition"
    - "{∅, {∅}, {∅, {∅}}} — the set containing 0, 1, and 2"
    - "{{∅}} — the set containing the set containing the empty set"
    - "The successor of 2, defined as S(2) = {2} alone"
  answer: 1
  explanation: "In the Von Neumann construction, each ordinal is the set of all ordinals that came before it: 0 = ∅, 1 = {0} = {∅}, 2 = {0,1} = {∅,{∅}}, 3 = {0,1,2} = {∅,{∅},{∅,{∅}}}. The successor operation adds the ordinal itself as a new element: S(α) = α ∪ {α}. So 3 = S(2) = 2 ∪ {2} = {0,1} ∪ {2} = {0,1,2}. Every ordinal contains exactly its predecessors as elements — a feature that makes the ordering relation (α < β iff α ∈ β) coincide perfectly with set membership."

- question: "Why does transfinite induction require three cases rather than the two cases (base + inductive step) of ordinary mathematical induction?"
  type: multiple-choice
  options:
    - "Because ordinals extend into three 'zones': finite, countably infinite, and uncountably infinite"
    - "Because limit ordinals like ω have no immediate predecessor, so the successor step cannot reach them from below"
    - "Because the base case at 0 must be split into two sub-cases for even and odd ordinals"
    - "Because set theory requires an extra case to handle the axiom of choice"
  answer: 1
  explanation: "Ordinary induction proves P(0) and (P(n) → P(n+1)), which covers all natural numbers because every natural number can be reached by repeatedly applying the successor from 0. But ω is a limit ordinal — there is no ordinal just below it, so no single successor step reaches it. Transfinite induction adds a limit case: if P(α) holds for all α < λ (for every limit ordinal λ), then P(λ) holds. This third case is necessary precisely because limit ordinals are defined as suprema, not as successors, and the proof must reflect that structure."

- question: "In the Von Neumann construction, the statement 'α < β' (α is less than β as ordinals) is equivalent to 'α ∈ β' (α is a member of β as sets)."
  type: true-false
  answer: true
  explanation: "This is the elegant feature of the Von Neumann construction: the two most natural relations on ordinals (order and membership) coincide exactly. Since each ordinal is defined as the set of all smaller ordinals, β = {α : α < β} — so α is an element of β if and only if α is less than β. This makes ordinal comparisons set-theoretically transparent: to check if one ordinal is smaller than another, you check membership. No separate definition of '<' is needed; it is inherited from ∈."

- question: "ω (the first infinite ordinal) is a successor ordinal — it is the successor of the largest finite ordinal."
  type: true-false
  answer: false
  explanation: "ω is a limit ordinal, not a successor ordinal. There is no largest finite ordinal: for every finite ordinal n, S(n) = n+1 is also a finite ordinal. Since no finite ordinal is 'just below' ω, ω cannot be reached by a single successor step. Instead, ω is defined as the set of all finite ordinals: ω = {0, 1, 2, 3, …} — the supremum of the infinite sequence of finite ordinals. This is the defining characteristic of a limit ordinal: it has no immediate predecessor and equals the union (supremum) of all ordinals below it."

- question: "What does it mean to say that ω is a 'limit ordinal,' and why does this make it fundamentally different from finite ordinals?"
  type: short-answer
  answer: "ω is a limit ordinal because it has no immediate predecessor — there is no ordinal α such that S(α) = ω. Every finite ordinal n is a successor ordinal: n = S(n−1). But ω is the supremum of the entire infinite sequence {0, 1, 2, 3, …}; you cannot reach it by any finite number of successor steps from below. In the Von Neumann construction, ω is defined as the set of all finite ordinals: ω = {0, 1, 2, …}, so it contains infinitely many elements. This is why transfinite induction needs a special limit case: you cannot use the successor step to 'get to' ω, so you must prove the property holds at ω by a different argument — typically showing it holds for all smaller ordinals and that this forces it to hold at the supremum."
  explanation: "The limit/successor distinction is fundamental to the structure of transfinite arithmetic. It recurs at every level: after ω come ω+1, ω+2, … (successor ordinals), then the limit ordinal ω·2, and so on. The ordinals alternate between successor stages (reachable by one step) and limit stages (defined as suprema). Any proof or recursive definition over all ordinals must handle both types explicitly."
```

## Explainer

You already know that ordinals are a well-ordered extension of the natural numbers that reach into the transfinite. The Von Neumann construction answers a foundational question: what *are* ordinals made of, if we want to build everything from pure sets? The elegant answer is that each ordinal simply *is* the set of all ordinals that came before it. So 0 = ∅ (nothing came before zero), 1 = {0} = {∅}, 2 = {0, 1} = {∅, {∅}}, and so on. At every stage, an ordinal contains exactly its predecessors as elements, which means that comparing two ordinals by "less than" is the same as the ∈ relation — α < β if and only if α ∈ β.

With this construction established, every ordinal falls into one of two categories. A **successor ordinal** is one that has an immediate predecessor: S(α) = α ∪ {α} adds α itself as a new element to the set α, producing the next ordinal. All finite ordinals (1, 2, 3, …) are successor ordinals, as are ordinals like ω+1, ω+2, and so on. A **limit ordinal** has no immediate predecessor — it cannot be reached by a single successor step. The first and most important limit ordinal is **ω**, the set of all finite ordinals: ω = {0, 1, 2, 3, …}. There is no ordinal just below ω in the way that 4 is just below 5; instead ω is the *supremum* of all the finite ordinals, the smallest ordinal larger than every finite one.

The distinction matters enormously for transfinite induction and recursion. When proving something about all ordinals by transfinite induction, you need three cases: the base case (0), the successor case (if it holds for α, prove it for S(α)), and the **limit case** (if it holds for all ordinals below a limit ordinal λ, prove it for λ itself). The limit case typically requires taking a union or supremum over all smaller stages, reflecting that limit ordinals are defined exactly that way.

The reason the Von Neumann construction is preferred over alternatives is that it makes ordinal structure transparent: membership and ordering coincide, every set of ordinals has a least element (by well-foundedness), and the ordinals themselves form a proper class rather than a set — there is no "set of all ordinals" without contradiction, which connects to the Burali-Forti paradox you may encounter next. The construction grounds all of transfinite arithmetic — addition, multiplication, exponentiation — on a foundation of nothing but the empty set and the successor and union operations of ZFC set theory.
