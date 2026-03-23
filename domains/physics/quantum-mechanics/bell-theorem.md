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
stage: advanced
status: draft
---

# Bell's Theorem and Nonlocality

## Core Idea
Bell's theorem proves no local hidden-variable theory reproduces all quantum predictions. Bell inequalities bound classical correlations; entangled states violate these bounds.

## Questions

```yaml
- question: "Before Bell's theorem, Einstein proposed that entanglement correlations could be explained by local hidden variables — pre-set properties each particle carries. Bell's theorem rules this out. What does it actually prove?"
  type: multiple-choice
  options:
    - "It proves that quantum mechanics is fundamentally incomplete and must be replaced"
    - "It proves that no theory of any kind — local or nonlocal — can reproduce quantum predictions"
    - "It proves that no local hidden-variable theory can reproduce all the statistical predictions of quantum mechanics"
    - "It proves that faster-than-light signaling between particles must be occurring in entangled systems"
  answer: 2
  explanation: "Bell's theorem is specifically about *local* hidden-variable theories — theories where each particle carries pre-determined information that travels with it and is not influenced by what happens at the distant detector. The theorem proves that no such theory can match all quantum predictions. It does NOT rule out nonlocal hidden-variable theories (Bohmian mechanics, for instance, is a hidden-variable theory that is nonlocal and does reproduce quantum predictions). It also does not imply faster-than-light signaling — individual outcomes remain random, and nonlocality only appears in correlations when results are compared after the fact."

- question: "The CHSH inequality states that |S| ≤ 2 for any local hidden-variable theory. Quantum mechanics predicts |S| = 2√2 ≈ 2.83 for optimal measurements. What is the significance of this gap?"
  type: multiple-choice
  options:
    - "It shows that quantum mechanics computes correlations incorrectly and needs a correction factor"
    - "It provides a testable numerical prediction: if experiments measure |S| > 2, local hidden variables are ruled out by the data"
    - "It shows that the inequality is too weak to distinguish quantum from classical predictions in real experiments"
    - "It proves that hidden variables exist but are fundamentally undetectable"
  answer: 1
  explanation: "The gap between 2 and 2√2 is the empirical handle on a metaphysical question. By constructing the CHSH quantity S from actual measurement statistics, experimenters can test whether nature respects the local hidden-variable bound. Experiments from Aspect (1982) to loophole-free tests (2015) consistently find |S| > 2, matching the quantum prediction. The numerical gap is what makes Bell's theorem experimentally testable rather than merely philosophical — it translates a question about the nature of reality into a measurable number."

- question: "Bell's theorem shows that quantum entanglement produces correlations that cannot be explained by any local realistic mechanism — that is, the particles cannot simply be 'pre-programmed' with answers that they carry to their respective detectors."
  type: true-false
  answer: true
  explanation: "This is precisely what Bell's theorem proves. If each particle secretly carried predetermined spin values (like colored balls in boxes — one red, one blue — determined before separation), then the correlations between measurements would be bounded by the Bell inequality. Experiments violate this bound, demonstrating that the correlations arise from a mechanism that cannot be explained locally. The particles do not carry pre-existing definite values that they simply reveal upon measurement — the quantum state is genuinely indeterminate until measured, and the correlations reflect this in a way that exceeds any local explanation."

- question: "Bell's theorem proves that quantum nonlocality allows information to be transmitted faster than light between entangled particles."
  type: true-false
  answer: false
  explanation: "Bell nonlocality does NOT enable faster-than-light communication. When Alice measures her particle, Bob's measurement outcome on his particle remains individually random — he sees a sequence of 0s and 1s with no pattern he can decode. The nonlocal correlation only appears when Alice and Bob later compare their results over a classical channel. Neither party can control what outcome they get, so neither can encode a message in their outcomes. The correlations are 'spooky' but not exploitable for signaling. Bell's theorem tells us the world is not locally real, but it is still consistent with no-faster-than-light signaling (relativistic causality)."

- question: "What was Einstein's hidden-variable intuition, and what specific feature of Bell's experimental design — using three or more measurement angles rather than two — makes it possible to rule out that intuition?"
  type: short-answer
  answer: "Einstein believed that entangled particles' correlated outcomes could be explained by shared pre-existing properties (hidden variables) set at the moment of entanglement — like two gloves separated into different boxes, where finding one left-handed instantly tells you the other is right-handed, with no mystery. With only two measurement angles, local hidden variables and quantum mechanics happen to agree on the predicted correlations. Bell's insight was to use three or four angles: at certain angle combinations, quantum mechanics predicts correlations stronger than any local pre-programming strategy can produce. The CHSH inequality bounds what any local model can achieve across four angle settings, and quantum mechanics exceeds that bound with the right entangled state."
  explanation: "The genius of Bell's theorem is translating a philosophical disagreement into a mathematical inequality that can be tested. Two angles are insufficient because both theories agree there; the disagreement only emerges with more angles, where the geometry of quantum predictions cannot be mimicked by any local classical model regardless of how clever the hidden variables are."
```

## Explainer

From your study of quantum entanglement, you know that two particles can be prepared in a joint state where neither particle has a definite spin until measured, yet measurements on the two particles are correlated in a way that cannot be explained by anything each particle carries locally. The natural skeptical response — Einstein's response — was to suppose this apparent mystery is resolved by **hidden variables**: perhaps each particle secretly carries a pre-determined spin value that we just don't know. Bell's theorem is a mathematical proof that this escape route is closed.

The argument works by considering what correlations between measurements on two distant particles would have to look like if the particles each carried local hidden variables. Bell derived an inequality — a bound on how correlated the results could possibly be — that any local hidden-variable theory must satisfy. The inequality is not a quantum-mechanical result; it is a purely classical, probabilistic constraint that follows just from the assumption that the two particles' behaviors are determined locally, without any influence traveling between them faster than light. The bound is tight: it applies to all local realistic theories, regardless of what the hidden variables actually are.

**Bell's insight** was to choose three or four detector angle settings instead of two. With just two settings, local hidden variables and quantum mechanics happen to agree. With three angles, the predictions diverge. Quantum mechanics predicts that certain angle combinations produce correlations stronger than any local model permits. The specific inequality most often used in experiments, the CHSH inequality, states that a quantity S formed from four correlation measurements satisfies |S| ≤ 2 for any local hidden-variable theory. Quantum mechanics predicts |S| = 2√2 ≈ 2.83 for the optimal entangled state and measurement settings.

Experiments — beginning with Aspect's 1982 tests and culminating in loophole-free Bell tests around 2015 — consistently violate the CHSH inequality and match the quantum prediction. This means that nature is genuinely **nonlocal** in the following precise sense: the correlations between distant entangled particles cannot be reproduced by any theory where each particle carries only local information. What it does not mean is that you can use this nonlocality to send signals faster than light — the individual outcomes on each side remain individually random. The nonlocality only appears when you bring the two sets of results together and compare them. Bell's theorem thus tells us something deep: the world is not locally real, and we must give up at least one of those words.
