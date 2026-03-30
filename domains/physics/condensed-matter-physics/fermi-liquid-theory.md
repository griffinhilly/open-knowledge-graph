---
id: fermi-liquid-theory
title: Fermi Liquid Theory
domain: physics
course: condensed-matter-physics
prerequisites:
- id: fermi-gas-ideal-quantum
  type: hard
- id: fermi-dirac-statistics
  type: hard
tags:
- fermi-liquid
- quasiparticle
- landau
- effective-mass
stage: expert
status: validated
---

# Fermi Liquid Theory

## Core Idea
Landau's Fermi liquid theory explains why interacting electrons in a metal behave qualitatively like a free Fermi gas, despite strong Coulomb repulsion. The key insight is that there exists a one-to-one correspondence (adiabatic continuity) between the states of the interacting system and those of the non-interacting Fermi gas. The elementary excitations are not bare electrons but quasiparticles — electron-like entities with renormalized effective mass m* and finite lifetime tau proportional to 1/(E - E_F)^2. Near the Fermi surface, quasiparticles are long-lived enough to be well-defined, and the system retains a sharp Fermi surface, linear specific heat, and Pauli-like susceptibility, but with renormalized coefficients.

## Questions

```yaml
- question: "Fermi liquid theory relies on 'adiabatic continuity' between the non-interacting and interacting ground states. What does this mean physically?"
  type: multiple-choice
  options:
    - "The interactions can be turned on quickly without changing the physics"
    - "If you imagine slowly turning on the electron-electron interaction starting from the free Fermi gas, the quantum numbers (k, spin) of each state are preserved — the states deform continuously without any level crossings or phase transitions, creating a one-to-one mapping between free-electron states and quasiparticle states"
    - "The interacting system has exactly the same energy levels as the free Fermi gas"
    - "Adiabatic continuity means the system is always in thermal equilibrium"
  answer: 1
  explanation: "Adiabatic continuity is the foundation of Fermi liquid theory. As interactions are turned on infinitely slowly, each free-electron state evolves into a quasiparticle state with the same quantum numbers (momentum, spin) but renormalized energy and effective mass. The crucial requirement is that no phase transition occurs during this process — if interactions drive an instability (superconductivity, magnetism, Mott transition), adiabatic continuity breaks down and Fermi liquid theory fails."

- question: "The quasiparticle lifetime in a Fermi liquid scales as τ ∝ 1/(E - E_F)^2. What is the physical origin of this energy dependence?"
  type: multiple-choice
  options:
    - "It follows from the uncertainty principle applied to the quasiparticle energy"
    - "Phase space restriction: a quasiparticle at energy E above E_F can only scatter into empty states above E_F and create particle-hole pairs, and the available phase space for both the final state and the particle-hole pair scales as (E - E_F), giving a scattering rate proportional to (E - E_F)^2"
    - "The Coulomb interaction itself becomes weaker at energies close to E_F"
    - "Crystal symmetry protects quasiparticles near E_F from scattering"
  answer: 1
  explanation: "This is the key result. At the Fermi surface (E = E_F), there are zero available final states for scattering because all states below are filled (Pauli exclusion). An excitation at energy ε above E_F has a phase space for scattering that is proportional to ε for the excited electron's final state and ε for the particle-hole pair it can create, giving τ^{-1} ∝ ε^2. This means quasiparticles become infinitely long-lived as E → E_F, which is why the Fermi liquid description is internally consistent: the entities it calls quasiparticles are well-defined precisely where the theory is applied."

- question: "Fermi liquid theory predicts that the electronic specific heat of a metal is linear in temperature, C = γT, just as for a free Fermi gas, but with a renormalized coefficient γ ∝ m*/m."
  type: true-false
  answer: true
  explanation: "The linear-T specific heat is a hallmark of a Fermi liquid. The renormalized coefficient γ = (π²/3)k_B² g*(E_F) reflects the quasiparticle density of states g* ∝ m* at the Fermi level. In heavy-fermion systems, m*/m can be 100-1000, producing enormously enhanced specific heat coefficients — but the functional form C ∝ T is preserved. Deviations from linearity (such as C ∝ T log T) signal non-Fermi-liquid behavior."

- question: "Under what conditions does Fermi liquid theory break down?"
  type: short-answer
  answer: "Fermi liquid theory breaks down when adiabatic continuity fails — when interactions drive the system through a phase transition or qualitative change. Key examples include: (1) Superconductivity, where Cooper pairing opens a gap and the Fermi surface is destroyed. (2) Magnetic ordering, where spontaneous symmetry breaking creates a new ground state. (3) Mott transitions, where strong correlations localize electrons despite a partially filled band. (4) One-dimensional systems, where the Fermi surface reduces to two points and any interaction, no matter how weak, destroys the quasiparticle picture (Luttinger liquid behavior). (5) Quantum critical points, where divergent fluctuations produce non-Fermi-liquid scaling (e.g., resistivity ∝ T instead of T²)."
  explanation: "The remarkable thing about Fermi liquid theory is how robust it is: it works for most metals despite interaction strengths comparable to the kinetic energy. Its failures define some of the most interesting problems in condensed matter: unconventional superconductors, heavy fermions, quantum criticality, and strongly correlated systems."
```

## Explainer

One of the deepest puzzles of solid-state physics is why the free-electron model works so well for metals, given that electrons interact via strong Coulomb repulsion (energies of several eV per electron). The answer, provided by Lev Landau in 1956, is **Fermi liquid theory**. The central concept is **adiabatic continuity**: if you start from the non-interacting Fermi gas and slowly turn on interactions, the ground state and low-energy excitations evolve smoothly — no phase transition occurs, and there is a one-to-one mapping between free-electron states and the states of the interacting system.

The mapped states are called **quasiparticles**. A quasiparticle with crystal momentum k and spin sigma is not a bare electron — it is an electron "dressed" by a cloud of particle-hole excitations from interactions with all other electrons. This dressing changes the effective mass from the bare electron mass m to a renormalized mass m*, and gives the quasiparticle a finite lifetime tau. Crucially, the lifetime diverges as the quasiparticle energy approaches E_F: tau is proportional to 1/(E - E_F)^2 due to **phase space restriction**. Near the Fermi surface, Pauli exclusion severely limits the available scattering channels (the electron has nowhere to scatter to because all nearby states are occupied), making quasiparticles increasingly sharp and well-defined.

Because quasiparticles carry the same quantum numbers as free electrons and are long-lived near E_F, the interacting system retains all the qualitative features of a Fermi gas: a sharp Fermi surface, a linear-T electronic specific heat C = gamma T, a temperature-independent Pauli paramagnetic susceptibility, and a T^2 resistivity from quasiparticle-quasiparticle scattering. The quantitative values are renormalized: gamma is proportional to m*/m, the susceptibility is enhanced by Landau parameters F_0^a, and the compressibility by F_0^s. These Landau parameters encode the residual quasiparticle interactions and are measured experimentally, not calculated from first principles.

Fermi liquid theory is the **default theoretical framework** for metals. Its power comes from its generality: it applies regardless of the microscopic details of the interactions, as long as adiabatic continuity holds. Its failures are equally important, because they signal exotic physics. Non-Fermi-liquid behavior — anomalous temperature dependences, absence of well-defined quasiparticles, breakdown of the T^2 resistivity — appears near quantum phase transitions, in heavy-fermion compounds, in cuprate superconductors, and in one-dimensional conductors. Understanding when and why Fermi liquid theory breaks down remains one of the central challenges of modern condensed matter physics.
