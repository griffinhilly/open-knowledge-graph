---
id: epistemic-logic-basics
title: Epistemic Logic Basics
domain: philosophy
course: epistemology
prerequisites:
- id: formal-epistemology-introduction
  type: hard
- id: modal-logic-intro
  type: hard
- id: first-order-logic-syntax
  type: hard
- id: propositional-logic-introduction
  type: soft
builds-toward:
- possible-worlds-semantics-knowledge
- knowledge-and-belief-operators
tags:
- modal-logic
- knowledge-operators
- belief
stage: formal-systems
status: validated
---

# Epistemic Logic Basics

## Core Idea
Epistemic logic extends modal logic with operators for knowledge (K) and belief (B). In this framework, Kₐp means 'agent a knows that p,' and the truth of p is determined by accessibility relations: what is true in all possible worlds accessible to the agent. Epistemic logic formalizes principles like the S5 axioms for knowledge (transitivity, introspection) and S4 for belief.

## Questions

```yaml
- question: "In possible worlds semantics, what does it mean for Kₐp ('agent a knows that p') to be true at world w?"
  type: multiple-choice
  options:
    - "p is true at world w, and agent a believes that p"
    - "p is true at every world that agent a considers possible from w"
    - "p is true at some world accessible to agent a from w"
    - "Agent a has a justified true belief in p according to traditional epistemology"
  answer: 1
  explanation: "Kₐp is true at w just when p holds at every world in a's accessibility set from w — every world a cannot rule out. This is why knowledge requires p to be settled across all epistemic possibilities: if there is even one accessible world where p is false, the agent doesn't know p. Option A confuses the modal-logic framework with JTB epistemology. Option C is the condition for possibility (◇p), not knowledge. The universal quantifier over accessible worlds is what makes K behave like the necessity operator □."

- question: "An agent knows p but does NOT know that she knows p. Which axiom of S5 epistemic logic does this situation violate?"
  type: multiple-choice
  options:
    - "The T axiom (Kₐp → p), because knowledge must be factive"
    - "The 4 axiom (Kₐp → KₐKₐp), the positive introspection axiom"
    - "The 5 axiom (¬Kₐp → Kₐ¬Kₐp), the negative introspection axiom"
    - "The K axiom (Kₐ(p→q) → (Kₐp → Kₐq)), the distribution axiom"
  answer: 1
  explanation: "The 4 axiom (Kₐp → KₐKₐp) states that if you know p, you know that you know p — positive introspection. If an agent knows p but doesn't know she knows p, this axiom is violated. Students often confuse the 4 and 5 axioms: the 5 axiom concerns *negative* introspection (not knowing → knowing you don't know). Dropping the 5 axiom while keeping T and 4 gives S4, often used for belief, where you can fail to recognize your own ignorance."

- question: "In epistemic logic, if a proposition p is actually true in the world, then every agent in the system knows p."
  type: true-false
  answer: false
  explanation: "The T axiom runs in only one direction: knowledge implies truth (Kₐp → p). Truth does not imply knowledge. An agent may be in a world where p is true but still have accessible worlds where p is false — those worlds are ones the agent cannot rule out. In the card example from the explainer: the card being red is true, but before you see it, you don't know it because red-false worlds remain epistemically accessible to you."

- question: "Common knowledge of p requires more than all agents individually knowing p — it additionally requires each agent to know that every other agent knows p, and this iteration continues infinitely."
  type: true-false
  answer: true
  explanation: "Common knowledge CK(p) is an infinite conjunction: everyone knows p, AND everyone knows that everyone knows p, AND everyone knows that everyone knows that everyone knows p, and so on. This is strictly stronger than 'everyone knows p.' The muddy children puzzle illustrates why: even when all children can see which children are muddy (so each knows the relevant facts), no child can act on this until a public announcement creates the infinite chain of mutual knowledge."

- question: "Explain what the accessibility relation represents in epistemic logic and how it encodes what an agent knows."
  type: short-answer
  answer: "The accessibility relation for agent a at world w is the set of worlds that a cannot distinguish from w — worlds that, from a's perspective, could be the actual world. An agent knows p at w if and only if p is true at every world in this set. A larger accessibility set means the agent knows less (more possibilities remain open); a smaller set means more is settled."
  explanation: "This is the central mechanism of the semantics. Gaining knowledge corresponds to shrinking the accessibility set: new information eliminates worlds that are now inconsistent with what the agent has learned. The axioms T, 4, and 5 correspond to structural properties of the accessibility relation: T requires reflexivity (the actual world is always accessible — you can't rule out reality), 4 requires transitivity, and 5 requires symmetry (Euclidean property), making the relation an equivalence relation in S5."
```

## Explainer

You already know modal logic, so you are comfortable with the idea that necessity (□) and possibility (◇) are evaluated relative to **accessibility relations** between possible worlds: □p is true at a world w when p is true at every world accessible from w. Epistemic logic plugs directly into this framework by reinterpreting the operators. Instead of one universal accessibility relation, we assign a separate relation to each agent. The formula **Kₐp** ("agent a knows that p") is then true at world w just in case p is true at every world that agent a considers possible from w — every world that, from a's perspective, could be the actual world. The accessibility relation encodes the agent's epistemic state: the closer the accessible worlds are to the actual world, the more the agent knows.

This might seem abstract, but consider a concrete case. You are holding a deck of cards and draw one face-down. You do not know which card it is. In epistemic logic terms, you are in a state where many worlds are accessible to you — one where the card is the ace of spades, one where it is the three of clubs, and so on. The proposition "the card is red" is not something you know, because there are accessible worlds where it is black. Now suppose I see the card and tell you it is red. Your accessibility relation shrinks: all the black-card worlds are eliminated. You now know the card is red, even if you still do not know the exact card. **Kₐ**(the card is red) has become true because every remaining accessible world is a red-card world.

The **S5 axiom system** for knowledge captures several intuitive principles. The T axiom says: if you know p, then p is true (Kₐp → p) — you cannot know something false. The 4 axiom says: if you know p, you know that you know p (positive introspection). The 5 axiom says: if you do not know p, you know that you do not know p (negative introspection). Together these create a very idealized picture of an agent who has perfect insight into their own epistemic state. **S4**, the weaker system often used for belief, drops the 5 axiom: you can fail to know that you do not believe something, which corresponds better to how humans actually work — we are often uncertain about our own doxastic states.

Where epistemic logic becomes genuinely powerful is in **multi-agent settings**. We can write not just Kₐp but also KₐKbp ("a knows that b knows p") or ¬Kₐ¬Kbp ("a does not know that b doesn't know p"). This opens the way to **common knowledge**, written CK(p): a state where all agents know p, and all agents know that all agents know p, and so on ad infinitum. Common knowledge is surprisingly difficult to achieve — the classic "muddy children" puzzle shows that even obvious visible facts don't become common knowledge until a public announcement makes them so. This formalism connects directly to game theory and computer science, where reasoning about what other agents know is essential for designing protocols and analyzing strategic interaction.

