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
status: draft
---

# Epistemic Logic Basics

## Core Idea
Epistemic logic extends modal logic with operators for knowledge (K) and belief (B). In this framework, Kₐp means 'agent a knows that p,' and the truth of p is determined by accessibility relations: what is true in all possible worlds accessible to the agent. Epistemic logic formalizes principles like the S5 axioms for knowledge (transitivity, introspection) and S4 for belief.

## Explainer

You already know modal logic, so you are comfortable with the idea that necessity (□) and possibility (◇) are evaluated relative to **accessibility relations** between possible worlds: □p is true at a world w when p is true at every world accessible from w. Epistemic logic plugs directly into this framework by reinterpreting the operators. Instead of one universal accessibility relation, we assign a separate relation to each agent. The formula **Kₐp** ("agent a knows that p") is then true at world w just in case p is true at every world that agent a considers possible from w — every world that, from a's perspective, could be the actual world. The accessibility relation encodes the agent's epistemic state: the closer the accessible worlds are to the actual world, the more the agent knows.

This might seem abstract, but consider a concrete case. You are holding a deck of cards and draw one face-down. You do not know which card it is. In epistemic logic terms, you are in a state where many worlds are accessible to you — one where the card is the ace of spades, one where it is the three of clubs, and so on. The proposition "the card is red" is not something you know, because there are accessible worlds where it is black. Now suppose I see the card and tell you it is red. Your accessibility relation shrinks: all the black-card worlds are eliminated. You now know the card is red, even if you still do not know the exact card. **Kₐ**(the card is red) has become true because every remaining accessible world is a red-card world.

The **S5 axiom system** for knowledge captures several intuitive principles. The T axiom says: if you know p, then p is true (Kₐp → p) — you cannot know something false. The 4 axiom says: if you know p, you know that you know p (positive introspection). The 5 axiom says: if you do not know p, you know that you do not know p (negative introspection). Together these create a very idealized picture of an agent who has perfect insight into their own epistemic state. **S4**, the weaker system often used for belief, drops the 5 axiom: you can fail to know that you do not believe something, which corresponds better to how humans actually work — we are often uncertain about our own doxastic states.

Where epistemic logic becomes genuinely powerful is in **multi-agent settings**. We can write not just Kₐp but also KₐKbp ("a knows that b knows p") or ¬Kₐ¬Kbp ("a does not know that b doesn't know p"). This opens the way to **common knowledge**, written CK(p): a state where all agents know p, and all agents know that all agents know p, and so on ad infinitum. Common knowledge is surprisingly difficult to achieve — the classic "muddy children" puzzle shows that even obvious visible facts don't become common knowledge until a public announcement makes them so. This formalism connects directly to game theory and computer science, where reasoning about what other agents know is essential for designing protocols and analyzing strategic interaction.

