---
id: ising-model-statmech
title: The Ising Model and Magnetic Transitions
domain: physics
course: statistical-mechanics
prerequisites:
- id: canonical-ensemble
  type: hard
- id: phase-transition-equilibrium
  type: soft
builds-toward:
- mean-field-theory-statmech
- monte-carlo-statistical-mechanics
tags:
- ising-model
- magnetism
- phase-transition
stage: advanced
status: draft
---

# The Ising Model and Magnetic Transitions

## Core Idea
The Ising model represents a magnetic system as a lattice of spins σ_i = ±1 coupled by nearest-neighbor interactions. The Hamiltonian is H = -J Σ σ_i σ_j - h Σ σ_i. It exhibits a ferromagnetic phase transition at T_c in d ≥ 2. The 2D Ising model is exactly solvable (Onsager); in higher dimensions, it reveals universal critical behavior.

## Explainer

The Ising model is the simplest possible model of a magnetic material that still captures a phase transition. Each site i on a lattice carries a spin variable σ_i that can take only two values: +1 (up) or −1 (down). The total energy is H = −J Σ_{⟨ij⟩} σ_i σ_j − h Σ_i σ_i, where the first sum runs over nearest-neighbor pairs and J > 0 favors alignment (ferromagnetism). The model discards almost everything real about electrons — continuous position, orbital motion, long-range interactions — and keeps only the binary choice and nearest-neighbor coupling. The remarkable fact is that this caricature still exhibits a genuine phase transition.

To connect to the canonical ensemble you already know: the partition function is Z = Σ_{all spin configs} exp(−βH), where the sum runs over all 2^N configurations of N spins. From Z you can compute every thermodynamic quantity — free energy F = −kT ln Z, magnetization m = (1/N)⟨Σ_i σ_i⟩, susceptibility χ = ∂m/∂h, and specific heat. The challenge is that this sum has 2^N terms, which is astronomically large for any macroscopic system. The competition between energy (J favors alignment) and entropy (many disordered configurations) determines the equilibrium state at each temperature. Low T: energy wins, all spins align, m ≠ 0. High T: entropy wins, spins are random, m = 0. The critical temperature T_c separates these phases.

In one dimension, the Ising model has no phase transition at T > 0 — thermal fluctuations always destroy order. The intuitive reason: a single domain wall between an up-region and a down-region costs energy 2J but gains entropy k ln N (since it can be placed anywhere), so for any T > 0 and large N, domain walls proliferate and destroy order. In **two dimensions**, the balance shifts: domain walls are not single bonds but extended objects whose energy scales with their length, so they cost enough energy to be suppressed at low T. Onsager's 1944 exact solution showed that the 2D Ising model has a sharp transition at kT_c = 2J/ln(1+√2) ≈ 2.269 J. Above T_c, m = 0; below T_c, m ≠ 0. The specific heat diverges logarithmically at T_c — the first exact confirmation that critical behavior involves divergences.

The **mean-field approximation** offers a simpler route to understanding the transition, at the cost of accuracy near T_c. In mean-field theory, you replace the neighbors' spins with their average: σ_j → ⟨σ_j⟩ = m. Then each spin sees an effective field h_eff = Jzm + h, where z is the number of nearest neighbors. The self-consistency equation becomes m = tanh(β(Jzm + h)), a transcendental equation that has m = 0 as its only solution for T > T_c^{MF} = Jz/k, but develops two nonzero solutions (±m_0) for T < T_c^{MF}. Mean-field theory gets the qualitative picture right — there is a transition, m vanishes continuously at T_c, and the susceptibility diverges — but predicts wrong critical exponents (β = 1/2, γ = 1) compared to the exact 2D values (β = 1/8, γ = 7/4). The discrepancy is largest in low dimensions where fluctuations are strongest, exactly where mean-field's assumption that all neighbors look like their average fails most badly.
