---
id: natural-deduction-fol
title: Natural Deduction for First-Order Logic
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: natural-deduction-propositional
  type: hard
- id: first-order-logic-syntax
  type: hard
- id: first-order-semantics
  type: soft
- id: substitution-and-unification
  type: hard
builds-toward:
- fol-soundness-completeness
tags:
- natural-deduction
- quantifier-rules
- universal
- existential
- FOL-proof
stage: formal-systems
status: validated
---
# Natural Deduction for First-Order Logic

## Core Idea
Natural deduction for FOL extends propositional natural deduction with four quantifier rules. Universal introduction (∀I) derives ∀x φ(x) from φ(a) where a is an arbitrary fresh constant not mentioned elsewhere. Universal elimination (∀E) instantiates ∀x φ(x) to φ(t) for any term t. Existential introduction (∃I) derives ∃x φ(x) from φ(t). Existential elimination (∃E) discharges an assumption φ(a) when proving a conclusion that does not mention the fresh constant a. The freshness conditions on ∀I and ∃E are critical: they formalize the logical principle that reasoning about 'an arbitrary object' must not smuggle in extra assumptions.

## How It's Best Learned
Prove simple theorems like ∀x P(x) → ∀x (P(x) ∨ Q(x)) in Fitch notation before attempting ∃-elimination. Pay close attention to which constants appear in the context when applying freshness conditions.

## Common Misconceptions
- The fresh constant in ∀I and ∃E is a proof artifact — it does not exist in the theorem statement.
- ∀E does not require a fresh constant; only ∀I and ∃E have freshness restrictions.

## Questions

```yaml
- question: "You want to prove ∀x P(x) by deriving P(a) from your premises. The constant a already appears in one of your undischarged assumptions. Which rule is blocked?"
  type: multiple-choice
  options:
    - "∀E — universal elimination cannot be applied to premises containing a"
    - "∀I — universal introduction requires a fresh constant not appearing in any undischarged assumption"
    - "∃I — existential introduction requires the witness to be fresh"
    - "∃E — you must discharge a before generalizing"
  answer: 1
  explanation: "∀I (universal introduction) has a freshness condition: the constant a must not appear in any undischarged assumption. The reason is that if a already appears in an assumption, then P(a) was derived using some specific property of a — you cannot legitimately conclude that every object has property P. Only ∀I and ∃E have freshness conditions; ∀E and ∃I are unconstrained."

- question: "In existential elimination (∃E), you derive conclusion C from ∃x φ(x) using a fresh constant a. Why must a not appear in C?"
  type: multiple-choice
  options:
    - "Because fresh constants are automatically removed from all formulas when ∃E is applied"
    - "Because C must hold regardless of which specific object witnesses the existential, and mentioning a would tie C to that particular witness"
    - "Because ∃E discharges the assumption φ(a), which removes a from the proof's scope entirely"
    - "Because first-order logic does not allow constants to appear in conclusions, only in premises"
  answer: 1
  explanation: "The whole point of ∃E is that you don't know which object witnesses ∃x φ(x) — you name it a and reason from φ(a). If your conclusion C mentioned a, it would assert something about that specific (unknown) witness, not about the world in general. The freshness condition ensures that C is a fact that follows from ∃x φ(x) alone, independent of which witness was chosen. The fresh constant is a proof artifact — a device for reasoning — not an object the theorem is about."

- question: "Universal elimination (∀E) has no freshness condition: from ∀x φ(x), you may derive φ(t) for any term t already appearing in the proof."
  type: true-false
  answer: true
  explanation: "True. ∀E is unconstrained — you may substitute any term t for x, including terms that already appear everywhere in your proof. This makes sense: if everything has property φ, then this particular thing (referred to by t) has it too. There is no freshness needed because you are instantiating a universal claim to a specific case, not generalizing from a specific case to all cases."

- question: "The fresh constant a introduced by ∃E appears in the final theorem that is ultimately proved."
  type: true-false
  answer: false
  explanation: "False. The fresh constant is a proof artifact — it is the name given to the unknown witness during the ∃E derivation, but it is discharged when ∃E concludes. The final conclusion C is required by the rule to not mention a at all. This mirrors the natural language phrasing: 'suppose the witness is called a; then... therefore C' — C is the conclusion, and the name a was just scaffolding."

- question: "Explain why applying ∀I to a constant a that already appears in an undischarged assumption would make the proof unsound."
  type: short-answer
  answer: "If a appears in an undischarged assumption, then the derivation of φ(a) relied on some specific property of a that was assumed. Applying ∀I would claim that because φ(a) was proved, φ holds for all objects — but the proof only worked because a has whatever special property the assumption ascribed to it. Other objects may not have that property. The freshness condition ensures that a is genuinely arbitrary: if a appears nowhere in the undischarged assumptions, then nothing special was assumed about it, and the derivation of φ(a) must work for any object."
  explanation: "A concrete example: suppose you assume P(a) and then derive P(a) trivially. Applying ∀I would 'prove' ∀x P(x) — everything has property P — from a mere assumption that a does. This is clearly invalid. The freshness condition blocks exactly this inference by requiring that a was not assumed to have any properties."
```

## Explainer

You already know natural deduction for propositional logic: every connective has an introduction rule (how to prove it) and an elimination rule (how to use it). FOL natural deduction extends this system by giving introduction and elimination rules for the two quantifiers ∀ and ∃. The rules look symmetric on the surface but have subtly different constraints that reflect a deep logical distinction: the difference between *an arbitrary object* and *a specific unknown object*.

**Universal elimination (∀E)** is the simple one: from ∀x φ(x), you can derive φ(t) for *any* term t you like. If everything has a property, then this specific thing has it. No freshness condition is needed — t can be anything, including terms that already appear in your proof. This is just instantiation. **Universal introduction (∀I)** is the inverse and is more constrained: to derive ∀x φ(x), you must have derived φ(a) where a is a **fresh constant** — one that doesn't appear in any undischarged assumption. The fresh constant represents a *generic* object: if you proved φ(a) without using any special property of a, then a stands for any object whatsoever, and you're entitled to universally generalize.

**Existential introduction (∃I)** is also unconstrained: from φ(t), derive ∃x φ(x). You have a witness, so something satisfies the property. **Existential elimination (∃E)** is the tricky rule. From ∃x φ(x) and a derivation of conclusion C from assumption φ(a) (where a is fresh), you may derive C. The idea: you don't know *which* object witnesses ∃x φ(x), so you name it a and reason from what you know about it (just that it satisfies φ). If you reach a conclusion C that doesn't mention a, then C holds regardless of which witness a actually is. The freshness condition on a is essential: if a appeared in your other assumptions or in C, your reasoning would smuggle in extra information about the witness, corrupting the inference.

A worked example cements the rules. Prove ∃x P(x) → ∃x (P(x) ∨ Q(x)). Assume ∃x P(x). Apply ∃E: assume P(a) for fresh a. By ∃I on P(a) ∨ Q(a) (derived via ∨I from P(a)), derive ∃x (P(x) ∨ Q(x)). This conclusion doesn't mention a, so ∃E discharges the assumption P(a) and gives ∃x (P(x) ∨ Q(x)) from ∃x P(x). The proof works because a serves as a stand-in for "whichever object witnesses the existential" — we don't need to know which one it is, only that it satisfies P. This four-rule extension of propositional natural deduction is complete for FOL: every valid first-order sentence has a natural deduction proof.

