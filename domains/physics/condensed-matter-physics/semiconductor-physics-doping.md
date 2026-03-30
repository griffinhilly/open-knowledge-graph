---
id: semiconductor-physics-doping
title: Semiconductor Physics (Doping and p-n Junctions)
domain: physics
course: condensed-matter-physics
prerequisites:
- id: metals-insulators-semiconductors
  type: hard
- id: fermi-dirac-statistics
  type: hard
tags:
- semiconductor
- doping
- p-n-junction
- carrier-concentration
stage: expert
status: validated
---

# Semiconductor Physics (Doping and p-n Junctions)

## Core Idea
Intrinsic semiconductors have equal concentrations of thermally excited electrons and holes (n = p = n_i). Doping — substituting impurity atoms with more or fewer valence electrons — creates extrinsic semiconductors: n-type (donor impurities, excess electrons) or p-type (acceptor impurities, excess holes). The Fermi level shifts toward the conduction band in n-type and toward the valence band in p-type material. A p-n junction forms a depletion region with a built-in electric field that permits current flow in one direction (forward bias) but blocks it in the other (reverse bias), creating a diode — the fundamental building block of all semiconductor electronics.

## Questions

```yaml
- question: "In n-type silicon doped with phosphorus, the Fermi level shifts toward the conduction band. Why doesn't it shift all the way into the conduction band?"
  type: multiple-choice
  options:
    - "The crystal structure prevents the Fermi level from entering a band"
    - "At finite temperature, the Fermi level must balance electron occupation: it rises high enough that the donor states are mostly ionized and the conduction band has enough electrons to match the donor density, but thermal broadening keeps it below the band edge except at extreme doping"
    - "The Fermi level is fixed at the middle of the gap by definition"
    - "Phosphorus atoms repel the Fermi level away from the conduction band"
  answer: 1
  explanation: "The Fermi level position is determined self-consistently by charge neutrality: the number of ionized donors (plus holes) must equal the number of conduction electrons. At moderate doping (~10^15-10^18 cm^-3), E_F sits between the donor level and the conduction band edge. At very high doping (>~10^19 cm^-3 in Si), E_F can actually enter the conduction band, creating a 'degenerate' semiconductor that behaves metallically. Temperature also matters: at very low T, carriers freeze out onto donors and E_F drops; at very high T, intrinsic carriers dominate and E_F returns to mid-gap."

- question: "The law of mass action states that np = n_i^2 in a semiconductor at thermal equilibrium, regardless of doping. What is the physical origin of this constraint?"
  type: multiple-choice
  options:
    - "It follows from conservation of charge in the crystal"
    - "It results from the product of the electron and hole Fermi-Dirac distributions: n depends on (E_F - E_c) and p depends on (E_v - E_F), so their product np is independent of E_F and depends only on the gap and temperature"
    - "It is an empirical observation with no theoretical derivation"
    - "It holds only for intrinsic semiconductors"
  answer: 1
  explanation: "n = N_c exp(-(E_c - E_F)/k_BT) and p = N_v exp(-(E_F - E_v)/k_BT). The product np = N_c N_v exp(-E_g/k_BT) = n_i^2, where the Fermi level cancels. This means that in equilibrium, increasing the electron concentration (by n-type doping) necessarily decreases the hole concentration, and vice versa. The constraint is purely thermodynamic and holds for any equilibrium doping — it breaks down only under non-equilibrium conditions (illumination, injection)."

- question: "A p-n junction in equilibrium has a built-in potential but produces no current. Explain why, despite the electric field in the depletion region."
  type: short-answer
  answer: "In equilibrium, the Fermi level is uniform throughout the junction. The built-in electric field in the depletion region creates a drift current (minority carriers swept across by the field), but this is exactly balanced by a diffusion current (majority carriers diffusing against the field from the high-concentration side). The two currents cancel at every point, giving zero net current. This must be the case: a p-n junction in thermal equilibrium is a closed system at uniform temperature, and any net current would violate the second law of thermodynamics (you could extract work from a system at uniform temperature)."
  explanation: "Forward bias reduces the built-in potential, allowing diffusion current to exceed drift current — net current flows. Reverse bias increases the barrier, suppressing diffusion and leaving a small reverse saturation current from thermally generated minority carriers."

- question: "Why does the depletion region of a p-n junction widen under reverse bias and narrow under forward bias?"
  type: short-answer
  answer: "Under reverse bias, the external voltage adds to the built-in potential, increasing the electric field across the junction. This stronger field sweeps more mobile carriers away from the junction, uncovering more fixed ionized dopant charges on both sides — the depletion region widens. Under forward bias, the external voltage opposes the built-in potential, reducing the field. Majority carriers can now diffuse further into the junction, neutralizing some of the fixed charges, and the depletion region narrows. At strong enough forward bias, the depletion region nearly vanishes and large currents flow."
  explanation: "The depletion width scales as W ∝ √(V_bi - V_applied) for an abrupt junction, where V_bi is the built-in potential. Reverse bias makes V_applied negative, increasing W. This voltage-dependent width is the basis of varactor diodes (voltage-tunable capacitors)."
```

## Explainer

Pure semiconductors like silicon at room temperature have roughly equal numbers of electrons in the conduction band and holes in the valence band, with carrier concentrations around 10^{10} cm^{-3} — far too few for practical electronics. The breakthrough that enabled the semiconductor industry is **doping**: intentionally introducing impurity atoms to control the carrier concentration. Substituting a silicon atom with phosphorus (Group V, one extra valence electron) creates an n-type semiconductor with a donor level just below the conduction band. At room temperature, virtually all donors are ionized, adding their extra electrons to the conduction band. Similarly, boron (Group III) creates an acceptor level just above the valence band, producing p-type material with excess holes.

The Fermi level acts as the thermodynamic "dial" that tracks the carrier balance. In n-type material, E_F shifts upward toward E_c; in p-type, it shifts downward toward E_v. At equilibrium, the carrier concentrations are constrained by the **law of mass action**: np = n_i^2, regardless of doping. This means doping cannot increase both carrier types — adding electrons necessarily suppresses holes, and vice versa. The constraint arises from the mathematical structure of Fermi-Dirac statistics and is one of the most powerful relationships in semiconductor physics.

The **p-n junction** — the interface between p-type and n-type regions — is the fundamental device structure. When the two regions are brought into contact, electrons diffuse from n to p and holes from p to n, leaving behind fixed ionized dopants. This creates a **depletion region** devoid of mobile carriers, with a built-in electric field pointing from n to p. In equilibrium, the drift and diffusion currents balance exactly (as required by thermodynamics), and no net current flows. The Fermi level is constant across the entire junction.

Applying a **forward bias** (positive voltage on the p-side) reduces the built-in potential barrier, exponentially increasing the current as carriers flood across the junction: I = I_0(e^{V/V_T} - 1), where V_T = k_BT/e ~ 26 mV at room temperature. **Reverse bias** increases the barrier, leaving only a tiny saturation current I_0 from thermally generated minority carriers. This asymmetric current-voltage characteristic is the diode — the building block from which transistors, solar cells, LEDs, and laser diodes are all constructed. The physics of the p-n junction is band theory made tangible: the interplay of Fermi statistics, electrostatics, and diffusion in a system with controlled band filling.
