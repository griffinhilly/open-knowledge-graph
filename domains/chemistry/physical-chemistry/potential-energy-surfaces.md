---
id: potential-energy-surfaces
title: Potential Energy Surfaces and Reaction Coordinates
domain: chemistry
course: physical-chemistry
prerequisites:
- id: born-oppenheimer-approximation
  type: hard
- id: collision-theory-advanced-kinetics
  type: soft
builds-toward:
- transition-state-theory
- unimolecular-reaction-mechanisms
tags:
- PES
- transition-state
- saddle-point
- reaction-coordinate
- IRC
- Hammond-postulate
stage: advanced
status: validated
---

# Potential Energy Surfaces and Reaction Coordinates

## Core Idea
A potential energy surface (PES) is the electronic energy of a molecular system as a function of all nuclear coordinates, obtained within the Born-Oppenheimer approximation. Reactants, products, and intermediates correspond to minima on the PES; the transition state is a first-order saddle point — a maximum along the reaction coordinate but a minimum in all perpendicular directions. The intrinsic reaction coordinate (IRC) traces the minimum-energy path from reactants through the transition state to products. Hammond's postulate states that the transition state resembles the higher-energy species (reactants or products), providing qualitative predictions of TS structure without quantum calculations.

## How It's Best Learned
Study 2D contour maps of PESs for simple reactions (e.g., H + H₂ → H₂ + H). Identify minima, saddle points, and valley-ridge inflection points. Confirm Hammond's postulate by comparing exothermic and endothermic reactions.

## Common Misconceptions
- Thinking the transition state is an intermediate — it has no lifetime and cannot be isolated.
- Confusing the reaction coordinate (a path through multidimensional space) with a single bond length.

## Questions

```yaml
- question: "A chemist proposes to isolate a transition state and study its spectroscopic properties in the same way they would study a reaction intermediate. Why is this impossible?"
  type: multiple-choice
  options:
    - "Transition states are too small to detect spectroscopically"
    - "Transition states have no imaginary vibrational frequencies and therefore cannot absorb light"
    - "Transition states are saddle points with no kinetic stability — any displacement leads downhill, so they have no lifetime"
    - "Transition states can only exist in the gas phase, not in solution"
  answer: 2
  explanation: "A transition state is a first-order saddle point on the PES: it is a maximum along the reaction coordinate, so any motion along that coordinate causes the system to roll downhill toward reactants or products. Unlike an intermediate (which sits in a local minimum and can persist for some duration), the transition state has no barrier confining it — it exists at an energy maximum with zero lifetime. Spectroscopy requires a molecule to spend time in a given state, which intermediates can do but transition states cannot."

- question: "Reaction A is highly exothermic (ΔE = −80 kJ/mol). Reaction B is highly endothermic (ΔE = +80 kJ/mol). According to Hammond's postulate, which statement best describes the transition states?"
  type: multiple-choice
  options:
    - "Reaction A has an early TS resembling reactants; Reaction B has a late TS resembling products"
    - "Reaction A has a late TS resembling products; Reaction B has an early TS resembling reactants"
    - "Both have TS structures midway between reactants and products regardless of thermodynamics"
    - "Hammond's postulate applies only to reactions in which bonds are broken homolytically"
  answer: 0
  explanation: "Hammond's postulate states the TS resembles whichever species it is closer to in energy. For an exothermic reaction, the TS is close in energy to the high-energy reactants (early TS: bonds barely stretched, structure resembles reactants). For an endothermic reaction, the TS is close in energy to the high-energy products (late TS: bonds nearly fully broken or formed, structure resembles products). This asymmetry lets chemists predict TS geometry — and therefore selectivity and rate sensitivity — from the sign of the reaction energy alone."

- question: "The transition state of a reaction is simply a very short-lived intermediate."
  type: true-false
  answer: false
  explanation: "This is a critical distinction. An intermediate occupies a local minimum on the PES — it is surrounded by energy barriers in all directions and therefore has some finite lifetime, however brief. A transition state is a first-order saddle point — a maximum along the reaction coordinate, meaning there is no barrier preventing it from converting to reactants or products. It has zero lifetime and cannot be isolated. The words 'intermediate' and 'transition state' describe topologically distinct features of the PES, not merely different lifetimes."

- question: "The intrinsic reaction coordinate (IRC) can be described as the path a classical ball would follow rolling from the saddle point toward reactants or products with infinitesimal initial kinetic energy."
  type: true-false
  answer: true
  explanation: "This physical picture captures the definition accurately. The IRC traces the minimum-energy path (steepest-descent path) from the transition state downhill in both directions — toward reactants and toward products. Starting from the saddle point and moving infinitesimally in the direction of the imaginary frequency (the downhill direction), the system follows the path of steepest descent, exactly as a ball with negligible kinetic energy would roll. The energy profile along the IRC is the familiar reaction energy diagram with its activation barrier."

- question: "Explain what makes the transition state a 'saddle point' and why this distinguishes it from both reactant/product minima and from random points on the PES."
  type: short-answer
  answer: "A saddle point is simultaneously a maximum in one direction and a minimum in all perpendicular directions — like the highest point on a mountain pass, which is the lowest point along the ridge but the highest point on the trail between two valleys. For a transition state, the 'downhill' direction is the reaction coordinate (movement along it converts TS to reactants or products), while all directions perpendicular to the reaction coordinate are uphill (the TS is confined laterally). This makes the TS a maximum along the reaction pathway but stable against displacements in any other direction, which is why it has exactly one imaginary vibrational frequency."
  explanation: "Minima on the PES (reactants, products, intermediates) are downhill in all directions — any displacement raises the energy, providing stability. Arbitrary points are typically saddle-point-like in some directions but not in the structured first-order way. The transition state's defining property — one imaginary frequency, corresponding to the reaction-coordinate motion — is what identifies it computationally and explains why it cannot be isolated: the system 'wants' to move in that one downhill direction."
```

## Explainer

From the Born-Oppenheimer approximation, you know that electrons move so much faster than nuclei that you can solve for the electronic energy at each fixed arrangement of nuclei. If you do this for every possible arrangement, you get a surface — the **potential energy surface (PES)** — where each point represents a molecular geometry and the height at that point is the total electronic energy. For a diatomic molecule, the PES is just a curve (energy versus bond length). For a triatomic system like H + H₂, the PES becomes a two-dimensional surface plotted over two bond distances, and for larger molecules it extends into many dimensions that we cannot visualize directly but can analyze mathematically.

The topology of the PES tells the entire story of a chemical reaction. **Minima** on the surface correspond to stable species — reactants, products, and intermediates — because any small displacement raises the energy. The system naturally settles into these valleys. Between two minima lies a mountain pass: the **transition state**, which is technically a first-order saddle point. A saddle point is a maximum in one direction (the reaction coordinate) but a minimum in all perpendicular directions, just like a mountain pass is the highest point on the trail between two valleys but the lowest point on the ridge connecting two peaks. The transition state has exactly one imaginary vibrational frequency, corresponding to the motion that carries the system over the barrier.

The **intrinsic reaction coordinate (IRC)** traces the minimum-energy pathway from reactants through the transition state to products. Think of it as the path a ball would follow if it rolled downhill from the saddle point in both directions with infinitesimal kinetic energy. The IRC gives you the reaction coordinate — not a single bond distance, but a composite coordinate that may involve simultaneous bond breaking and forming, angle changes, and molecular rearrangement. The energy profile along the IRC is the familiar reaction energy diagram with its activation energy barrier.

**Hammond's postulate** provides a powerful shortcut for predicting transition state structure without computing the full PES. It states that the transition state resembles whichever species — reactants or products — it is closer to in energy. For a highly exothermic reaction, the transition state is close in energy to the reactants, so it resembles the reactants structurally (early transition state with bonds only slightly stretched). For a highly endothermic reaction, the transition state resembles the products (late transition state with bonds nearly fully broken or formed). This lets you make qualitative predictions about activation energies and selectivity: if you know whether a reaction is exothermic or endothermic, Hammond's postulate tells you roughly what the transition state looks like, which in turn predicts how sensitive the rate is to structural changes in the reactants.
