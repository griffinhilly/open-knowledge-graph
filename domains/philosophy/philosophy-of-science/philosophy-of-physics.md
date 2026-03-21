---
id: philosophy-of-physics
title: Philosophy of Physics
domain: philosophy
course: philosophy-of-science
prerequisites:
- id: philosophy-of-science-intro
  type: hard
builds-toward:
- philosophy-of-neuroscience
tags:
- physics
- space-time
- quantum
- relativity
stage: advanced
status: draft
---

# Philosophy of Physics

## Core Idea
Physics raises fundamental philosophical questions about the nature of space, time, causality, and reality. Quantum mechanics poses interpretive challenges about wave function, measurement, locality, and entanglement. Relativity transforms understanding of space and time: are they fundamental or emergent? Do all moments exist equally (eternalism) or is the present special (presentism)? Thermodynamics raises questions about time's asymmetry. Philosophy of physics illustrates how scientific discoveries drive philosophical inquiry.

## Questions

```yaml
- question: "Bell's theorem, together with experimental results, rules out which class of theories?"
  type: multiple-choice
  options:
    - "Theories in which the wave function collapses during measurement"
    - "Theories in which quantum particles have definite states before measurement (local hidden-variable theories)"
    - "Theories in which the speed of light is the maximum speed of information transfer"
    - "Theories that deny the existence of quantum entanglement"
  answer: 1
  explanation: "Bell's theorem proves mathematically that no local hidden-variable theory can reproduce all the statistical predictions of quantum mechanics. A local hidden-variable theory would say: particles have definite but unknown properties before measurement, and no influence travels faster than light. Experiments (Aspect et al., and subsequent loophole-free tests) have confirmed the quantum predictions and violated Bell's inequalities, ruling out this entire class of theories. This forces a choice: accept nonlocality, accept many worlds, or accept that quantum mechanics doesn't describe a single definite reality."

- question: "The second law of thermodynamics (entropy increases toward the future) is philosophically puzzling because:"
  type: multiple-choice
  options:
    - "It contradicts quantum mechanics, which says entropy is always conserved"
    - "The fundamental laws of physics are nearly time-symmetric, so the asymmetry of entropy increase needs a separate explanation"
    - "Entropy is only a statistical concept and cannot apply to individual particles"
    - "It implies the universe will eventually reach a state of maximum order"
  answer: 1
  explanation: "The fundamental equations of physics (Newton's laws, quantum mechanics, electromagnetism) are nearly time-symmetric — run particle collisions backward and they still obey the laws. Yet heat flows in only one direction, eggs break but don't reassemble, and entropy increases toward the future but not the past. This irreversibility cannot be derived from time-symmetric fundamental laws alone — it requires positing a special low-entropy initial condition for the universe. Why the universe started in such an unusual state is a deep philosophical and cosmological puzzle, not resolved by the physics itself."

- question: "Special relativity's relativity of simultaneity creates a genuine tension with the philosophical position called presentism."
  type: true-false
  answer: true
  explanation: "Presentism holds that only the present moment exists — past and future are not real. But special relativity shows that which events count as 'simultaneous' (and hence 'present') depends on the observer's reference frame. Two events that are simultaneous for one observer are non-simultaneous for another in relative motion. If the present is frame-relative, there is no observer-independent 'now' that could define what exists. This makes it very difficult to maintain that 'the present' picks out a unique, real slice of reality, as presentism requires."

- question: "The Copenhagen interpretation of quantum mechanics holds that the wave function gives a complete description of quantum reality, and measurement causes a physical collapse of the wave function."
  type: true-false
  answer: false
  explanation: "Copenhagen is often mischaracterized this way. The standard Copenhagen interpretation is notably quiet about what the wave function represents physically — it treats the wave function as a calculational tool for predicting measurement outcomes, not as a literal description of physical reality. It also avoids specifying what triggers 'collapse' or what happens between measurements. This instrumentalism is part of why Copenhagen avoids committing to a picture of quantum reality, and why many physicists and philosophers find it philosophically unsatisfying despite its predictive success."

- question: "Why does the measurement problem in quantum mechanics count as a genuinely philosophical problem, and not just an unsolved physics problem awaiting a technical fix?"
  type: short-answer
  answer: "The measurement problem is philosophical because different solutions (Copenhagen, many-worlds, pilot-wave, collapse theories) are not distinguishable by experiment — they all reproduce the same quantum predictions. The disagreement is about what the wave function represents and what reality is like between measurements. These are questions about interpretation and ontology, not just about finding a better equation. A purely technical fix would be a new physical law; the measurement problem requires deciding what quantum mechanics says about reality, which is a philosophical question."
  explanation: "Physics tells us the Schrödinger equation evolves the wave function deterministically, but measurement seems to select one outcome from a superposition. Whether this 'collapse' is a real physical process, an illusion created by branching worlds, or something else entirely cannot be resolved by doing more experiments — all interpretations agree on the predictions. This is the hallmark of a philosophical rather than empirical dispute: the evidence underdetermines which picture of reality is correct."
```

## Explainer

Your foundation in philosophy of science prepared you to ask not just what science discovers, but what those discoveries mean. Philosophy of physics takes this question to its deepest level: the theories of physics that best describe nature — quantum mechanics and relativity — turn out to resist straightforward interpretation. Understanding them mathematically is one thing; understanding what they *say about reality* is another, and that second task is irreducibly philosophical.

**Quantum mechanics** is the most precisely tested theory in history, yet there is no consensus on what it describes. The **wave function** evolves deterministically according to the Schrödinger equation — but when we observe a quantum system, we seem to get a definite outcome rather than a superposition. The *Copenhagen interpretation* treats measurement as a special process that collapses the wave function, but refuses to say what the wave function represents physically. The *many-worlds interpretation* denies collapse: all outcomes occur, but in branching branches of a universal wave function. The measurement problem — why do we observe definite outcomes if the universe is just a wave function? — remains genuinely open. Add **entanglement** — where measuring one particle instantly constrains what you will find measuring a distant partner — and Bell's theorem, which proves no local hidden-variable theory can reproduce quantum predictions, and you have a theory that forces choice among deeply different metaphysics.

**Relativity** transforms the philosophy of space and time just as dramatically. Special relativity unifies space and time into a single four-dimensional **spacetime**: what counts as "simultaneous" depends on one's frame of reference, and there is no absolute present moment. This supports *eternalism* (or the "block universe" view): past, present, and future moments are equally real, just located at different coordinates in spacetime, as different places are spatially real without us being *there*. The rival view, *presentism*, insists only the present moment exists — but special relativity makes the present frame-relative, creating serious tension. General relativity goes further, treating gravity as spacetime curvature and making spacetime itself dynamic.

**Thermodynamics** raises a different puzzle: the *arrow of time*. The fundamental laws of physics are (nearly) time-symmetric — run a film of particle collisions backward and it still obeys the laws. Yet heat flows from hot to cold, entropy increases, and broken eggs do not reassemble. This irreversibility emerges from statistical mechanics and the **second law of thermodynamics**, which describes macroscopic phenomena. Why does entropy increase toward the future and not the past? The answer seems to require a special low-entropy initial condition of the universe — an unexplained brute fact, or a cosmological problem, or perhaps an anthropic selection effect. Philosophy of physics shows that the most precise scientific theories press hardest on the most fundamental philosophical questions.
