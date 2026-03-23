---
id: capacitance-definition
title: Capacitance and Capacitors
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: potential-energy-systems
  type: hard
- id: conductors-electrostatic-behavior
  type: hard
builds-toward:
- parallel-plate-capacitor-formula
- capacitor-circuits-series-parallel
tags:
- capacitance
- device
- charge-voltage
stage: formal-systems
status: validated
---

# Capacitance and Capacitors

## Core Idea
Capacitance C is defined as C = Q/V, where Q is magnitude of charge on each plate and V is potential difference. Capacitance depends only on geometry and material; higher capacitance means more charge storage for given voltage.

## Questions

```yaml
- question: "A capacitor is charged until it holds charge Q at voltage V. You then connect a second identical capacitor in parallel, doubling the total charge stored. What happens to the capacitance of the original capacitor?"
  type: multiple-choice
  options:
    - "It doubles, because twice as much charge is now stored"
    - "It remains unchanged — capacitance is a fixed geometric property of the device, not a function of charge or voltage"
    - "It halves, because the charge is now split between two capacitors"
    - "It increases slightly because the stronger electric field changes the plate geometry"
  answer: 1
  explanation: "Capacitance is determined solely by geometry (plate area, separation) and the dielectric material — it is an intrinsic property of the device, not its electrical state. Adding a second capacitor in parallel changes the circuit's total capacitance, not the individual capacitor's capacitance. Doubling Q would double V proportionally, leaving C = Q/V unchanged. Option A reflects the common misconception that 'more charge = higher capacitance.'"

- question: "For a parallel-plate capacitor, why does decreasing the plate separation d increase the capacitance?"
  type: multiple-choice
  options:
    - "Closer plates allow more charge to spread uniformly across the surface area"
    - "A smaller gap reduces the electric field between the plates, enabling more charge storage"
    - "The same charge Q produces a smaller potential difference V = Ed when d is smaller, so C = Q/V increases"
    - "Reducing d increases the dielectric constant of the material between the plates"
  answer: 2
  explanation: "For parallel plates, V = Ed = Qd/(ε₀A). Smaller d means smaller V for the same Q, so the ratio C = Q/V = ε₀A/d increases. Option B gets the field direction of reasoning wrong — the field E = Q/(ε₀A) doesn't depend on d at all for an ideal parallel-plate capacitor. The effect is entirely through the potential difference, which drops with d."

- question: "The energy stored in a capacitor is ½CV² rather than CV² because charge is deposited incrementally against an increasing voltage — starting from zero and building to the final value."
  type: true-false
  answer: true
  explanation: "When charging a capacitor, the first increment of charge dQ is deposited at near-zero voltage (nearly free). Subsequent increments are deposited against increasing voltage. Integrating dU = V dQ = (Q/C) dQ from 0 to Q gives U = Q²/(2C) = ½CV². The factor of ½ reflects the average voltage over the charging process, not the final voltage. A common error is multiplying full charge by full voltage, which gives QV = CV², double the actual energy."

- question: "Capacitance increases when more charge is stored on a capacitor, since C = Q/V and Q appears in the numerator."
  type: true-false
  answer: false
  explanation: "Although Q appears in the numerator of C = Q/V, storing more charge also increases V proportionally — the ratio remains constant. Capacitance is a fixed property determined by geometry and material, not by the charge state. The equation C = Q/V defines capacitance as an invariant ratio, analogous to how resistance R = V/I is a fixed property of a resistor regardless of which particular V and I are flowing through it."

- question: "Why is it more accurate to describe capacitance as a property of the device's geometry rather than a property of the charge stored on it?"
  type: short-answer
  answer: "Because changing the stored charge does not change the capacitance — it changes both Q and V in the same proportion, leaving their ratio C = Q/V fixed. The geometry (plate area A, separation d, dielectric ε) fully determines C = εA/d regardless of the electrical state. This invariance is what makes capacitance a useful circuit parameter: it tells you something stable about the device's charge-storing ability, not something that fluctuates with use. Just as a resistor's resistance doesn't change when different voltages are applied, a capacitor's capacitance doesn't change when different charges are stored."
  explanation: "This analogy to resistance helps clarify the concept: R = V/I is a property of a resistor's dimensions and material (like Ohm's law), not of the specific V or I at any moment. Similarly, C = Q/V is a property of the capacitor's dimensions and material, not of its current charge state."
```

## Explainer

Recall from your study of conductors that when charge is placed on an isolated conductor, it redistributes until the surface is an equipotential. A capacitor exploits this property deliberately: two conductors placed close together, carrying equal and opposite charges, create a well-defined electric field in the gap between them — and therefore a well-defined potential difference. **Capacitance** is simply the ratio of how much charge you stored to how much voltage it cost you: C = Q/V. A larger capacitance means you get more charge per volt — the device is better at storing charge.

What determines capacitance? Purely geometry (and the material between the plates). Consider two parallel plates of area A separated by distance d. The electric field between them is E = σ/ε₀ = Q/(ε₀A), and the potential difference is V = Ed = Qd/(ε₀A). So C = Q/V = ε₀A/d. This result is telling: bigger plates (more area) increase C because more charge can spread out; smaller gap (less distance) increases C because the same charge creates less voltage drop. Neither the charge Q nor the voltage V appears — capacitance is a purely geometric property, like resistance is a property of a resistor's dimensions.

The connection to potential energy — your prerequisite — is direct. You know that assembling a charge distribution requires work, which is stored as potential energy. For a capacitor, the energy stored is U = ½QV = ½CV² = Q²/(2C). The factor of ½ appears because you don't deposit all charge at the full final voltage; you start at V = 0 and build up to the final V. This energy lives in the electric field between the plates. When you discharge a capacitor through a circuit, that stored field energy becomes the work done on the charges.

The key conceptual shift in this topic is treating capacitance as a property of the geometry, not of the charge or voltage. You can double Q and V doubles proportionally; C stays the same. This invariance is what makes capacitance a useful circuit parameter — it is a fixed characteristic of the device, like mass or resistance. In circuits, capacitors appear wherever you need to store energy, smooth out voltage fluctuations, or block DC while passing AC — all consequences of this fundamental charge-per-volt relationship.
