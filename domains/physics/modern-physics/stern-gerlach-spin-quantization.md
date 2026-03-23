---
id: stern-gerlach-spin-quantization
title: 'Stern-Gerlach Experiment: Spin Quantization and Measurement'
domain: physics
course: modern-physics
prerequisites:
- id: electron-spin-magnetic-moment
  type: hard
- id: measurement-problem-quantum
  type: hard
tags:
- spin
- measurement
- quantum-mechanics
- experimental
stage: advanced
status: validated
---

# Stern-Gerlach Experiment: Spin Quantization and Measurement

## Core Idea
An inhomogeneous magnetic field exerts a force on a magnetic dipole. Atoms with spin experience a force proportional to the z-component of spin, splitting a beam into two: spin-up and spin-down. Cascading Stern-Gerlach devices reveal that spin measurement is projective (a spin-up atom will always show as spin-up in another z-aligned device) and that spin components are incompatible observables (measuring S_x destroys information about S_z).

## How It's Best Learned
Trace particle trajectories through sequential Stern-Gerlach devices with different orientations. Understand that measurement of one component randomizes the others. Quantitatively predict splitting angles and beam intensities.

## Common Misconceptions
Particles do not have pre-existing definite spin states that are merely revealed by measurement (measurement creates the outcome). The two beams have equal intensity only if the initial beam is unpolarized; oriented beams split unequally.

## Questions

```yaml
- question: "A beam of silver atoms passes through a z-aligned Stern-Gerlach device and the spin-up-z output is selected. That beam passes through an x-aligned device and the spin-up-x output is selected. That beam then enters a second z-aligned device. What does the second z-device produce?"
  type: multiple-choice
  options:
    - "100% spin-up-z, because the first device already selected for spin-up-z atoms"
    - "100% spin-down-z, because measuring S_x inverts the z-component"
    - "50% spin-up-z and 50% spin-down-z"
    - "No output, because sequential incompatible measurements cancel each other"
  answer: 2
  explanation: "Measuring S_x on the spin-up-z beam yields 50/50 spin-up-x and spin-down-x, and completely destroys the definite S_z value. The spin-up-x state is an equal superposition of spin-up-z and spin-down-z, so the final z-device gives 50/50. Option A is the classic misconception: treating the first measurement as revealing a pre-existing property that persists through subsequent measurements. S_x and S_z are incompatible observables — having a definite S_x value means maximal uncertainty in S_z."

- question: "What did classical physics predict for the Stern-Gerlach experiment, and what was actually observed?"
  type: multiple-choice
  options:
    - "Classical physics predicted two discrete spots; experiment showed a continuous smear of deflections"
    - "Classical physics predicted a continuous smear; experiment showed exactly two discrete spots"
    - "Classical physics predicted no deflection; experiment showed deflection in a continuous range"
    - "Classical physics predicted four discrete spots; experiment showed only two"
  answer: 1
  explanation: "Classically, a magnetic dipole can point in any direction, so the deflection force should vary continuously — producing a smeared stripe on the detector. Instead, only two discrete spots appeared. This directly demonstrated that the z-component of spin is quantized to exactly two values (±ℏ/2), not a classical continuum. The discreteness was not assumed; it was forced on physics by the experimental result."

- question: "If you take the spin-up output of a z-aligned Stern-Gerlach device and send it through an identical second z-aligned device, 100% of atoms will emerge from the spin-up port."
  type: true-false
  answer: true
  explanation: "This is projective measurement in action. The first device prepares a definite spin-up-z state. A second z-aligned device simply confirms that state — there is no probability of spin-down because the state is already an eigenstate of S_z. This is fundamentally different from measurement revealing a pre-existing classical property: the first measurement prepared the state, and the second confirms it."

- question: "A Stern-Gerlach device always splits an incoming beam into two beams of equal intensity, regardless of how the input beam was prepared."
  type: true-false
  answer: false
  explanation: "Equal intensity (50/50 split) only occurs when the input beam is unpolarized — when atoms have random spin orientations. If the input beam has already been selected for a definite spin direction, the intensities will be unequal. For example, a pure spin-up-z beam sent through a z-device gives 100% spin-up and 0% spin-down. Equal splitting along z only arises for beams in eigenstates of S_x or S_y (or any axis perpendicular to z)."

- question: "Why does the sequential Stern-Gerlach experiment (z → x → z) demonstrate that spin components are incompatible observables, rather than simply showing that the x-measurement physically disturbs a pre-existing spin state?"
  type: short-answer
  answer: "If S_z had a pre-existing definite value that the x-measurement merely disturbs, we might expect most atoms to retain their S_z value with occasional disturbances — not a perfect 50/50 split. But the result is exactly 50/50, which is precisely what quantum mechanics predicts: S_x and S_z do not commute, so an eigenstate of S_x is an equal superposition of S_z eigenstates. This is a structural feature of the algebra of spin operators, not a consequence of imprecision. No matter how gently one imagines performing the x-measurement, the incompatibility is fundamental — it reflects that S_x and S_z cannot simultaneously have definite values, as demanded by the Heisenberg uncertainty principle for non-commuting operators."
  explanation: "The key distinction is between 'measurement disturbs a real value' (classical disturbance) and 'there was no definite value to disturb' (quantum incompatibility). The perfect 50/50 outcome rules out any model where S_z has a hidden pre-existing value that the x-measurement merely scrambles."
```

## Explainer

You already know that an electron has a **magnetic moment** proportional to its spin. In a uniform magnetic field the electron just precesses — nothing dramatic. But when Stern and Gerlach ran a beam of silver atoms through a *non-uniform* magnetic field, the field gradient exerted a net force on each magnetic dipole, bending the trajectory upward or downward depending on the orientation of the moment. The key prediction of classical physics was a continuous smear of deflections, since classically the magnetic moment could point in any direction. What they observed instead was exactly two discrete spots — direct evidence that the z-component of spin takes only two values, +ℏ/2 and −ℏ/2. **Spin quantization** is not a theoretical assumption imposed on the theory; it is an experimental result that demands the theory.

The power of the Stern-Gerlach experiment goes beyond measuring spin. It is also the clearest demonstration of **projective measurement**. If you take the spin-up beam from one z-aligned device and send it into a second z-aligned device, you get 100% spin-up output — no spin-down. The first measurement prepared a definite state, and the second measurement simply confirms it. This is not like sorting balls by color; it is the state itself being created by the measurement act. No pre-existing property is being revealed.

The deeper insight comes from **sequential measurements with rotated devices**. Take the spin-up output of a z-device and send it into an x-aligned device. Now you get 50% spin-up-x and 50% spin-down-x — perfectly random. Take the spin-up-x output and feed it back into a z-device: again 50/50. Measuring S_x has completely randomized S_z. This is not a disturbance from imprecision; it follows from the algebra of spin operators. S_x and S_z do not commute, so they are **incompatible observables** — having a definite value for one implies maximal uncertainty in the other, exactly as the Heisenberg uncertainty principle demands for non-commuting operators.

This incompatibility has a concrete consequence: information about spin is orientation-specific. A beam that is "pure spin-up-z" has zero net S_x polarization, and vice versa. The Stern-Gerlach apparatus acts like a rotatable basis projector, filtering out one component of the quantum state and discarding the rest. Building the intuition that measurement is selection rather than revelation — and that different component measurements are genuinely exclusive — is the conceptual core of understanding spin and, more broadly, quantum measurement theory.
