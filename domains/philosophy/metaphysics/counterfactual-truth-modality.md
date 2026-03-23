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
builds-toward: []
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

## Questions

```yaml
- question: "You want to evaluate: 'If the moon were made of cheese, the tides would be unaffected.' Standard material conditional logic says this is automatically true because the antecedent is false. What does Lewis's possible-worlds account say instead?"
  type: multiple-choice
  options:
    - "It is also automatically true, for the same reason — false antecedents make all conditionals true on Lewis's view as well"
    - "It is evaluated by asking whether, in the closest possible worlds where the moon is made of cheese, the tides are unaffected — the truth depends on the structure of those worlds"
    - "It is false, because the consequent does not follow logically from the antecedent"
    - "It cannot be evaluated because the antecedent describes a physical impossibility"
  answer: 1
  explanation: "Lewis's account rejects the material conditional's vacuous truth for counterfactuals. Instead, you identify the possible worlds where the antecedent is true that are *most similar* to the actual world, and check whether the consequent holds there. This can give a determinate truth value for counterfactuals with false antecedents — it is not automatically true. The closest cheese-moon worlds presumably preserve the law of gravitation, so the tidal claim's truth turns on physics in those worlds, not on the falsity of the antecedent."

- question: "Lewis argues that preserving laws of nature matters more than preserving a large spread of particular facts when determining which worlds are 'closest.' Why?"
  type: multiple-choice
  options:
    - "Because laws of nature are simpler to describe, making similarity comparisons more tractable"
    - "Because a world with different laws diverges radically from actuality — small differences in particular facts are more like the actual world than a world with altered physics"
    - "Because particular facts are unobservable at the level of possible worlds"
    - "Because material conditionals only concern lawlike generalizations, not individual facts"
  answer: 1
  explanation: "Lewis's intuition is that two worlds can differ in many particular facts and still be 'close,' but if they differ in their laws of nature they are radically different kinds of worlds. This is because laws of nature govern everything in a world — changing them changes counterfactually infinite facts downstream. A world where one minor event went differently shares laws with the actual world and is therefore much more similar to it than a world with identical particular history but different physical laws. This asymmetry is what makes Lewis's similarity metric non-trivial."

- question: "On Lewis's account, a counterfactual 'If A had been the case, B would have been the case' is true whenever A is actually false."
  type: true-false
  answer: false
  explanation: "This describes the *material conditional*, not Lewis's counterfactual. The material conditional is vacuously true whenever its antecedent is false — which is exactly the problem Lewis's theory is designed to solve. On Lewis's view, the counterfactual is true only when B holds in the *closest* A-worlds — the possible worlds most similar to the actual world in which A is true. A false antecedent alone says nothing about the truth of the counterfactual; you must examine the modal neighborhood of the actual world."

- question: "The truth of a counterfactual conditional depends on facts about possible worlds other than the actual world."
  type: true-false
  answer: true
  explanation: "This is the central claim of Lewis's semantics. A counterfactual 'If A had been the case, B would have been the case' is true or false in virtue of facts about how nearby possible worlds are structured — specifically, whether B holds in the A-worlds closest to actuality. The actual world alone cannot settle the matter, since A is false in the actual world and we need to evaluate what would have happened had it been true. This is what makes counterfactual truth irreducibly modal."

- question: "Why can't counterfactual conditionals be analyzed as material conditionals, and what specific problem does this create for causal reasoning?"
  type: short-answer
  answer: "The material conditional is vacuously true whenever its antecedent is false. Since counterfactual antecedents are always false in the actual world (that's what makes them counterfactual), every counterfactual would come out true — 'If I had skipped breakfast, the sun would have risen in the west' would be as true as 'If I had skipped breakfast, I would have been hungry.' This collapses all causal distinctions: causal claims like 'C caused E because had C not occurred, E would not have occurred' are expressed as counterfactuals, and if all counterfactuals with false antecedents are equally true, you cannot distinguish genuine causes from irrelevant antecedents."
  explanation: "The failure of the material conditional for counterfactuals is not a minor technicality — it undermines the entire project of using counterfactuals to analyze causation. Lewis's solution, which ties truth to facts about the closest possible worlds, gives counterfactuals non-trivial truth conditions. Causal claims can then be distinguished from accidental correlations: C genuinely caused E only if, in the closest worlds where C is absent, E is also absent — not just in any world where C is absent."
```

## Explainer

From your study of counterfactual causation, you know that causal claims are often analyzed in terms of counterfactual dependence: event C caused event E just in case, had C not occurred, E would not have occurred. And from your study of possible worlds semantics, you know that modal claims are interpreted as quantification over possible worlds: what's necessary is true in all worlds, what's possible is true in some. Counterfactual truth conditions bring these two frameworks together in a way that resolves a pressing puzzle: how can a conditional claim be true when its antecedent is false?

The puzzle is real. Standard material conditionals ("if P then Q") are vacuously true whenever P is false — which means "if the sun had risen in the west today, we would all be speaking Latin" is technically true by the same logic as "if I had skipped breakfast, I would have been hungry." Clearly these are not the same kind of claim. **Counterfactual conditionals** ("if it had rained, the streets would be wet") demand a different analysis because they support genuine reasoning about causation, planning, and responsibility. Lewis's solution exploits the possible worlds framework: a counterfactual "if A had been the case, B would have been the case" is true when, among all the possible worlds where A is true, the ones **most similar to the actual world** are ones where B is also true.

The key technical concept is the **similarity metric** (also called a **closeness ordering**) among possible worlds. You hold the actual world fixed and ask: which worlds differ from it minimally while still making the antecedent true? A world where it rained in your city yesterday but everything else is as close to normal as possible is "closer" to actuality than a world where the laws of physics differ. If in those close rain-worlds the streets are wet, the counterfactual is true. This means counterfactual truth is not just about logical form — it depends on substantive metaphysical facts about what kinds of changes to the actual world are "small."

The deepest challenge is specifying what similarity means without circularity. Lewis distinguished between similarity with respect to **laws of nature** and similarity with respect to **particular facts**, and argued that preserving laws counts for more than preserving a wider spread of particular facts. Critics including Stalnaker have proposed alternative semantics, and the debate about what makes worlds "close" has proven to be a productive pressure point in both modal metaphysics and the philosophy of causation. The connection you established in counterfactual causation now becomes visible in full: causal claims are counterfactual claims, and counterfactual claims are made true (or false) by the structure of modal space.

