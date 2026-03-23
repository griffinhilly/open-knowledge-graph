---
id: capacitor-geometry
title: 'Capacitors: Geometry and Capacitance'
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: dielectric-polarization
  type: soft
- id: electric-potential-field
  type: hard
builds-toward:
- energy-stored-capacitors
tags:
- capacitor
- geometry
- capacitance
stage: formal-systems
status: validated
---

# Capacitors: Geometry and Capacitance

## Core Idea
A capacitor stores charge by maintaining a potential difference between conductors. Capacitance is C = Q/V. For a parallel-plate capacitor: C = ε₀κᵣA/d. For spherical and cylindrical geometries: C_sphere = 4πε₀κᵣab/(b−a) and C_cylinder = 2πε₀κᵣℓ/ln(b/a). Capacitance depends only on geometry and material properties, independent of Q and V.

## Questions

```yaml
- question: "A parallel-plate capacitor is charged so that it holds charge Q at voltage V. If you then double the charge Q stored on it (by connecting a stronger battery), what happens to the capacitance C?"
  type: multiple-choice
  options:
    - "C doubles — since C = Q/V and Q increased, C must increase"
    - "C stays the same — capacitance depends only on geometry and material, not on Q or V"
    - "C halves — the stronger field from more charge reduces the effective capacitance"
    - "C increases, and V also doubles, so the ratio C = Q/V stays the same only by coincidence"
  answer: 1
  explanation: "Capacitance C = Q/V is a geometric constant — it characterizes the device, not the charge state. When you double Q, the voltage V also doubles proportionally (since V = Q/C), keeping the ratio C = Q/V unchanged. C depends only on plate area A, separation d, and dielectric constant κᵣ: C = ε₀κᵣA/d. This is the central insight: Q and V are conjugate variables that both change together, while C remains fixed by geometry."

- question: "A cylindrical capacitor has inner radius a, outer radius b, and length ℓ. If you double the length ℓ while keeping a and b the same, what happens to capacitance?"
  type: multiple-choice
  options:
    - "Capacitance doubles — C_cylinder = 2πε₀ℓ/ln(b/a), so doubling ℓ doubles C"
    - "Capacitance increases by a factor of ln(2) — the logarithm picks up the extra length"
    - "Capacitance is halved — a longer cylinder distributes charge over more surface area, reducing efficiency"
    - "Capacitance is unchanged — it depends only on the ratio b/a, not the absolute length"
  answer: 0
  explanation: "The formula C_cylinder = 2πε₀κᵣℓ/ln(b/a) shows that capacitance scales linearly with ℓ. Doubling ℓ doubles C. Physically, a longer cylinder provides twice as much plate area (the cylindrical surfaces), just as increasing plate area A doubles a parallel-plate capacitor's capacitance. The log term ln(b/a) captures the radial geometry and is fixed when a and b don't change."

- question: "Inserting a dielectric material with relative permittivity κᵣ > 1 between the plates of a charged capacitor increases its capacitance because the dielectric polarizes, reducing the effective electric field and lowering the voltage for the same stored charge."
  type: true-false
  answer: true
  explanation: "This is correct. The dielectric's molecules align with the applied field, creating bound surface charges that partially oppose the free charges on the plates. This reduces the net electric field E, and since V = Ed (for a parallel-plate capacitor), V decreases for the same Q. Lower V with the same Q means C = Q/V increases. The dielectric effectively 'helps' the capacitor store charge more efficiently. All three geometry formulas gain a factor of κᵣ: C = ε₀κᵣA/d, etc."

- question: "A parallel-plate capacitor with larger plate separation d stores more charge at a given voltage, so increasing d increases capacitance."
  type: true-false
  answer: false
  explanation: "This is backwards. C = ε₀A/d — capacitance is inversely proportional to separation d. A larger gap means the electric field E = V/d is weaker for the same voltage, so fewer charges are induced on the plates (Q = CV decreases). Intuitively, moving the plates farther apart weakens the attractive interaction between opposite charges, reducing the device's ability to store charge per volt. To increase capacitance, you want a smaller d, not larger."

- question: "Why does capacitance C = Q/V remain constant as Q and V change — what physical property does this represent?"
  type: short-answer
  answer: "Capacitance measures a geometric property of the device: how much charge it can hold per unit of voltage difference. When you increase Q by adding more charge, the electric field between the conductors grows proportionally, and so does the voltage V = ∫E·dr. Since both Q and V scale together, their ratio C = Q/V stays fixed. This means C is a property of the geometry (plate area, separation, shape) and the material (dielectric constant) — not of how much charge happens to be stored at the moment. It characterizes the device's intrinsic ability to store charge, independent of its current state."
  explanation: "This independence from Q and V is what makes capacitance a useful circuit parameter: you can specify a capacitor by its capacitance value C, and then calculate V from Q (or vice versa) using V = Q/C for any charge state. The same reasoning explains why the derivation always cancels Q: finding E from Gauss's law gives a field proportional to Q, integrating to get V gives a result proportional to Q, and dividing Q by V eliminates Q entirely, leaving only geometric factors."
```

## Explainer

You already know that the **electric potential** V at a point describes the energy per unit charge needed to bring a test charge there. A capacitor exploits this idea deliberately: it consists of two conductors held apart, and when charge Q is deposited on them (equal and opposite), a potential difference V develops between them. The ratio C = Q/V is the **capacitance** — a geometric quantity that tells you how efficiently the device stores charge per volt of potential difference. A large capacitance means you can store a lot of charge with only a modest voltage; a small capacitance means even a little charge drives a large voltage.

To see where the geometry enters, consider the simplest case: two large parallel conducting plates, each with area A, separated by a small distance d. From your study of electric potential and Gauss's law, the electric field between ideal parallel plates is uniform: E = σ/ε₀ = Q/(ε₀A). The potential difference is just that field integrated over the gap: V = Ed = Qd/(ε₀A). Plugging into C = Q/V, the charge cancels entirely — giving C = ε₀A/d. This is the key insight: the Q and V dependence disappears, leaving only the geometric factors. A larger plate area stores more charge at the same voltage; a larger gap reduces capacitance because the same charge spreads its influence over more distance.

For other geometries you use the same approach: find the field (via Gauss's law exploiting symmetry), integrate to get the potential difference, and divide Q by V. For a **spherical capacitor** with inner radius a and outer radius b, the field is radial and falls off as Q/(4πε₀r²), so integrating from a to b gives V = Q(b−a)/(4πε₀ab), and C = 4πε₀ab/(b−a). Notice that as b → ∞ this becomes C = 4πε₀a — the capacitance of a single isolated sphere of radius a relative to infinity. For a **cylindrical capacitor** of length ℓ, the field is Q/(2πε₀ℓr), integrating from r = a to r = b yields V = Q·ln(b/a)/(2πε₀ℓ), so C = 2πε₀ℓ/ln(b/a). The logarithm reflects how the radial field distributes over a growing circumference.

Inserting a **dielectric material** (relative permittivity κᵣ) between the conductors multiplies capacitance by κᵣ in all three formulas. Physically, the dielectric polarizes: its molecules align with the applied field, creating bound surface charges that partially cancel the free charges on the plates, reducing the net field and the potential difference. Lower V for the same Q means higher C. All three geometry formulas therefore carry the factor ε₀κᵣ: C = ε₀κᵣA/d, C_sphere = 4πε₀κᵣab/(b−a), and C_cylinder = 2πε₀κᵣℓ/ln(b/a). The central lesson is that capacitance is a property of space and material, not of the charge itself — you can change Q and V dramatically while C remains fixed, as long as their ratio stays constant.
