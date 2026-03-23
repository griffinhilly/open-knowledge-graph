---
id: radiation-from-accelerated-charges
title: Radiation from Accelerated Charges
domain: physics
course: electrodynamics
prerequisites:
- id: lienard-wiechert-potentials
  type: hard
- id: classical-mechanics
  type: soft
builds-toward:
- larmor-formula
- multipole-expansion-radiation
tags:
- radiation
- acceleration
stage: expert
status: validated
---

# Radiation from Accelerated Charges

## Core Idea
Accelerated charges radiate electromagnetic waves. Lienard-Wiechert fields separate into velocity-dependent (near) and acceleration-dependent (far) components. The far field is the radiation field proportional to 1/r, responsible for energy transport.

## Questions

```yaml
- question: "A proton moves in a straight line at constant velocity 0.99c. Does it radiate electromagnetic energy?"
  type: multiple-choice
  options:
    - "Yes — at relativistic speed its fields become highly concentrated, releasing radiation"
    - "No — only acceleration produces radiation; constant velocity, regardless of speed, produces no radiation field"
    - "Yes — the velocity field increases as the proton approaches an observer, so energy is radiated"
    - "No — but only because 0.99c is below the threshold at which radiation begins"
  answer: 1
  explanation: "Radiation is caused by acceleration, not velocity. A charge in uniform motion — even at 0.99c — has only a velocity field that falls as 1/r² and carries no net energy to infinity. The radiation field ∝ 1/r only appears when the charge accelerates. This is why synchrotron radiation requires bending magnets (which accelerate electrons centripetally) rather than just high speed alone. There is no velocity threshold — the dividing line is zero versus nonzero acceleration."

- question: "A non-relativistic electron undergoes simple harmonic motion. At the moment of maximum displacement (momentarily at rest), does it radiate?"
  type: multiple-choice
  options:
    - "No — it is at rest, so it behaves like a stationary charge and produces no radiation"
    - "Yes — at maximum displacement the restoring force (and thus acceleration) is largest, so it radiates most strongly"
    - "Yes — but only because the radiation is a delayed effect of its prior motion"
    - "No — it only radiates when it is moving, so radiation is maximum at the equilibrium position"
  answer: 1
  explanation: "Radiation depends on acceleration, not velocity. At maximum displacement in SHM, velocity is zero but acceleration is maximum (the restoring force F = −kx is largest there). Since radiation power is proportional to acceleration squared, maximum displacement is the moment of peak radiation. At the equilibrium position, velocity is maximum but acceleration is zero — no radiation at that instant. This perfectly illustrates why acceleration, not speed, is the operative quantity."

- question: "The near (velocity) field of a moving charge also decreases as 1/r and therefore carries a finite amount of energy to infinity."
  type: true-false
  answer: false
  explanation: "The near field decreases as 1/r², not 1/r. The Poynting vector (energy flux) is proportional to E × B, so for the near field it goes as 1/r⁴. Integrating over a sphere of radius r gives power ∝ r² × (1/r⁴) = 1/r² → 0 as r → ∞. The near field carries zero net energy to infinity — it's reactive energy oscillating near the charge. Only the radiation field, with 1/r dependence, produces a Poynting vector ∝ 1/r² that integrates to a constant nonzero power over any sphere."

- question: "At relativistic speeds, radiation from an accelerated charge is distributed uniformly in all directions, just as in the non-relativistic case."
  type: true-false
  answer: false
  explanation: "In the non-relativistic case, radiation follows a sin²θ pattern (a donut around the acceleration axis). At relativistic speeds, the radiation is concentrated strongly in the forward direction — relativistic beaming. This is why synchrotron light sources produce tightly collimated beams: relativistic electrons emit radiation mostly forward along their direction of motion. The beaming effect intensifies with increasing speed and is a direct consequence of the relativistic Liénard-Wiechert fields."

- question: "Explain why the 1/r dependence of the radiation field, as opposed to the 1/r² dependence of the near field, is physically significant for energy transport."
  type: short-answer
  answer: "Energy flux (Poynting vector) is proportional to E × B. For a field component going as 1/r, the Poynting vector goes as 1/r². Integrating over a spherical surface of radius r gives total power ∝ r² × (1/r²) = constant, independent of r. Energy flows outward at the same rate through any sphere, no matter how large — it escapes to infinity permanently. For the near field (1/r²), the Poynting vector goes as 1/r⁴, integrating to 1/r² → 0 as r → ∞. Near-field energy never escapes; it oscillates reactively near the charge."
  explanation: "This is the precise reason why acceleration is necessary for radiation: only the acceleration-dependent 1/r field produces an outward energy flux that doesn't vanish at large distances. The near field is energy that's 'borrowed' from and returned to the source — never permanently radiated away."
```

## Explainer

From the Liénard-Wiechert potentials, you can compute the exact electric and magnetic fields of a moving point charge — at any position, at any instant, accounting for the fact that the fields propagate at c rather than instantaneously. When you do this for a charge in arbitrary motion, the resulting field splits into two qualitatively different pieces. The **velocity field** (or near field) looks like a distorted Coulomb field: it points from the charge's *current* position (corrected for retardation), falls off as 1/r², and carries no net energy to infinity. The **acceleration field** (or far field or radiation field) is proportional to the acceleration, falls off as 1/r, and is the one responsible for electromagnetic radiation.

Why does 1/r matter so much? The energy flux (Poynting vector) is proportional to E × B, and both radiation field components go as 1/r, so the Poynting vector goes as 1/r². Integrating over a sphere of radius r gives a total power proportional to r² × (1/r²) = constant — the same regardless of how large a sphere you choose. Energy flows outward and never comes back. By contrast, the near-field Poynting vector goes as 1/r⁴ after integration, and the total power it would carry through a large sphere vanishes — it's just reactive, oscillating energy that stays near the charge. **Radiation requires acceleration** precisely because only the acceleration field has the 1/r dependence needed to carry energy to infinity.

The physical picture is illuminating. Imagine a charge at rest: its field lines extend radially outward to infinity. Now suddenly accelerate the charge briefly. The field lines close to the charge quickly learn about the motion and update their configuration, but far-away field lines can't know yet — information travels at c. The result is a "kink" in the field lines at the shell where the disturbance has propagated. This kink is the radiation field, and it propagates outward at c as a genuine electromagnetic wave. The size of the kink — the amplitude of the radiation field — is proportional to the magnitude of the acceleration and to sin θ (the angle from the acceleration axis), giving the characteristic donut-shaped radiation pattern.

The generalization to relativistic motion involves the Liénard-Wiechert fields in their full relativistic form, with relativistic corrections that dramatically concentrate the radiation in the forward direction at high speeds (**relativistic beaming**). This is why synchrotron light sources produce intensely collimated beams: relativistic electrons emit radiation mostly in the direction they're moving, rather than the broad donut pattern of the non-relativistic limit. But whether non-relativistic or relativistic, the fundamental principle is the same — acceleration is the engine of electromagnetic radiation, and the 1/r decay of the far field is what allows energy to escape to infinity.
