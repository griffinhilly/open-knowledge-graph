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

## Explainer

You already know that ordinals are a well-ordered extension of the natural numbers that reach into the transfinite. The Von Neumann construction answers a foundational question: what *are* ordinals made of, if we want to build everything from pure sets? The elegant answer is that each ordinal simply *is* the set of all ordinals that came before it. So 0 = ∅ (nothing came before zero), 1 = {0} = {∅}, 2 = {0, 1} = {∅, {∅}}, and so on. At every stage, an ordinal contains exactly its predecessors as elements, which means that comparing two ordinals by "less than" is the same as the ∈ relation — α < β if and only if α ∈ β.

With this construction established, every ordinal falls into one of two categories. A **successor ordinal** is one that has an immediate predecessor: S(α) = α ∪ {α} adds α itself as a new element to the set α, producing the next ordinal. All finite ordinals (1, 2, 3, …) are successor ordinals, as are ordinals like ω+1, ω+2, and so on. A **limit ordinal** has no immediate predecessor — it cannot be reached by a single successor step. The first and most important limit ordinal is **ω**, the set of all finite ordinals: ω = {0, 1, 2, 3, …}. There is no ordinal just below ω in the way that 4 is just below 5; instead ω is the *supremum* of all the finite ordinals, the smallest ordinal larger than every finite one.

The distinction matters enormously for transfinite induction and recursion. When proving something about all ordinals by transfinite induction, you need three cases: the base case (0), the successor case (if it holds for α, prove it for S(α)), and the **limit case** (if it holds for all ordinals below a limit ordinal λ, prove it for λ itself). The limit case typically requires taking a union or supremum over all smaller stages, reflecting that limit ordinals are defined exactly that way.

The reason the Von Neumann construction is preferred over alternatives is that it makes ordinal structure transparent: membership and ordering coincide, every set of ordinals has a least element (by well-foundedness), and the ordinals themselves form a proper class rather than a set — there is no "set of all ordinals" without contradiction, which connects to the Burali-Forti paradox you may encounter next. The construction grounds all of transfinite arithmetic — addition, multiplication, exponentiation — on a foundation of nothing but the empty set and the successor and union operations of ZFC set theory.
