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

## Questions

```yaml
- question: "In a Kripke frame with worlds {w₁, w₂, w₃} where w₁ accesses w₂ and w₁ accesses w₃, proposition p is true at w₂ but false at w₃. What is the truth value of ◇p at w₁?"
  type: multiple-choice
  options: ["False, because p is false at w₃ which w₁ accesses", "True, because p is true at w₂ which w₁ accesses", "True, because □p holds at w₁", "Undefined, because p has different truth values at accessible worlds"]
  answer: 1
  explanation: "◇p ('possibly p') is true at a world if p is true in at least one accessible world. Since w₁ accesses w₂ and p is true at w₂, ◇p is true at w₁ — regardless of what happens at w₃. Only one witness world is required for possibility. This contrasts with □p ('necessarily p'), which requires p to be true at ALL accessible worlds — which would fail here because p is false at w₃."

- question: "In modal logic, if □p is true at a world w, then p must be a logical tautology."
  type: true-false
  answer: false
  explanation: "□p means p is true in all worlds accessible from w — not that p is true in all possible worlds of all frames, which is what logical validity (⊨ p) requires. In a frame where only a few worlds are accessible from w, □p can hold even if p is false elsewhere in the same frame or in other frames entirely. Necessity is frame-relative and world-relative; tautology is an absolute semantic property."

- question: "What distinguishes modal system T from system K, and what feature of the accessibility relation accounts for this difference?"
  type: short-answer
  answer: "System T adds the axiom □φ → φ (whatever is necessary is actually true), which corresponds to making the accessibility relation reflexive — every world accesses itself. System K imposes no conditions on accessibility."
  explanation: "In system K, a world might not access itself, so □φ could be true at w (φ holds in all worlds w sees) while φ is false at w (w doesn't see itself). Adding reflexivity ensures every world is among its own accessible worlds, which forces □φ → φ: if φ holds everywhere accessible, and w is accessible from itself, then φ holds at w. This axiom is intuitively plausible for metaphysical necessity — if something is necessarily true, it should be actually true."
```

## Explainer

You already know from propositional semantics that every formula is evaluated relative to a truth assignment — a function mapping propositional variables to true or false. Modal logic introduces a richer semantic structure: instead of a single truth assignment, you have many possible worlds, each with its own assignment, connected by an accessibility relation. The intuition is that necessity means "true in every way things could be" and possibility means "true in some way things could be." Kripke semantics makes this precise.

A Kripke frame is a pair (W, R) where W is a set of worlds and R is a binary accessibility relation on W. A Kripke model adds a valuation: for each world w and proposition variable p, the valuation says whether p is true at w. Given a model, you evaluate □φ at a world w by checking whether φ is true at every world accessible from w (every v such that wRv). You evaluate ◇φ at w by checking whether φ is true at some world accessible from w. If a world has no accessible worlds at all, □φ is vacuously true and ◇φ is false at that world. Evaluating formulas by inspecting a drawn Kripke diagram — with worlds as nodes and accessibility as directed edges — is the most reliable way to build intuition.

Different modal systems arise by imposing structural constraints on the accessibility relation. The base system K imposes none. System T adds reflexivity (wRw for all w), yielding the axiom T: □φ → φ — whatever is necessary is actually true. System S4 adds transitivity (if wRv and vRu then wRu), yielding axiom 4: □φ → □□φ — if φ is necessary, then it's necessarily necessary. System S5 uses an equivalence relation (reflexive, transitive, and symmetric), collapsing the accessibility structure so that □φ and ◇φ depend only on which worlds exist, not on which ones a given world can "see." Each system is appropriate for different interpretations of necessity. Epistemic logic (knowledge) commonly uses S4 or S5. Deontic logic (obligation) uses its own variants. Temporal logic uses frames where worlds are time points and accessibility corresponds to temporal precedence.

The most important misconception to avoid is conflating □φ with logical validity (⊨ φ). Logical validity means φ is true under every possible interpretation — every assignment in every frame. □φ at a world w means φ is true in all worlds accessible from w in this particular model. These are very different claims. A proposition like "it is raining" can be necessary at some world in some model (every world that world accesses has rain), without "it is raining" being a tautology. Similarly, ◇φ at w does not mean φ is satisfiable in the general logical sense — it means there is an accessible world where φ holds, in this specific model.

The modal operators also interact with the existing propositional connectives in ways worth knowing. □ distributes over conjunction: □(φ ∧ ψ) ↔ (□φ ∧ □ψ). But □ does not distribute over disjunction in the same way, and these asymmetries matter in proofs. The duality of □ and ◇ mirrors the duality of ∀ and ∃ in predicate logic — and this is not a coincidence. One of the deep results in modal logic is that Kripke semantics for modal logic corresponds to a fragment of first-order logic, allowing translation between the two frameworks. If you continue into advanced logic, this correspondence will be a recurring theme.
