---
id: ampere-law-applications
title: Ampere's Law and Its Applications
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: biot-savart-law-applications
  type: hard
- id: divergence-theorem
  type: soft
builds-toward:
- faraday-law-electromagnetic-induction
- lorentz-force-complete-em
tags:
- ampere-law
- symmetry
- current
stage: formal-systems
status: validated
---

# Ampere's Law and Its Applications

## Core Idea
Ampere's law states ∮B⋅dL = μ₀I_enclosed. Like Gauss's law for magnetism, it is most powerful with symmetry (long wire, solenoid, toroid). Field circulates around current, with right-hand rule determining direction.

## Questions

```yaml
- question: "A student wants to use Ampere's law to find the magnetic field at distance r from a long straight wire. They draw a square Amperian loop of side length r centered on the wire. Can they solve for B?"
  type: multiple-choice
  options:
    - "Yes — any closed loop gives the same result; the choice of loop shape doesn't matter"
    - "No — on a square loop, B varies in magnitude and direction along each side, so the integral B·dL cannot be simplified to B times a simple length"
    - "No — Ampere's law only applies to circular loops by definition"
    - "Yes — since I_enclosed is the same for any loop enclosing the wire, B can be computed directly"
  answer: 1
  explanation: "Ampere's law ∮B·dL = μ₀I_enclosed is always *true* for any closed loop, but it's only *useful* when you can factor B out of the integral. On a square loop around a wire, B changes in magnitude and direction at every point — the integral is a complicated mess that doesn't simplify without already knowing B. A circular loop of radius r works because cylindrical symmetry guarantees B is tangential and constant in magnitude everywhere on the circle, turning the integral into B(2πr). Option D correctly notes I_enclosed is independent of loop shape but wrongly concludes B can be found — you need to evaluate the left side, not just the right."

- question: "The result B = μ₀nI inside a solenoid (where n is turns per unit length) comes from applying Ampere's law with a rectangular loop. Which feature of that loop analysis produces this result?"
  type: multiple-choice
  options:
    - "The rectangular loop must enclose all N turns of the solenoid to capture the total current"
    - "A rectangular loop straddling the solenoid wall has only one side contributing to ∮B·dL — the segment inside — because B ≈ 0 outside and B is perpendicular to the two transverse sides"
    - "The circular winding geometry of the solenoid ensures B is constant everywhere on any rectangular loop"
    - "Biot-Savart must first confirm the field is uniform before Ampere's law can be applied"
  answer: 1
  explanation: "The rectangle is chosen to straddle the solenoid wall (one segment inside, one outside, two transverse segments). Outside: B ≈ 0, contributing nothing. Transverse sides: B is parallel to the solenoid axis, perpendicular to dL along those sides, contributing nothing. Inside: B is parallel to dL and uniform, contributing B × L. The right side is μ₀ × (nL) × I, since nL turns pass through the loop. Thus B × L = μ₀nLI → B = μ₀nI. The loop doesn't need to enclose all turns (option A); it just needs to enclose a known number of them."

- question: "Ampere's law ∮B·dL = μ₀I_enclosed is always mathematically valid, but it is only practically useful for computing magnetic fields when the current distribution has sufficient symmetry."
  type: true-false
  answer: true
  explanation: "Exactly right. Ampere's law is an exact statement about any closed loop, but it becomes a useful computational tool only when you can choose an Amperian loop where B is constant and parallel on part of the loop (and zero or perpendicular on the rest). Without that symmetry, the law gives you a true equation with an unknown integral on the left — unsolvable without already knowing B everywhere. Biot-Savart, though harder to compute, works for asymmetric configurations where Ampere's law cannot be usefully applied."

- question: "The Amperian loop used in Ampere's law must correspond to an actual physical conductor or current path in the problem."
  type: true-false
  answer: false
  explanation: "False — the Amperian loop is a purely mathematical construct chosen for computational convenience. It has no physical reality and need not correspond to any conductor or circuit. For a solenoid, we choose a rectangle that straddles the solenoid wall; for a wire, we choose a circle around it. These are imaginary geometric objects drawn to exploit symmetry. The only physical requirement is that I_enclosed correctly counts the net current passing through any surface bounded by the loop."

- question: "What is the key criterion for choosing a useful Amperian loop, and why does that criterion matter for the calculation?"
  type: short-answer
  answer: "The Amperian loop should be chosen so that B is either (1) parallel to dL and constant in magnitude — so ∮B·dL = B × (loop length) — or (2) perpendicular to dL — contributing zero. Without this, the left side of Ampere's law ∮B·dL is a complicated integral that cannot be evaluated without already knowing B in detail, defeating the purpose. Symmetry is what makes such a loop choice possible: cylindrical symmetry for a wire (circular loop), translational symmetry for a solenoid (rectangular loop), and toroidal symmetry for a toroid (circular loop inside the coils)."
  explanation: "This is the direct analog of choosing a Gaussian surface in Gauss's law: both techniques work by turning a hard integral into a trivial product using the fact that the field is uniform and aligned on the chosen surface or loop. The underlying law is always valid; the choice of integration path or surface determines whether it yields a usable equation."
```

## Explainer

You already know from Biot-Savart how to compute magnetic fields by integrating current contributions — but that approach becomes algebraically brutal for anything beyond a simple straight wire or loop. **Ampere's law**, ∮ B⃗ · dL⃗ = μ₀I_enclosed, is the magnetic analog of Gauss's law for electric fields: instead of summing up all the little field contributions, you exploit symmetry to turn a hard calculation into a trivial one. The left side is a **line integral** of the magnetic field around a closed loop (called an Amperian loop), and the right side is simply μ₀ times the total current passing through any surface bounded by that loop.

The strategy is identical to Gauss's law, just with a loop instead of a surface. You choose your Amperian loop so that B⃗ is either parallel or perpendicular to dL⃗ everywhere on the loop, and constant in magnitude where it is parallel. When that holds, the integral reduces to B × (circumference), and you can solve for B immediately. Consider the canonical example: an infinitely long straight wire carrying current I. By symmetry, B must be tangential (circling the wire) and constant in magnitude at any fixed radius r. Choose a circular Amperian loop of radius r centered on the wire: ∮ B⃗ · dL⃗ = B(2πr) = μ₀I, giving B = μ₀I/(2πr). This result, which agrees with Biot-Savart, drops out in two lines.

The same logic applies to the **solenoid** — a tightly wound coil of wire — which is the most practically important application. Inside an ideal solenoid, the field is uniform and parallel to the axis; outside, the field is essentially zero. Choose a rectangular Amperian loop straddling the solenoid wall: the only contributing segment is the one inside, giving B × L = μ₀(nL)I, where n is the number of turns per unit length. Thus B = μ₀nI inside the solenoid. A **toroid** (a solenoid bent into a donut shape) is the third classic case: a circular Amperian loop inside the toroid gives B = μ₀NI/(2πr), where N is the total number of turns and r is the radius of the loop.

The **right-hand rule** determines direction: curl the fingers of your right hand in the direction of positive current flow around the Amperian loop, and your thumb points in the direction of the net current that contributes positively. Alternatively, point your right thumb in the direction of current in a wire, and your curling fingers show the direction B circulates around it. The key constraint on Ampere's law (in the form ∮ B · dL = μ₀I) is that it only works for **steady currents** — this is the form you use in magnetostatics. Maxwell later added a displacement current correction term to make it valid for time-varying fields too, which is what completes the full electromagnetic theory you'll encounter next.
