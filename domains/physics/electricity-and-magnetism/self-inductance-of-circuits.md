---
id: self-inductance-of-circuits
title: Self-Inductance and Energy Storage
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: inductance-and-inductors
  type: hard
- id: faraday-law-of-induction
  type: hard
builds-toward:
- rc-circuits
- lc-and-rlc-circuits
tags:
- inductance
- self-inductance
- EMF
stage: formal-systems
status: validated
---

# Self-Inductance and Energy Storage

## Core Idea
Self-inductance L is the proportionality between current and magnetic flux: Φ = LI. The self-induced EMF is ε = -L(dI/dt), opposing current changes (Lenz's law). Self-inductance depends on circuit geometry: L = μ₀N²A/l for a solenoid. The circuit stores magnetic energy: U = (1/2)LI². Inductors are essential in filters, oscillators, and power supplies.

## How It's Best Learned
Calculate inductance of simple geometries by integrating magnetic flux. Measure self-induced EMF when current changes. Verify energy storage formula from the magnetic field.

## Common Misconceptions
- Self-inductance creates constant opposing force (it is proportional to rate of change of current).
- Self-inductance and inductance in general are identical (self-inductance is one type; mutual inductance is another).
- Inductors store energy 'like batteries' (they store it temporarily in the magnetic field).

## Questions

```yaml
- question: "A circuit contains a large inductor carrying steady current. A switch is suddenly opened, interrupting the current path. What happens immediately after the switch opens?"
  type: multiple-choice
  options:
    - "Current stops instantly because the switch breaks the circuit"
    - "The inductor drives current through whatever path is available, potentially generating a large voltage spike"
    - "The magnetic field immediately collapses with no further effect on the circuit"
    - "The inductor stores extra charge in its windings, which discharges slowly through the switch contacts"
  answer: 1
  explanation: "An inductor resists changes to current — it will generate whatever back-EMF is necessary to maintain that current through any available path. When the switch opens, if no low-resistance path exists, the inductor generates a large voltage spike to push current through the switch gap or any parasitic path. The stored magnetic energy is real and must go somewhere; it does not simply disappear. This is why circuits with large inductors require flyback diodes or snubbers. Option A reflects the naive misconception that a broken circuit instantly stops all current."

- question: "The number of turns in a solenoid is doubled while keeping its length and cross-sectional area the same. What happens to its self-inductance?"
  type: multiple-choice
  options:
    - "It doubles, because twice as many turns means twice the inductance"
    - "It quadruples, because L = μ₀N²A/ℓ and N appears squared"
    - "It stays the same, because the geometry (length and area) is unchanged"
    - "It halves, because the wire is now twice as densely wound and the field concentrates differently"
  answer: 1
  explanation: "L = μ₀N²A/ℓ. Doubling N gives L → μ₀(2N)²A/ℓ = 4μ₀N²A/ℓ — four times the original. The N² dependence means inductance is very sensitive to turns: each turn contributes both more flux and more flux linkage with all other turns. Option A (linear dependence) is the most common error, assuming a simple proportional relationship without noticing the exponent."

- question: "A self-induced EMF resists any current flowing through an inductor, meaning inductors usually oppose current."
  type: true-false
  answer: false
  explanation: "Self-inductance opposes changes in current, not current itself. A steady current flowing through an ideal inductor produces no self-induced EMF at all — dI/dt = 0, so ε = −L(dI/dt) = 0. The inductor only generates a back-EMF when you try to increase or decrease the current. This is the electromagnetic analogue of inertia: a massive object at constant velocity requires no force to maintain it, and an inductor at constant current requires no back-EMF. Confusing 'opposes changes in current' with 'opposes current' is the central misconception."

- question: "The energy stored in an inductor is proportional to the square of the current flowing through it."
  type: true-false
  answer: true
  explanation: "U = (1/2)LI². Doubling the current quadruples the stored energy. This parallels the energy stored in a capacitor (½CV²) and kinetic energy (½mv²) — all quadratic in the relevant 'flow' quantity. The squared dependence means small currents store little energy, but energy grows rapidly with current, which is why high-current inductors in power supplies store significant energy and require careful circuit protection when interrupted."

- question: "In what sense is an inductor the electromagnetic analogue of a massive object, and why does this analogy correctly predict an inductor's behavior when current is interrupted?"
  type: short-answer
  answer: "Both mass and inductance resist changes to their respective flows: mass resists velocity changes (F = m·dv/dt) while inductance resists current changes (ε = L·dI/dt). Just as a massive moving object tends to continue moving and exerts large impulsive forces if abruptly stopped, an inductor carrying current tends to maintain that current and generates large voltage spikes if the current is suddenly interrupted. In both cases, stored energy (½mv² and ½LI²) must be dissipated or transferred — it cannot simply vanish."
  explanation: "The analogy extends to energy storage and the ODE structure: the RLC circuit and the spring-mass system are formally equivalent, with L ↔ m (inertia), R ↔ c (damping), and 1/C ↔ k (restoring force). Understanding inductance as electromagnetic inertia correctly predicts all its behaviors — why it takes time to build current, why it opposes rapid changes, and why interrupting it without a discharge path causes dangerous voltage spikes."
```

## Explainer

You know from Faraday's law that a changing magnetic flux induces an EMF. Now consider what happens inside a circuit carrying changing current: the current itself creates a magnetic field, and as that current changes, the flux through the circuit's own area changes. The result is an EMF induced by the circuit on *itself* — this is **self-inductance**. The self-inductance L is defined by Φ_B = LI: it is the proportionality constant between the current and the total magnetic flux the circuit threads through itself. It depends entirely on geometry — the size, shape, and number of turns of the conductor — not on the current.

The **self-induced EMF** is ε = −L(dI/dt). This is Faraday's law applied to the circuit's own flux. The negative sign means the self-induced EMF *opposes* the current change: if you try to increase the current quickly, the inductor fights back with a back-EMF; if you try to decrease it, the inductor tries to sustain it. This is the electromagnetic analogue of mechanical inertia. A massive object resists changes to its velocity; an inductor resists changes to its current. The inductance L plays the same role as mass m in the analogy F = m(dv/dt) ↔ ε = L(dI/dt).

For a **solenoid** with N turns, cross-sectional area A, and length ℓ, the inductance is L = μ₀N²A/ℓ. This formula shows what geometrically amplifies inductance: more turns (N² dependence — doubling turns quadruples L), larger cross-section (more flux per unit current), and shorter length (fields are more concentrated). Practical inductors — the coiled components in filters, power supplies, and radios — exploit all three.

The energy stored in an inductor is U = (1/2)LI². This is the magnetic analogue of a capacitor's (1/2)CV². When you ramp up current in an inductor, you do work against the back-EMF; that work is stored in the magnetic field filling the inductor's volume. When current is interrupted — say by opening a switch — the inductor does not simply stop. It drives whatever current it can through whatever path is available, sometimes creating dangerous voltage spikes. The energy was real and stored in the field; it must go somewhere. This is why circuits with large inductors require protective flyback diodes or snubbers to dissipate the stored energy safely.
