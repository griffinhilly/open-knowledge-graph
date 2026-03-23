---
id: ergodicity-breaking
title: Ergodicity Breaking
domain: physics
course: statistical-mechanics
prerequisites:
- id: ergodic-hypothesis
  type: hard
- id: phase-transitions
  type: soft
builds-toward:
- spin-glasses-quenched-disorder
tags:
- non-equilibrium
- disorder
- dynamics
stage: expert
status: draft
---

# Ergodicity Breaking

## Core Idea
Ergodicity breaking occurs when a system's phase space fragments into disconnected regions separated by high barriers, preventing exploration of all microstates within experimental timescales. This commonly occurs in glasses and disordered systems, where dynamics become trapped in limited phase space regions far from true equilibrium.

## Questions

```yaml
- question: "Two glass samples are made from the same material — one cooled rapidly, one cooled slowly. Their densities and optical properties differ measurably. What does this observation demonstrate about ergodicity?"
  type: multiple-choice
  options:
    - "Rapid cooling produces a crystalline microstructure while slow cooling produces an amorphous one, explaining the different properties"
    - "The system is history-dependent: different cooling paths trap the system in different metastable free-energy valleys, demonstrating ergodicity breaking — the final state cannot be predicted from temperature and pressure alone"
    - "The glass transition temperature differs between the two samples, indicating different chemical compositions after cooling"
    - "Entropy production is greater during rapid cooling, which permanently elevates the free energy of the rapidly cooled sample"
  answer: 1
  explanation: "History-dependence is the observable signature of ergodicity breaking. In an ergodic system, the equilibrium state is determined entirely by macroscopic state variables (temperature, pressure, composition). In an ergodicity-broken system, the system is trapped in one of many metastable free-energy valleys, and which valley it occupies depends on its history — including cooling rate. Both glass samples have the same composition and are held at the same temperature, but they occupy different basins of the landscape. This path-dependence is impossible in a truly ergodic equilibrium system."

- question: "A ferromagnet below its Curie temperature is trapped in one magnetization direction and never spontaneously reverses. How does this ergodicity breaking differ from that of a glass?"
  type: multiple-choice
  options:
    - "Ferromagnets break ergodicity kinetically (slow dynamics), while glasses break it through a sharp thermodynamic phase transition with a well-defined order parameter"
    - "Ferromagnets break ergodicity through spontaneous symmetry breaking at a sharp phase transition with a well-defined order parameter; glasses break ergodicity kinetically, without a sharp transition or obvious order parameter, and their properties are history-dependent"
    - "Both systems break ergodicity identically — high free-energy barriers separate equivalent ground states in both cases, so the distinction is merely quantitative"
    - "Only glasses truly break ergodicity; ferromagnets remain ergodic because thermal fluctuations can eventually reverse the magnetization"
  answer: 1
  explanation: "The distinction is thermodynamic versus kinetic. In a ferromagnet, symmetry breaking is a genuine equilibrium phase transition: below T_c, the free energy has two equivalent minima separated by a barrier that diverges in the thermodynamic limit. This is sharp, reversible at T_c, and described by an order parameter (magnetization). Glass ergodicity breaking is kinetic: there is no sharp transition, no obvious order parameter, and the system falls out of equilibrium because structural relaxation times exceed experimental timescales. Glass properties are path-dependent in a way that reflects this kinetic trapping."

- question: "In an ergodicity-broken system, time averages measured over experimental timescales differ from ensemble averages because the system cannot explore all of phase space within those timescales."
  type: true-false
  answer: true
  explanation: "This is the operational definition of ergodicity breaking. Ergodicity, in statistical mechanics, equates time averages with ensemble averages — the justification for using equilibrium ensembles to predict measurable properties. When a system is trapped in a metastable free-energy valley, it samples only that valley's portion of phase space over any realistic observation time. Its time-averaged properties reflect the local valley, not the full ensemble of all accessible microstates — which is why different samples (different valleys) exhibit different properties."

- question: "Ergodicity breaking always requires a sharp thermodynamic phase transition — systems that remain in a disordered, amorphous state as they are cooled cannot break ergodicity."
  type: true-false
  answer: false
  explanation: "Glasses are the paradigm counterexample. A glass-forming liquid cooled below T_g becomes kinetically arrested in an amorphous, disordered state — no crystallization, no sharp phase transition, no obvious order parameter. The ergodicity breaking is kinetic: structural relaxation times grow faster than experimentally accessible timescales as temperature drops, eventually trapping the system. This is distinct from symmetry-breaking ergodicity breaking at equilibrium phase transitions. Glass demonstrates that ergodicity breaking can arise from dynamics alone, without any thermodynamic transition."

- question: "What is the key observable signature that distinguishes an ergodicity-broken system from a truly equilibrated one, and why does it arise from the free-energy landscape picture?"
  type: short-answer
  answer: "The key signature is history-dependence: two samples prepared with the same macroscopic conditions (temperature, pressure, composition) but via different routes arrive at states with measurably different properties. In a truly ergodic equilibrium system, macroscopic state variables alone determine the equilibrium state — history is irrelevant. In an ergodicity-broken system, the preparation path determines which metastable free-energy valley the system occupies, and different valleys have different structural and physical properties."
  explanation: "The free-energy landscape picture explains why: if the landscape has many valleys separated by high barriers, different paths through configuration space lead to different valleys. Once trapped, the system cannot hop between valleys on experimental timescales, so the valley it occupies — determined by its history — determines its measured properties. A truly ergodic system has barriers low enough that thermal fluctuations explore all valleys, making the eventual state path-independent regardless of how the system arrived there."
```

## Explainer

The **ergodic hypothesis** you studied earlier makes a sweeping claim: given long enough time, a system visits every microstate consistent with its macroscopic constraints, and time averages equal ensemble averages. Statistical mechanics is built on this foundation. Ergodicity breaking is what happens when that assumption fails — and understanding *when* and *why* it fails is essential for understanding glasses, disordered magnets, proteins, and a wide range of complex systems.

The simplest way to picture ergodicity breaking is through a **free energy landscape**. Imagine phase space not as a flat field but as a mountainous terrain, where valleys are configurations of low free energy and ridges are high-barrier transitions between them. In a well-behaved ergodic system, thermal fluctuations are large enough to hop over barriers on reasonable timescales, so the system explores all valleys. Ergodicity breaks when the barriers become so high — or so numerous — that the system is effectively trapped in one valley forever on any practical observation timescale. The system is not at true thermodynamic equilibrium; it is stuck in a **metastable state** that will never relax to the global minimum.

Glasses are the paradigm example. Cool a liquid fast enough and it does not crystallize; instead it becomes increasingly viscous as temperature drops, until molecular rearrangements become so slow that the material behaves mechanically like a solid. At the glass transition temperature T_g, the structural relaxation time exceeds experimental timescales — the system is frozen into one particular amorphous configuration out of an astronomically large number of equivalent configurations. Different glass samples cooled by different routes end up in different valleys; their properties depend on history, not just temperature and pressure. This history-dependence is the smoking gun of ergodicity breaking. From the phase transitions prerequisite, you know that a symmetry-broken ordered phase (like a ferromagnet below T_c) also breaks ergodicity — the system is trapped in one magnetization direction and never spontaneously flips — but that is **spontaneous symmetry breaking** at a sharp phase transition. Glass is subtler: there is no sharp transition, no obvious order parameter, and the trapping is kinetic rather than thermodynamic.

**Spin glasses** represent a more exotic form: magnetic systems with quenched random interactions where some bonds favor alignment and others anti-alignment. No single ordered state wins; instead the system freezes into a frustrated configuration that depends on the specific disorder realization. The system's phase space fragments into an exponentially large number of nearly-degenerate valleys separated by high barriers — an extreme form of ergodicity breaking called **replica symmetry breaking**. Time averages become sample-dependent and the usual statistical mechanics ensemble must be reconsidered. The study of ergodicity breaking thus sits at the boundary between equilibrium statistical mechanics, dynamics, and the physics of disordered systems — the frontier this course is building toward.
