---
id: h-theorem-irreversibility
title: H-Theorem and Irreversibility
domain: physics
course: statistical-mechanics
prerequisites:
- id: boltzmann-transport-equation
  type: hard
- id: entropy-intro
  type: hard
builds-toward:
- fluctuation-dissipation-theorem
tags:
- irreversibility
- entropy
- boltzmann-equation
stage: expert
status: validated
---

# H-Theorem and Irreversibility

## Core Idea
Boltzmann's H-theorem states that H = ∫ d³r d³v f ln f monotonically decreases (dH/dt ≤ 0) until equilibrium is reached, where dH/dt = 0. This 'explains' the second law of thermodynamics and irreversibility from time-reversible microscopic dynamics via the assumption that collisions are uncorrelated (molecular chaos). The resolution of Loschmidt's paradox requires that initial conditions are non-generic.

## Questions

```yaml
- question: "The molecular chaos assumption (Stosszahlansatz) states that pre-collision velocities are statistically uncorrelated. Why does this assumption break time-reversal symmetry in the H-theorem?"
  type: multiple-choice
  options:
    - "Because the Boltzmann equation itself is time-asymmetric and does not permit time reversal under any conditions"
    - "Because molecular chaos applies to pre-collision pairs but not post-collision pairs — time-reversing the system creates correlated pre-collision velocities, violating the assumption"
    - "Because entropy is automatically larger in the time-reversed state, ensuring H always decreases in both directions"
    - "Because molecular chaos is an empirical regularity that, by definition, only holds in the forward time direction"
  answer: 1
  explanation: "The asymmetry is subtle. Molecular chaos says pre-collision velocities are uncorrelated. After a collision, the two molecules carry correlated velocities (they 'remember' the collision). If you time-reverse the system — reversing all velocities — what were post-collision pairs become pre-collision pairs with correlated velocities. This violates molecular chaos. So the time-reversed trajectory starts from a specially correlated state to which the Stosszahlansatz does not apply, and the H-theorem cannot be applied to it. The assumption treats pre-collision and post-collision correlations differently, and that asymmetry is where the time-reversal breaking enters."

- question: "Loschmidt's paradox points out that for every gas trajectory where H decreases (entropy increases), there exists a time-reversed trajectory. What does the time-reversed trajectory look like, and why is it problematic for the H-theorem?"
  type: multiple-choice
  options:
    - "The time-reversed trajectory also shows H decreasing — so there is no paradox, just confirmation of the theorem"
    - "The time-reversed trajectory shows H increasing — a gas spontaneously evolving from equilibrium toward lower entropy — which appears to contradict the theorem's claim that H always decreases"
    - "The time-reversed trajectory keeps H constant, since the system starts at equilibrium in the reversed direction"
    - "The time-reversed trajectory is physically impossible because velocity reversal cannot be performed in practice"
  answer: 1
  explanation: "This is the core of Loschmidt's paradox. If Newton's laws are time-reversible and the H-theorem says H always decreases, then for every entropy-increasing trajectory there must exist a time-reversed entropy-decreasing one — a gas spontaneously contracting from equilibrium to a low-entropy state. Boltzmann's resolution is that the time-reversed initial state has special correlated velocities that violate molecular chaos, so the theorem doesn't apply to it. Such states exist but are extraordinarily rare; we'd never observe them because the overwhelming majority of initial conditions satisfy molecular chaos."

- question: "The H-theorem requires the molecular chaos assumption in addition to the Boltzmann equation; time-reversible mechanics alone is insufficient to derive entropy increase."
  type: true-false
  answer: true
  explanation: "This is precisely what Loschmidt's paradox establishes. Time-reversible mechanics permits both entropy-increasing and entropy-decreasing trajectories. The H-theorem holds only for initial states satisfying molecular chaos (uncorrelated pre-collision velocities). This assumption carries the time-asymmetric information: it is satisfied by macroscopically prepared states but violated by the special time-reversed states. Irreversibility does not follow from the equations of motion alone — it requires a statistical assumption about the kind of initial conditions we actually prepare and encounter."

- question: "The H-theorem implies that a macroscopic gas can never spontaneously decrease in entropy — such a decrease is absolutely forbidden by the laws of physics."
  type: true-false
  answer: false
  explanation: "The H-theorem is a statistical result, not an absolute prohibition. By Poincaré recurrence, any finite mechanical system will eventually return arbitrarily close to any initial state, including a low-entropy one — because the equations of motion are deterministic and the phase space is bounded. For a macroscopic gas, such a recurrence is not forbidden but takes a time astronomically longer than the age of the universe (~10^(10^23) years). The H-theorem says that for macroscopically prepared states satisfying molecular chaos, entropy decrease is overwhelmingly improbable — not that it is physically impossible."

- question: "How does Boltzmann resolve Loschmidt's paradox — and what does the resolution reveal about the status of the second law of thermodynamics?"
  type: short-answer
  answer: "Boltzmann's resolution is that the H-theorem does not apply to all initial conditions — only those satisfying molecular chaos (uncorrelated pre-collision velocities). The time-reversed entropy-decreasing trajectories Loschmidt points to start from states with special post-collision correlations, which violate this assumption. Such states exist in phase space but are extraordinarily rare: macroscopically prepared systems almost always satisfy molecular chaos, so entropy increase is overwhelmingly probable. This reveals that the second law is not an absolute consequence of mechanics but a statistical claim about the overwhelming probability of entropy increase for the kinds of initial conditions the universe actually presents."
  explanation: "The deeper lesson is that irreversibility is an emergent statistical phenomenon, not a fundamental mechanical law. It requires two ingredients: time-reversible equations of motion plus the statistical assumption that initial conditions are 'generic' (satisfying molecular chaos). The second law holds not because entropy-decreasing trajectories are forbidden by physics, but because they require initial conditions that are infinitely improbable compared to entropy-increasing ones — a fact that ultimately traces back to the universe beginning in an unusually low-entropy state."
```

## Explainer

From your study of the Boltzmann transport equation, you know how it governs the evolution of the phase-space distribution f(r, v, t) through free streaming and collisions. From your study of entropy, you know that the second law demands entropy to increase until equilibrium. Boltzmann's H-theorem makes this connection explicit and raises a profound paradox about time and irreversibility.

Define **H = ∫∫ f ln f d³r d³v** — essentially the negative of entropy: as H decreases, entropy increases. Boltzmann proved that under the Boltzmann equation with the **Stosszahlansatz** (molecular chaos assumption — that the velocities of two molecules about to collide are statistically uncorrelated), dH/dt ≤ 0 always, with equality only at equilibrium when f is a Maxwell-Boltzmann distribution. This appears to derive the second law from kinetic theory: an isolated gas inevitably approaches equilibrium, and H serves as a Lyapunov function guaranteeing convergence. The equilibrium condition dH/dt = 0 also pins down the form of f at equilibrium — exactly the Maxwell-Boltzmann distribution you know from statistical mechanics.

**Loschmidt's paradox** strikes at the heart of this argument. Newton's equations are time-reversible: if you take any trajectory and reverse all velocities at some instant, you get another valid trajectory that runs backward. If there exists a trajectory in which H decreases, then there also exists the time-reversed trajectory in which H increases — apparently contradicting the theorem. Boltzmann's resolution is that the **molecular chaos assumption breaks time-reversal symmetry**. The Stosszahlansatz says pre-collision velocities are uncorrelated; after a collision, the two particles carry correlated velocities. Reversing all velocities creates a state with post-collision correlations (a "special" initial condition), which violates the assumption. The theorem only applies when molecular chaos holds — and the time-reversed state, with its special correlations, violates it.

The deeper lesson is that irreversibility is not derivable from time-reversible mechanics alone. It requires a statistical assumption about initial conditions. The second law is not an absolute statement but a probabilistic one: states that violate it exist but are extraordinarily rare in phase space. A gas will eventually — by Poincaré recurrence — return arbitrarily close to any initial state (even a low-entropy one), but the recurrence time for a macroscopic system is astronomically longer than the age of the universe. The H-theorem establishes that for any macroscopically prepared initial state satisfying molecular chaos, the approach to equilibrium is overwhelmingly likely — which is, ultimately, all the second law claims.
