---
id: insolvability-of-the-quintic
title: Insolvability of the Quintic
domain: mathematics
course: abstract-algebra
prerequisites:
- id: galois-groups
  type: hard
- id: polynomial-rings
  type: hard
tags:
- quintic
- solvability
- radicals
stage: advanced
status: draft
---

# Insolvability of the Quintic

## Core Idea
A polynomial is solvable by radicals if roots can be expressed using field operations and nth roots. The Galois group determines solvability: f is solvable iff its Galois group is solvable. The general quintic has Galois group S_5, which is not solvable, proving the quintic is generally insolvable.

## Explainer

For thousands of years, mathematicians searched for a formula that would solve fifth-degree (quintic) equations by radicals — the way the quadratic formula solves degree-2 equations, and analogous formulas solve degrees 3 and 4. In the early 19th century, Abel and Galois proved no such formula exists. This is one of mathematics' landmark negative results: not "we haven't found the formula yet" but "the formula cannot exist." Understanding why requires the Galois correspondence you've already studied.

A polynomial is **solvable by radicals** if its roots can be written using the four field operations (addition, subtraction, multiplication, division) together with taking nth roots — just like the quadratic formula √(b²−4ac). The Galois group of a polynomial encodes the symmetries among its roots: it is the group of field automorphisms that permute the roots while fixing the base field. The central theorem connecting these ideas: a polynomial f(x) is solvable by radicals if and only if its Galois group Gal(f) is a **solvable group**.

A group G is **solvable** if it has a subnormal series G = G₀ ⊃ G₁ ⊃ ⋯ ⊃ Gₖ = {e} where each quotient Gᵢ/Gᵢ₊₁ is abelian. Abelian quotients correspond (loosely) to the layers of taking radicals one at a time. The symmetric groups S₁, S₂, S₃, S₄ are all solvable — which is why formulas exist for degrees 1 through 4. But **S₅ is not solvable**: its only normal subgroups are {e}, A₅, and S₅ itself, and A₅ is simple (no further normal subgroups), so the chain of abelian quotients cannot be completed. Since a general quintic has Galois group isomorphic to S₅ (it permutes five roots with full symmetry), no radical formula can exist.

This result reframes what it means to "solve" an equation. Rather than asking "find these roots," Galois theory asks "what symmetries do the roots have?" The impossibility of the quintic formula isn't a limitation of our technique — it is a structural fact about the symmetry group of the problem. Specific quintics can be solvable by radicals (those whose Galois group happens to be solvable), and numerical methods can always approximate roots. But the general quintic, the one whose coefficients are truly free parameters, lives in a symmetry world — S₅ — that is simply too complex for radicals to reach.
