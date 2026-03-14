---
id: modal-logic-intro
title: Introduction to Modal Logic
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: propositional-semantics
  type: hard
- id: first-order-semantics
  type: soft
- id: intuitionistic-logic-intro
  type: soft
tags:
- modal-logic
- possible-worlds
- Kripke-semantics
- necessity
- possibility
stage: formal-systems
status: validated
---

# Introduction to Modal Logic

## Core Idea
Modal logic extends propositional logic with operators □ ('necessarily') and ◇ ('possibly'). Kripke semantics interprets □φ as 'φ is true in all accessible worlds' and ◇φ as 'φ is true in some accessible world.' Different systems of modal logic arise by imposing different conditions on the accessibility relation: system K (no conditions), T (reflexive), S4 (reflexive and transitive), S5 (equivalence relation). Modal logic has applications in philosophy (epistemic and deontic logic), computer science (temporal logic for program verification), and linguistics (expressing necessity and possibility in natural language).

## How It's Best Learned
Draw Kripke frames as directed graphs and evaluate □φ and ◇φ at each world by inspecting its successors. Verify which axioms (T: □φ → φ, 4: □φ → □□φ, B: φ → □◇φ) hold under reflexive, transitive, and symmetric frames respectively.

## Common Misconceptions
- Modal necessity (□φ) is not the same as logical validity (⊨ φ); □p can be true at a world even if p is not a tautology.
- Different modal systems are not competing — they model different notions of necessity (metaphysical, epistemic, deontic) and should be chosen based on the intended interpretation.
