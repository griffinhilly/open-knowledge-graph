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
status: draft
---

# Ampere's Law and Its Applications

## Core Idea
Ampere's law states ∮B⋅dL = μ₀I_enclosed. Like Gauss's law for magnetism, it is most powerful with symmetry (long wire, solenoid, toroid). Field circulates around current, with right-hand rule determining direction.

## Explainer

You already know from Biot-Savart how to compute magnetic fields by integrating current contributions — but that approach becomes algebraically brutal for anything beyond a simple straight wire or loop. **Ampere's law**, ∮ B⃗ · dL⃗ = μ₀I_enclosed, is the magnetic analog of Gauss's law for electric fields: instead of summing up all the little field contributions, you exploit symmetry to turn a hard calculation into a trivial one. The left side is a **line integral** of the magnetic field around a closed loop (called an Amperian loop), and the right side is simply μ₀ times the total current passing through any surface bounded by that loop.

The strategy is identical to Gauss's law, just with a loop instead of a surface. You choose your Amperian loop so that B⃗ is either parallel or perpendicular to dL⃗ everywhere on the loop, and constant in magnitude where it is parallel. When that holds, the integral reduces to B × (circumference), and you can solve for B immediately. Consider the canonical example: an infinitely long straight wire carrying current I. By symmetry, B must be tangential (circling the wire) and constant in magnitude at any fixed radius r. Choose a circular Amperian loop of radius r centered on the wire: ∮ B⃗ · dL⃗ = B(2πr) = μ₀I, giving B = μ₀I/(2πr). This result, which agrees with Biot-Savart, drops out in two lines.

The same logic applies to the **solenoid** — a tightly wound coil of wire — which is the most practically important application. Inside an ideal solenoid, the field is uniform and parallel to the axis; outside, the field is essentially zero. Choose a rectangular Amperian loop straddling the solenoid wall: the only contributing segment is the one inside, giving B × L = μ₀(nL)I, where n is the number of turns per unit length. Thus B = μ₀nI inside the solenoid. A **toroid** (a solenoid bent into a donut shape) is the third classic case: a circular Amperian loop inside the toroid gives B = μ₀NI/(2πr), where N is the total number of turns and r is the radius of the loop.

The **right-hand rule** determines direction: curl the fingers of your right hand in the direction of positive current flow around the Amperian loop, and your thumb points in the direction of the net current that contributes positively. Alternatively, point your right thumb in the direction of current in a wire, and your curling fingers show the direction B circulates around it. The key constraint on Ampere's law (in the form ∮ B · dL = μ₀I) is that it only works for **steady currents** — this is the form you use in magnetostatics. Maxwell later added a displacement current correction term to make it valid for time-varying fields too, which is what completes the full electromagnetic theory you'll encounter next.
