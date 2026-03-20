---
id: common-knowledge-mutual-knowledge
title: Common Knowledge and Mutual Knowledge
domain: philosophy
course: epistemology
prerequisites:
- id: knowledge-and-belief-operators
  type: hard
- id: first-order-logic-syntax
  type: soft
builds-toward:
- collective-knowledge-and-group-epistemology
tags:
- group-knowledge
- iteration
- common-ground
stage: advanced
status: draft
---

# Common Knowledge and Mutual Knowledge

## Core Idea
Mutual knowledge that p means each agent knows p; common knowledge that p means each agent knows p, each agent knows that each knows p, and so on infinitely. Formally, common knowledge is the limit of an infinite sequence of nested operators: everyone knows p, everyone knows everyone knows p, etc. Common knowledge is crucial for coordinating behavior and understanding discourse, yet is surprisingly difficult to achieve.

## Explainer

You've studied knowledge and belief operators — the formal tools for reasoning about what agents know: K_i(p) means agent i knows p. **Mutual knowledge** now extends this to groups. If agents A and B both know that it will rain, then we have mutual knowledge that it will rain: K_A(rain) ∧ K_B(rain). This seems like enough for coordination — if both people know to bring umbrellas, they'll both bring umbrellas. But a classic puzzle shows that mutual knowledge often is not enough.

Consider the **coordinated attack problem**: two generals, A and B, plan to attack simultaneously at dawn. General A sends a messenger to B confirming the attack. But A cannot attack until B confirms receipt, because if the messenger is lost, A attacks alone and loses. So B sends a confirmation. But now B can't be sure A got *that* confirmation, so A must confirm the confirmation — and so on infinitely. Each round of messaging adds one layer: "I know you know," "I know you know I know," etc. No finite number of confirmation rounds ever achieves genuine coordination certainty. What the generals need is **common knowledge** — an infinite iteration of nested knowledge that the attack is on — and that is precisely what a finite sequence of fallible messages cannot guarantee.

Formally, common knowledge that p (written CK(p)) is defined as: everyone knows p, *and* everyone knows that everyone knows p, *and* everyone knows that everyone knows that everyone knows p, *and* so on without end. Using the knowledge operator K, if we let E(p) mean "everyone knows p," then common knowledge is E(p) ∧ E(E(p)) ∧ E(E(E(p))) ∧ ... — the infinite conjunction. This is not just philosophical abstraction: common knowledge is the epistemic condition required for genuine **convention**. A word means what it means, a traffic light works as it does, money has value — all because everyone knows the convention, everyone knows everyone knows it, and so on. Without that infinite-iteration structure, coordination is fragile.

Common knowledge is also surprisingly rare in practice. You and a friend may both know that a party was awkward — but do you both know that you both know? And do you both know that? A **public announcement** — something heard simultaneously by all parties with no private uncertainty — is one of the few mechanisms that generates genuine common knowledge instantly. This is why rituals, public ceremonies, and formal declarations have such social power: they produce common knowledge by design. The mutual-to-common knowledge gap explains a host of social phenomena, from why whispered agreements are less binding than public ones to why scientific consensus requires public publication rather than private circulation of findings.


