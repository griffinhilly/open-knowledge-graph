---
id: path-integral-formulation
title: Path Integral Formulation of Quantum Mechanics
domain: physics
course: quantum-mechanics
prerequisites:
- id: schrodinger-equation-intro
  type: hard
tags:
- path-integrals
- feynman
stage: expert
status: validated
---

# Path Integral Formulation of Quantum Mechanics

## Core Idea
The amplitude for propagation from (x₀,t₀) to (xf,tf) sums over all paths: K = ∫ D[x(t)] e^{iS[x]/ℏ}, where S[x] = ∫ L dt is the action. Classical paths dominate (stationary phase); quantum fluctuations come from all paths. Equivalent to Schrödinger equation and elegant for transitions and semiclassics.

## Questions

```yaml
- question: "In the Feynman path integral, paths far from the classical trajectory contribute negligibly to the quantum amplitude. The correct reason for this is:"
  type: multiple-choice
  options:
    - "The action S is larger for non-classical paths, so e^{iS/ℏ} has smaller magnitude"
    - "Non-classical paths are physically forbidden by the equations of motion"
    - "Neighboring non-classical paths have rapidly varying phases e^{iS/ℏ} that cancel via destructive interference"
    - "The path integral assigns zero weight to paths that violate energy conservation"
  answer: 2
  explanation: "Every path has the SAME magnitude of contribution — |e^{iS/ℏ}| = 1 always, since e^{iS/ℏ} is a pure phase. No path has larger or smaller magnitude; what differs is the phase direction. Near the classical path, δS/δx(t) = 0 (stationary action), so neighboring paths have nearly the same phase — they interfere constructively. Far from the classical path, the action changes rapidly between neighboring paths, phases point in all directions, and they cancel by destructive interference. Option A is the most common misconception — confusing phase cancellation with amplitude suppression."

- question: "What determines the phase contributed by each path in the Feynman path integral?"
  type: multiple-choice
  options:
    - "The energy of the particle along that path, divided by ℏ"
    - "The classical action S[x] = ∫ L dt along that path, divided by ℏ"
    - "The time duration of the path multiplied by the particle's mass"
    - "Whether the path satisfies the Schrödinger equation at each point"
  answer: 1
  explanation: "Each path x(t) contributes amplitude e^{iS[x]/ℏ}, where S[x] = ∫ L dt is the classical action — the time integral of the Lagrangian L = T − V. All paths have equal magnitude (1); only their phases differ. The phase is S/ℏ, which is dimensionless (both S and ℏ have units of energy × time). The Lagrangian and action are exactly the quantities from Hamilton's principle of least action in classical mechanics — the same quantity that selects the classical path. The path integral is constructed so that the classical path emerges naturally from constructive interference of phases near δS = 0."

- question: "In the limit ℏ → 0, the Feynman path integral is dominated by the classical path — the path where the action is stationary — which is why classical mechanics emerges as the limit of quantum mechanics."
  type: true-false
  answer: true
  explanation: "As ℏ → 0, the phase e^{iS/ℏ} oscillates infinitely rapidly for any path where S is not exactly stationary. Only paths in a vanishingly small neighborhood of the classical path (where δS ≈ 0 and phase is nearly constant) contribute — all others cancel. The classical path is the path of stationary action (Hamilton's principle: δS = 0), equivalent to Newton's equations. Quantum mechanics does not contradict classical mechanics: classical trajectories are what remain after all quantum interference has resolved. The same mechanism operates in optics: geometric optics (light rays) is the ℏ → 0 analogue — rays are paths of stationary phase in the wave description."

- question: "In the path integral, the classical trajectory is assigned a larger amplitude magnitude than other paths, which is why it dominates."
  type: true-false
  answer: false
  explanation: "This is the central misconception about the path integral. Every path has exactly the same amplitude magnitude: |e^{iS/ℏ}| = 1, since the exponential of an imaginary number lies on the unit circle. The classical path does NOT have larger magnitude. What makes it dominate is constructive interference: near the classical path, the action is stationary (δS = 0), so nearby paths have nearly the same phase direction and add together. Away from the classical path, the action varies rapidly between neighbors, phase directions randomize, and they cancel. The dominance of the classical path is a collective interference effect, not a property of any individual path."

- question: "Why does the path integral formulation make the emergence of classical mechanics from quantum mechanics more transparent than the Schrödinger equation does? What is the key correspondence?"
  type: short-answer
  answer: "In the Schrödinger equation, classical mechanics appears only in the limit through Ehrenfest's theorem or WKB approximation — the connection requires work to see. In the path integral, the correspondence is immediate: the classical path is where the action S is stationary (δS = 0), which is exactly Hamilton's principle — the variational principle that defines classical trajectories. As ℏ → 0, phases e^{iS/ℏ} oscillate faster for non-classical paths and destructive interference eliminates them, leaving only the classical trajectory. The quantum particle explores all paths, but only near the classical path do contributions reinforce. Classical mechanics is the stationary-phase approximation to quantum mechanics — the path integral makes this explicit through the same mathematics that relates geometric optics to wave optics."
  explanation: "The path integral is the natural language for the quantum-classical correspondence because it starts with the classical Lagrangian and action — the quantities that define classical trajectories — and adds quantum mechanics by summing over all paths with phase e^{iS/ℏ}. The classical limit is a direct mathematical statement (stationary phase), not a separate approximation scheme. This transparency is one reason the path integral is especially useful in quantum field theory."
```

## Explainer

The Schrödinger equation gives you one complete picture of quantum mechanics: the wavefunction evolves in time deterministically, and you extract probabilities from it. Feynman's **path integral formulation** gives you a completely different but equivalent picture — one that makes the connection to classical mechanics vivid and almost tactile. The central idea is this: to find the quantum amplitude for a particle to travel from point x₀ at time t₀ to point xf at time tf, you sum a phase contribution from every conceivable path connecting those endpoints. Not just the classical path. Every path.

Each path x(t) contributes an amplitude with magnitude 1 and phase equal to the classical **action** S[x] = ∫ L dt divided by ℏ: the contribution is e^{iS[x]/ℏ}. The **action** is the time integral of the Lagrangian L = T − V — the quantity you studied in classical mechanics via Hamilton's principle. For familiar classical systems, S has units of energy × time, same as ℏ. The ratio S/ℏ is therefore dimensionless, and e^{iS/ℏ} is a pure phase on the unit circle in the complex plane.

The deep insight is what happens when you add up all these phases. For most paths, neighboring paths have wildly different phases that cancel when summed — **destructive interference** washes out their contributions. But near the **classical path** — the one that satisfies Hamilton's principle and makes S stationary (δS = 0) — neighboring paths have nearly identical phases. They add constructively. In the limit ℏ → 0, only the classical path survives. Quantum mechanics thus contains classical mechanics as a limit: classical trajectories are the paths of stationary phase, exactly as light rays are the paths of stationary phase in geometric optics. The particle doesn't "choose" the classical path — the classical path is what remains after all quantum interference has occurred.

For paths far from the classical trajectory, the action varies rapidly and the phases cancel. But nearby quantum fluctuations do survive, and their magnitude is governed by ℏ. This is what makes the path integral naturally suited to **semiclassical approximations**: expand around the classical path, treat fluctuations perturbatively, and you get systematic quantum corrections to classical results. The same framework that makes WKB transparent also makes the path integral the natural language for quantum field theory, where the "paths" become field configurations over all spacetime, and the action integral becomes the foundation for Feynman diagrams and perturbation theory.
