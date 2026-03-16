---
id: counterfactual-truth-modality
title: Counterfactual Truth Conditions and Modal Metaphysics
domain: philosophy
course: metaphysics
prerequisites:
- id: counterfactual-causation
  type: hard
- id: possible-worlds-semantics
  type: hard
- id: modal-semantics-possible-worlds
  type: soft
- id: modal-logic-intro
  type: soft
builds-toward:
- causal-order-temporal-order
tags:
- counterfactuals
- modality
- truth-conditions
- causation
- semantics
stage: formal-systems
status: draft
---

# Counterfactual Truth Conditions and Modal Metaphysics

## Core Idea
Counterfactual conditionals are true in virtue of facts about how nearby possible worlds are structured rather than the actual world alone. Lewis's theory uses similarity metrics between possible worlds: 'if A then B' is true when A is false in the actual world but B is true in the closest worlds where A is true. This directly connects counterfactual truth to metaphysical questions about possible worlds.

## Explainer

From your study of counterfactual causation, you know that causal claims are often analyzed in terms of counterfactual dependence: event C caused event E just in case, had C not occurred, E would not have occurred. And from your study of possible worlds semantics, you know that modal claims are interpreted as quantification over possible worlds: what's necessary is true in all worlds, what's possible is true in some. Counterfactual truth conditions bring these two frameworks together in a way that resolves a pressing puzzle: how can a conditional claim be true when its antecedent is false?

The puzzle is real. Standard material conditionals ("if P then Q") are vacuously true whenever P is false — which means "if the sun had risen in the west today, we would all be speaking Latin" is technically true by the same logic as "if I had skipped breakfast, I would have been hungry." Clearly these are not the same kind of claim. **Counterfactual conditionals** ("if it had rained, the streets would be wet") demand a different analysis because they support genuine reasoning about causation, planning, and responsibility. Lewis's solution exploits the possible worlds framework: a counterfactual "if A had been the case, B would have been the case" is true when, among all the possible worlds where A is true, the ones **most similar to the actual world** are ones where B is also true.

The key technical concept is the **similarity metric** (also called a **closeness ordering**) among possible worlds. You hold the actual world fixed and ask: which worlds differ from it minimally while still making the antecedent true? A world where it rained in your city yesterday but everything else is as close to normal as possible is "closer" to actuality than a world where the laws of physics differ. If in those close rain-worlds the streets are wet, the counterfactual is true. This means counterfactual truth is not just about logical form — it depends on substantive metaphysical facts about what kinds of changes to the actual world are "small."

The deepest challenge is specifying what similarity means without circularity. Lewis distinguished between similarity with respect to **laws of nature** and similarity with respect to **particular facts**, and argued that preserving laws counts for more than preserving a wider spread of particular facts. Critics including Stalnaker have proposed alternative semantics, and the debate about what makes worlds "close" has proven to be a productive pressure point in both modal metaphysics and the philosophy of causation. The connection you established in counterfactual causation now becomes visible in full: causal claims are counterfactual claims, and counterfactual claims are made true (or false) by the structure of modal space.

