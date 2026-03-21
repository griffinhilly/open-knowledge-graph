---
id: causal-explanation-theories
title: Causal Theories of Explanation
domain: philosophy
course: philosophy-of-science
prerequisites:
- id: scientific-explanation-introduction
  type: hard
- id: counterfactual-causation
  type: soft
builds-toward:
- laws-of-nature-metaphysics
tags:
- explanation
- causation
- mechanism
stage: advanced
status: draft
---

# Causal Theories of Explanation

## Core Idea
Many philosophers argue that genuine explanation requires causal connection, not merely deductive structure. An explanation must cite the causes responsible for an event. The DN model overlooks causation, treating all deductive arguments equally, while causal theories prioritize identifying causal mechanisms and actual causal processes.

## Questions

```yaml
- question: "Given the length of a shadow and the angle of the sun, you can validly deduce the height of the flagpole using laws of optics. What does this example reveal about the deductive-nomological (DN) model?"
  type: multiple-choice
  options:
    - "It shows the DN model works correctly — valid deductions using laws are always explanatory"
    - "It shows the DN model fails because it has no resources to distinguish explanatory from non-explanatory arguments; it would accept the shadow-to-flagpole deduction as a genuine explanation"
    - "It shows the DN model correctly identifies that the shadow doesn't explain the flagpole, because causal direction is built into the model's requirements"
    - "It shows the DN model requires probabilistic rather than deductive laws to handle asymmetric cases"
  answer: 1
  explanation: "The flagpole example is a direct counterexample to the DN model: the shadow-to-flagpole deduction is logically valid, uses real laws (optics, geometry), and satisfies every formal requirement of the DN model — yet it clearly does not explain the flagpole's height. The shadow is caused by the flagpole; it cannot explain it. The DN model has no way to exclude this inverted argument because it only checks logical form, not causal direction. This is the model's central flaw."

- question: "Salmon's causal-mechanical theory and Lewis's counterfactual approach to causal explanation differ in how they characterize causation, but they share a fundamental commitment. Which of the following best captures that shared commitment?"
  type: multiple-choice
  options:
    - "Both reduce explanation to deductive validity, differing only in which logical framework they apply"
    - "Both hold that explanation requires citing the actual causal history of an event, prioritizing causal reality over logical form"
    - "Both require that explanatory factors be deterministic causes — probabilistic causes cannot figure in genuine explanation"
    - "Both accept the DN model as correct but add a causal restriction on which laws count"
  answer: 1
  explanation: "Despite their differences — Salmon traces physical energy-transmission processes, Lewis focuses on counterfactual dependence ('had A not occurred, B would not have occurred') — both agree that explanation is fundamentally about identifying what causally produced the explanandum. The question shifts from 'does this satisfy a deductive schema?' to 'have you identified what actually brought this event about?' This shared commitment to causal reality is what distinguishes causal theories from the DN model."

- question: "A deductively valid argument that uses genuine laws of nature can fail to be an explanation if it runs causally backwards."
  type: true-false
  answer: true
  explanation: "The flagpole/shadow example establishes this directly. The shadow-to-flagpole argument is deductively valid and invokes real optical and geometric laws, yet it is not explanatory because the shadow does not cause the flagpole. Causal asymmetry — the direction of causation — is what makes the flagpole-to-shadow argument explanatory and the reverse non-explanatory. The DN model misses this asymmetry entirely by attending only to logical form."

- question: "According to causal theories of explanation, any event that causally produces another event thereby explains it — causal connection is sufficient for explanation."
  type: true-false
  answer: false
  explanation: "Causal connection is necessary but not automatically sufficient for explanation. The asymmetry matters: the flagpole causes the shadow, not vice versa, so only the flagpole-to-shadow direction is explanatory. Moreover, explanatory relevance matters — a barometer reading causally covaries with a storm but doesn't explain the storm (both are effects of atmospheric pressure). The counterfactual approach makes this precise: the explanatorily relevant factor is one whose absence would have made a difference to the outcome, not just any cause in the causal chain."

- question: "What does the flagpole/shadow example reveal about the deductive-nomological model, and what do causal theories of explanation offer as a remedy?"
  type: short-answer
  answer: "The flagpole example shows that logical validity plus laws is not sufficient for explanation: the shadow-to-flagpole deduction satisfies every formal requirement of the DN model yet explains nothing, because the shadow doesn't cause the flagpole. The DN model has no resources to block this inverted argument. Causal theories remedy this by adding a causal criterion: a genuine explanation must trace the actual causal processes or counterfactual dependencies that produced the explanandum. This injects asymmetry — the causal arrow runs only one way — so the inverted deduction is automatically excluded. The criterion shifts from logical form to causal reality."
  explanation: "This also points to a deeper issue: the DN model treats all valid arguments symmetrically, but explanation is inherently asymmetric. The asymmetry is causal — causes explain effects, not the other way around. Causal theories make this foundational rather than an afterthought."
```

## Explainer

From your prerequisite on **scientific explanation**, you know the deductive-nomological (DN) model: an explanation is a valid deductive argument where the explanandum (what is explained) follows logically from laws plus initial conditions. The DN model captures something real — explanations do invoke laws and systematic reasoning. But it has a crippling flaw: it ignores causation, and this lets in explanations that clearly get things backwards.

The **flagpole example** makes the problem vivid. You can explain the length of a shadow from the height of the flagpole and the angle of the sun. But the deductive logic works in either direction: given the shadow length and the sun's angle, you can deduce the height of the flagpole. Both deductions are equally valid, yet only one is genuinely explanatory. The flagpole causes the shadow; the shadow does not cause the flagpole. The DN model has no resources to capture this asymmetry. Causal theories of explanation are designed precisely to fix this by making causation, not deductive structure, the criterion of genuine explanation.

The central claim of causal theories is that to explain an event is to identify its **causes** — specifically, the actual causal processes that produced it. Wesley Salmon's influential **causal-mechanical theory** holds that explanation requires tracing the physical mechanisms linking cause to effect: energy transmissions, particle interactions, the continuous causal processes that connect the explainer to the explained. On this view, an explanation doesn't just show that an event was nomically necessary; it shows *how it was brought about* through real physical processes in the world.

Your soft prerequisite on **counterfactual causation** points to a second approach. Lewis's **counterfactual theory** identifies causation with counterfactual dependence: A caused B if, had A not occurred, B would not have occurred. Applied to explanation, this asks which factors in a causal history are genuinely relevant: those whose absence would have made a difference. This criterion helps exclude mere correlations and select the factors that are *explanatorily relevant* rather than just lawfully associated. Together, the causal-mechanical and counterfactual approaches share a core commitment: what makes an explanation work is not logical form but causal reality. The question shifts from "does this argument satisfy a deductive schema?" to "have you identified what actually produced this event?" This distinction will matter immediately when you encounter laws of nature — because causal theories raise the further question of whether causal explanation requires laws, or whether causation is prior to and independent of lawhood.
