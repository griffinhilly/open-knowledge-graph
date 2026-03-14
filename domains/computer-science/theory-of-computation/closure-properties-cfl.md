---
id: closure-properties-cfl
title: Closure Properties of Context-Free Languages
domain: computer-science
course: theory-of-computation
prerequisites:
- id: cfg-pda-equivalence
  type: hard
- id: closure-properties-regular
  type: soft
builds-toward:
- pumping-lemma-cfl
tags:
- CFL
- closure
- context-free
- operations
stage: advanced
status: validated
---

# Closure Properties of Context-Free Languages

## Core Idea
Context-free languages are closed under union, concatenation, and Kleene star, but notably NOT under intersection or complement. The union of two CFLs is proved CFL by combining their grammars with a new start variable; concatenation and star are similar. The failure of closure under intersection is shown by the counterexample {aⁿbⁿcⁿ} = {aⁿbⁿc* } ∩ {a*bⁿcⁿ}, each of which is CFL. However, the intersection of a CFL with a regular language is always CFL (proved by a product construction of PDA and DFA).

## Common Misconceptions
- Assuming CFLs are closed under complement just because regular languages are — CFLs are not.
- Forgetting the useful CFL ∩ Regular = CFL result, which is often more applicable than the general intersection non-closure.
