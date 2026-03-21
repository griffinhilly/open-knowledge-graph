---
id: idealization-in-science
title: Idealization in Science
domain: philosophy
course: philosophy-of-science
prerequisites:
- id: scientific-models-representation
  type: hard
- id: laws-of-nature
  type: soft
builds-toward:
- reduction-emergence-science
- philosophy-of-physics
tags:
- idealization
- approximation
- simplification
- models
stage: advanced
status: draft
---

# Idealization in Science

## Core Idea
Scientific models are typically idealizations: they ignore complicating factors, assume unrealistic conditions, and employ false simplifications. Physics assumes frictionless surfaces; biology assumes infinite populations; economics assumes perfectly rational agents. Idealizations enable tractable analysis and explanation. However, they raise philosophical questions: How do false idealizations provide true explanations? When is an idealization legitimate versus misleading? How do we apply idealized theories to real systems?

## Questions

```yaml
- question: "Population genetics uses the Hardy-Weinberg equilibrium, derived by assuming infinite population size — a condition no real population meets. Biologists then use deviations from Hardy-Weinberg as evidence of selection, drift, or migration. This use of the infinite-population idealization is best described as:"
  type: multiple-choice
  options:
    - "A computational shortcut that could be replaced by a finite-population model without loss of insight"
    - "A Galilean idealization performing explanatory work — the false assumption generates the null model that makes real deviations scientifically meaningful"
    - "An Aristotelian abstraction that reveals a truth holding approximately in all large populations"
    - "A misleading idealization that should be replaced by models of actual population sizes"
  answer: 1
  explanation: "This is the key distinction between idealizations that merely simplify computation and those that do explanatory work. Hardy-Weinberg is not just 'easier to calculate' — the infinite-population assumption generates the equilibrium itself, and that equilibrium serves as the scientific null model against which real populations are compared. Removing the idealization (using a realistic finite N) would destroy the null model's clarity. This is why it cannot be dismissed as merely a computational convenience: the false assumption is structurally necessary for the inference pattern."

- question: "The distinction between Galilean idealization and Aristotelian abstraction is that:"
  type: multiple-choice
  options:
    - "Galilean idealization applies to physics; Aristotelian abstraction applies to biology and social science"
    - "Galilean idealization removes accidental features to reveal universal truths; Aristotelian abstraction introduces deliberate falsehoods to simplify analysis"
    - "Galilean idealization introduces deliberately false assumptions to render systems tractable; Aristotelian abstraction removes accidental features to reveal properties that genuinely hold"
    - "They are synonyms — both describe the practice of simplifying models to make them mathematically manageable"
  answer: 2
  explanation: "The terms are often confused. Aristotelian abstraction is a genuine generalization: remove the particular color of this triangle to expose geometric properties that hold of all triangles. The abstracted claim is true. Galilean idealization is different: assume a frictionless plane, a point mass, or an infinite population. These claims are false — no such things exist. Yet theories built on them make accurate predictions. The philosophical puzzle (why do false assumptions produce true predictions?) only arises for Galilean idealization, not for Aristotelian abstraction."

- question: "A scientific model built on a known false assumption can nonetheless be scientifically legitimate and explanatorily powerful."
  type: true-false
  answer: true
  explanation: "This is the central claim of the idealization literature. Models like the ideal gas (no intermolecular forces), frictionless planes, and infinite populations are known to be false descriptions of reality. Yet they underpin successful theories and explanations. Scientific legitimacy does not require literal truth of model assumptions — it requires that the conclusions drawn from the idealized model accurately describe the target system, either because the idealization is a controlled approximation or because it performs genuine explanatory work as a limiting or null-model case."

- question: "An idealized model that makes accurate predictions must have assumptions that are at least approximately true."
  type: true-false
  answer: false
  explanation: "This is the inference that idealization-in-science refutes. The ideal gas law makes excellent predictions for many real gases at moderate pressures, yet it assumes zero intermolecular forces and zero molecular volume — both strictly and non-negligibly false at high pressures. The success of a prediction does not license reading off the truth of the underlying assumptions. This is related to the problem of 'inference to the best explanation' and the scientific realism debate: predictive success and truth of assumptions come apart when the model is an idealization."

- question: "What is the 'de-idealization problem,' and why do infinite idealizations — like the thermodynamic limit — resist standard de-idealization strategies?"
  type: short-answer
  answer: "The de-idealization problem asks: if a model is known to be false, how do we correct it and show that its conclusions still approximately hold for the real system? For controlled approximations (like point-mass planets), de-idealization works by adding corrections and showing the idealized result is the limiting case as corrections vanish. Infinite idealizations resist this because the explanatory concept (phase transitions, spontaneous symmetry breaking, Hardy-Weinberg equilibrium) only emerges at the infinite limit — in a finite system of any size, the sharp transition or equilibrium does not exist. There is no smooth correction to add; the ideal system is qualitatively different from any finite real system."
  explanation: "This is why infinite idealizations raise harder philosophical questions than ordinary approximations. Real systems are never infinite, yet explanations invoke concepts (thermodynamic phases, critical points) that only exist in the infinite limit. Whether such explanations are genuinely mechanistic or are better understood as structural or mathematical is an active debate in philosophy of science."
```

## Explainer

From your study of **scientific models**, you know that models are not literal descriptions of the world — they are purpose-built representations that highlight some features while ignoring others. The concept of **idealization** sharpens this: many models do not just omit details, they make claims that are *strictly false*. A frictionless plane does not exist. An ideal gas with no intermolecular forces does not exist. An infinite population with perfectly equal reproductive rates does not exist. Yet physics, chemistry, and biology routinely build theories on these fictions, and those theories make accurate predictions. This is the idealization puzzle: how can false assumptions generate true predictions?

One influential distinction is between **Galilean idealization** and **Aristotelian abstraction**. Aristotelian abstraction removes accidental features to reveal a simpler underlying truth — like abstracting from this specific triangle to properties that hold of all triangles. Galilean idealization, by contrast, deliberately introduces *false* assumptions to render systems tractable. Newton's *Principia* assumes that planetary bodies have their mass concentrated at a point; this is false for real planets, but it gives excellent predictions because the deviation from point-mass behavior is negligibly small. The key question is when such false assumptions are *legitimate* — when the conclusions you draw from the idealized model accurately describe the real system despite the false assumption.

The **de-idealization** problem asks: if we know the model is false, how do we correct it? Sometimes the idealization is a controlled approximation — we can add corrections and show that the idealized result is the limit as those corrections vanish. Other times, the idealization plays a deeper explanatory role: the infinite-population assumption in population genetics does not just simplify computation — it *generates* the Hardy-Weinberg equilibrium, which is used as a null model to detect selection in real finite populations. Here the false assumption is doing *explanatory* work, not just computational work.

A philosophically important case is **infinite idealization**: some explanations seem to require taking a system to an infinite limit (infinite population, infinite system size, thermodynamic limit). The puzzle is that real systems are never infinite, yet the explanatory concepts — phase transitions, spontaneous symmetry breaking — only appear at the infinite limit. This raises questions about whether such explanations are truly mechanistic or whether they are something else: structural, mathematical, emergent. Your study of **laws of nature** is relevant here: idealizations often work by identifying a true law governing an idealized system, then arguing that the real system closely approximates the ideal. Understanding when that argument succeeds and when it misleads is a central task in the philosophy of science.
