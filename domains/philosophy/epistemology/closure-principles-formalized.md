---
id: closure-principles-formalized
title: Closure Principles Formalized
domain: philosophy
course: epistemology
prerequisites:
- id: possible-worlds-semantics-knowledge
  type: hard
- id: epistemic-closure
  type: soft
- id: first-order-logic-syntax
  type: soft
- id: propositional-logic-introduction
  type: soft
tags:
- closure
- deductive-closure
- knowledge-transmission
stage: formal-systems
status: draft
---

# Closure Principles Formalized

## Core Idea
A closure principle states that if an agent knows p and knows that p entails q, she knows q. Formally: if Kₐp and Kₐ(p → q), then Kₐq. In possible-worlds semantics, closure fails when the agent fails to know a valid implication; for instance, one might know the premises of a long proof without knowing the conclusion. Closure is controversial: some epistemologists reject it to avoid skepticism, while others defend restricted versions.

## Explainer

You've already studied epistemic closure informally and have tools from possible-worlds semantics and propositional logic. The closure principle can now be stated precisely. Using the notation **Kₐp** for "agent a knows that p" and "→" for material implication, the basic closure principle reads: if Kₐp and Kₐ(p → q), then Kₐq. In words: if an agent knows a proposition and knows that it implies another proposition, she knows the second proposition too. This seems almost definitionally obvious — knowledge should be "closed" under known implication, the way that valid deduction transmits truth from premises to conclusions.

In possible-worlds semantics (your prerequisite), knowledge is analyzed as truth in all epistemically accessible worlds — the worlds compatible with everything the agent knows. Closure then has a natural reading: if p is true in all accessible worlds, and p → q is true in all accessible worlds, then q must also be true in all accessible worlds, so Kₐq holds. The logic seems impeccable. But closure generates a powerful **skeptical argument** via contraposition. Consider: you know you have two hands (Kₐp). "I have two hands" entails "I am not a handless brain in a vat" (p → ¬SK). By closure, you must know you are not a brain in a vat — but do you? If you cannot rule out the skeptical hypothesis directly, closure forces the conclusion backward: since you don't know ¬SK, and you know p → ¬SK, you don't know p either. This is Nozick's and Dretske's motivation for **rejecting closure**: denying the principle lets you claim ordinary knowledge while admitting ignorance of far-fetched skeptical scenarios.

Those who defend closure, like John Hawthorne and Timothy Williamson, argue that abandoning it produces its own absurdities — allowing knowledge of a conclusion while denying knowledge of its obvious consequences. **Restricted closure** principles attempt a middle path: closure holds for "obvious" or "single-step" deductions but may fail for long deductive chains where each step adds some risk of error. This connects to your logic background: in a proof of 100 steps where each step is 99% reliable, the probability of a sound conclusion is about 37% — yet we speak of knowing the premises and knowing each step follows. Whether we thereby "know" the conclusion is exactly what the closure debate forces us to confront. Formalizing the principle makes the stakes unavoidable: you must decide whether knowledge is truly closed under deduction, and the answer has consequences that reach all the way to skepticism.
