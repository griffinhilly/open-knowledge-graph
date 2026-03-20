---
id: bell-theorem
title: Bell's Theorem and Nonlocality
domain: physics
course: quantum-mechanics
prerequisites:
- id: quantum-entanglement
  type: hard
builds-toward:
- bell-inequalities
tags:
- bell-theorem
- nonlocality
stage: formal-systems
status: draft
---

# Bell's Theorem and Nonlocality

## Core Idea
Bell's theorem proves no local hidden-variable theory reproduces all quantum predictions. Bell inequalities bound classical correlations; entangled states violate these bounds.

## Explainer

From your study of quantum entanglement, you know that two particles can be prepared in a joint state where neither particle has a definite spin until measured, yet measurements on the two particles are correlated in a way that cannot be explained by anything each particle carries locally. The natural skeptical response — Einstein's response — was to suppose this apparent mystery is resolved by **hidden variables**: perhaps each particle secretly carries a pre-determined spin value that we just don't know. Bell's theorem is a mathematical proof that this escape route is closed.

The argument works by considering what correlations between measurements on two distant particles would have to look like if the particles each carried local hidden variables. Bell derived an inequality — a bound on how correlated the results could possibly be — that any local hidden-variable theory must satisfy. The inequality is not a quantum-mechanical result; it is a purely classical, probabilistic constraint that follows just from the assumption that the two particles' behaviors are determined locally, without any influence traveling between them faster than light. The bound is tight: it applies to all local realistic theories, regardless of what the hidden variables actually are.

**Bell's insight** was to choose three or four detector angle settings instead of two. With just two settings, local hidden variables and quantum mechanics happen to agree. With three angles, the predictions diverge. Quantum mechanics predicts that certain angle combinations produce correlations stronger than any local model permits. The specific inequality most often used in experiments, the CHSH inequality, states that a quantity S formed from four correlation measurements satisfies |S| ≤ 2 for any local hidden-variable theory. Quantum mechanics predicts |S| = 2√2 ≈ 2.83 for the optimal entangled state and measurement settings.

Experiments — beginning with Aspect's 1982 tests and culminating in loophole-free Bell tests around 2015 — consistently violate the CHSH inequality and match the quantum prediction. This means that nature is genuinely **nonlocal** in the following precise sense: the correlations between distant entangled particles cannot be reproduced by any theory where each particle carries only local information. What it does not mean is that you can use this nonlocality to send signals faster than light — the individual outcomes on each side remain individually random. The nonlocality only appears when you bring the two sets of results together and compare them. Bell's theorem thus tells us something deep: the world is not locally real, and we must give up at least one of those words.
