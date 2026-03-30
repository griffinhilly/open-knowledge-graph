---
id: integer-quantum-hall-effect
title: Quantum Hall Effect (Integer)
domain: physics
course: condensed-matter-physics
prerequisites:
- id: band-structure-density-of-states
  type: hard
- id: boltzmann-transport-equation-cm
  type: soft
tags:
- quantum-hall-effect
- landau-levels
- topological
- edge-states
stage: expert
status: validated
---

# Quantum Hall Effect (Integer)

## Core Idea
In a two-dimensional electron gas subjected to a strong perpendicular magnetic field, the energy spectrum splits into discrete Landau levels E_n = hbar omega_c (n + 1/2), where omega_c = eB/mc is the cyclotron frequency. When the Fermi level lies between Landau levels, the Hall conductance is exactly quantized: sigma_{xy} = nu e^2/h, where nu is an integer equal to the number of filled Landau levels. This quantization is extraordinarily precise (~1 part in 10^9) and is independent of material details, disorder, or sample geometry — it is topological in origin. The integer quantum Hall effect provides the primary resistance standard and was the first example of a topological phase of matter.

## Questions

```yaml
- question: "The Hall conductance σ_{xy} = νe²/h is quantized to extraordinary precision despite the samples being disordered. How does disorder, which usually degrades quantization, actually help here?"
  type: multiple-choice
  options:
    - "Disorder has no effect on the quantum Hall effect"
    - "Disorder broadens each Landau level into a band of localized states (in the tails) and extended states (at the center). The localized states act as a reservoir that pins the Fermi level between Landau levels over a finite range of B or carrier density, creating the plateaus. Without disorder, the Hall conductance would change continuously with B, showing no plateaus at all"
    - "Disorder screens the magnetic field, making the Landau levels sharper"
    - "Disorder creates additional Landau levels that improve the quantization"
  answer: 1
  explanation: "This is counterintuitive but essential. In a perfect 2D system, Landau levels are infinitely sharp and the Hall conductance would jump discontinuously at each level crossing — no plateaus. Disorder broadens the levels, creating a continuum of localized states (which don't contribute to transport) and a narrow band of extended states (which carry current). As B changes, the Fermi level sweeps through localized states without changing σ_{xy}, creating a plateau. The transition between plateaus occurs only when E_F crosses the extended states at the center of a Landau level."

- question: "The integer quantum Hall effect is called 'topological' because the quantized Hall conductance is related to a topological invariant (the TKNN integer or Chern number). What does this mean physically?"
  type: multiple-choice
  options:
    - "The Hall conductance depends on the topology (shape) of the sample"
    - "The Hall conductance of each filled Landau level is determined by an integer topological invariant (Chern number) of the band structure in the magnetic Brillouin zone. Like the genus of a surface (a sphere has 0 holes, a torus has 1), this integer cannot change under smooth deformations — it is robust against disorder, interactions, and geometry changes, explaining the extraordinary precision of the quantization"
    - "Topological means the effect only occurs in materials with non-trivial crystal topology"
    - "It refers to the fact that the magnetic field lines form closed loops"
  answer: 1
  explanation: "The Chern number C_n = (1/2π)∫∫ F dk_x dk_y is the integral of the Berry curvature F over the magnetic Brillouin zone for each filled band. It is always an integer (a mathematical theorem about fiber bundles), and the Hall conductance is σ_{xy} = (e²/h)Σ_n C_n. Since an integer cannot change continuously, the Hall conductance is exactly quantized and immune to any perturbation that doesn't close the gap between Landau levels. This topological protection is fundamentally different from symmetry protection and is the reason for the remarkable precision."

- question: "In the integer quantum Hall state, the bulk is insulating but current flows along the edges of the sample. Explain this bulk-boundary correspondence."
  type: short-answer
  answer: "When the Fermi level sits between Landau levels, the bulk is a gapped insulator — there are no extended states to carry current. However, at the sample edges, the confining potential bends the Landau levels upward, and they must cross the Fermi level. These edge-crossing states are chiral (propagating in one direction only, determined by the magnetic field direction) and carry the Hall current. The number of edge channels equals the number of filled Landau levels ν. Because the edge states are chiral (no counter-propagating states to scatter into), they are immune to backscattering and carry current dissipationlessly. This bulk-boundary correspondence — a gapped topological bulk implies protected gapless edge states — is a general principle that extends to all topological phases."
  explanation: "The edge states can be understood semiclassically: electrons near the boundary undergo skipping orbits (reflecting off the edge), producing a net drift along the edge. On opposite edges, the drift is in opposite directions. This picture gives the right number of channels but misses the topological protection."

- question: "The integer quantum Hall effect provides the international resistance standard. Why is it more precise than any material-based standard?"
  type: short-answer
  answer: "The quantized Hall resistance R_H = h/νe² = 25,812.807... Ω/ν depends only on fundamental constants (h and e) and the integer ν. It has no material-dependent corrections — no dependence on sample purity, geometry, temperature (within limits), or the detailed nature of the 2D electron gas. This universality is guaranteed by the topological nature of the quantization. The von Klitzing constant R_K = h/e² has been measured to agree across different materials (GaAs, Si, graphene) to parts per billion, confirming that it is truly a fundamental constant. Since 2019, the SI system uses R_K to define the ohm."
  explanation: "Von Klitzing discovered the effect in 1980 and received the Nobel Prize in 1985. The fact that a messy semiconductor sample with disorder, impurities, and finite temperature gives a resistance quantized to 10⁻⁹ precision was completely unexpected and demanded a fundamental explanation — which topology provided."
```

## Explainer

The **integer quantum Hall effect** (IQHE), discovered by Klaus von Klitzing in 1980, occurs when a two-dimensional electron gas (2DEG) — typically at a semiconductor heterointerface like GaAs/AlGaAs — is placed in a strong perpendicular magnetic field at low temperature. The Hall resistance R_{xy} = V_H/I, instead of increasing linearly with B as in the classical Hall effect, develops a series of flat plateaus at precisely quantized values R_{xy} = h/(nu e^2), where nu = 1, 2, 3, ... The longitudinal resistance R_{xx} simultaneously vanishes on each plateau. The quantization is exact to about 1 part in 10^9.

The starting point for understanding the IQHE is **Landau quantization**. A free electron in 2D in a magnetic field B has its continuous energy spectrum collapsed into discrete **Landau levels** at energies E_n = hbar omega_c (n + 1/2), each massively degenerate (degeneracy = eB/h per unit area). When exactly nu Landau levels are filled and the Fermi level sits in the gap between the nu-th and (nu+1)-th levels, the system is a gapped insulator in the bulk with quantized Hall conductance sigma_{xy} = nu e^2/h.

The role of **disorder** is crucial and counterintuitive. In a clean system, Landau levels are infinitely sharp delta functions, and the Fermi level can only sit in a gap at discrete values of B — no plateaus would exist. Disorder broadens each Landau level into a band of mostly localized states (Anderson localization in 2D) with a narrow strip of delocalized states at the center. As B varies, the Fermi level sweeps through the localized states without changing the transport properties, creating the observed plateaus. The transition between plateaus (where R_{xx} peaks) occurs when E_F crosses the delocalized states.

The deep reason for the exact quantization is **topology**. The Hall conductance of each filled Landau level is a topological invariant — the **Chern number** — computed as an integral of the Berry curvature over the magnetic Brillouin zone. Chern numbers are integers by mathematical necessity (like the genus of a surface), and they cannot change under continuous deformations of the Hamiltonian that do not close the energy gap. This topological protection explains why the quantization is independent of disorder, sample geometry, and material details. The IQHE was the first experimentally realized **topological phase of matter**, launching the field that later produced topological insulators, topological superconductors, and the mathematical framework of topological band theory.
