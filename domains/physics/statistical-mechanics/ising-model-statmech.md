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
stage: expert
status: draft
---

# The Ising Model and Magnetic Transitions

## Core Idea
The Ising model represents a magnetic system as a lattice of spins σ_i = ±1 coupled by nearest-neighbor interactions. The Hamiltonian is H = -J Σ σ_i σ_j - h Σ σ_i. It exhibits a ferromagnetic phase transition at T_c in d ≥ 2. The 2D Ising model is exactly solvable (Onsager); in higher dimensions, it reveals universal critical behavior.

## Questions

```yaml
- question: "The 1D Ising chain has no ferromagnetic phase transition at any finite temperature, while the 2D Ising model does. What is the fundamental physical reason for this difference?"
  type: multiple-choice
  options:
    - "The 2D lattice has more sites, allowing longer-range correlations to develop and stabilize order"
    - "Domain walls in 1D are single broken bonds (low energy, no entropy gain), so thermal fluctuations always proliferate them; in 2D, domain walls are extended line objects whose energy grows with length, making them costly enough to suppress at low T"
    - "The coupling constant J has a different sign in 1D versus 2D models"
    - "The 2D model has an external field h that stabilizes the ordered phase"
  answer: 1
  explanation: "The 1D argument: a domain wall between an up-region and a down-region costs energy 2J but gains entropy k ln N (it can be placed anywhere along the chain). For any T > 0 and large N, the free energy gain from entropy exceeds the energy cost — domain walls proliferate and destroy long-range order. In 2D, a domain wall is a closed loop whose energy scales with its perimeter, making it much more costly to create. Below T_c, this energy cost suppresses domain walls; above T_c, entropy wins. This is a dimension-dependent balance, not a difference in model parameters."

- question: "Mean-field theory applied to the Ising model correctly predicts a ferromagnetic transition and that magnetization vanishes continuously at T_c, but gives the wrong critical exponent β = 1/2 instead of β = 1/8 (2D). Why?"
  type: multiple-choice
  options:
    - "Mean-field theory uses an approximate partition function that omits nearest-neighbor pairs"
    - "Mean-field theory replaces neighbors' spins with their average value, suppressing fluctuations that are actually large near T_c — the approximation fails worst where it matters most"
    - "Mean-field theory only applies to models without an external field h, introducing systematic error"
    - "Mean-field theory assumes a square lattice, which does not match the hexagonal structure of the 2D Ising model"
  answer: 1
  explanation: "Mean-field theory's key approximation is replacing σ_j with its mean ⟨σ_j⟩ = m, eliminating correlations between neighboring spins. Near T_c, fluctuations are actually enormous — the correlation length diverges — so the assumption that neighbors look like their average is maximally wrong exactly at the critical point. In high dimensions (d > 4, the upper critical dimension), fluctuations become small and mean-field exponents become exact. In 2D they fail badly, giving β = 1/2 versus the exact β = 1/8."

- question: "In the Ising model with J > 0, the ferromagnetic phase at low temperature exists simply because energy always wins over entropy."
  type: true-false
  answer: false
  explanation: "Energy wins over entropy only below T_c. Above T_c, entropy dominates and the system is disordered (m = 0). The phase transition is precisely the temperature at which these competing tendencies balance. Saying 'energy always wins when J > 0' ignores the temperature-dependence of the free energy: at high T, the entropy of disordered configurations (which vastly outnumber ordered ones) overwhelms the energy benefit of alignment."

- question: "The partition function Z of an N-spin Ising model contains exactly 2^N terms, because each spin independently takes one of two values."
  type: true-false
  answer: true
  explanation: "Z = Σ_{all configs} exp(−βH), where the sum runs over all possible assignments of ±1 to each of the N spins. Since each spin has 2 choices and the choices are independent, there are exactly 2^N configurations. For macroscopic N (~10^23), this sum is astronomically large — which is why direct computation is impossible and techniques like the transfer matrix method, mean-field approximation, or Monte Carlo simulation are needed."

- question: "Explain in terms of energy-entropy competition why the Ising model has a ferromagnetic phase transition at a finite critical temperature T_c (in d ≥ 2)."
  type: short-answer
  answer: "At low temperature, the Boltzmann factor strongly weights low-energy (aligned) configurations, so the system orders: spins align, m ≠ 0. At high temperature, the entropy of the vast number of disordered configurations overwhelms the energy benefit of alignment, so m = 0. There is a critical temperature T_c at which these tendencies balance — below it, order is thermodynamically stable; above it, disorder is. This competition is encoded in the free energy F = E − TS: at low T, minimizing E dominates; at high T, maximizing S dominates."
  explanation: "The entropy argument is quantitative: there are vastly more disordered configurations than ordered ones (one perfectly aligned state vs. 2^N − 2 others). Only the energy penalty J for misaligned neighbors keeps order stable at low T. The transition at T_c is where the free energy first prefers disorder — a collective phenomenon that requires d ≥ 2 for the energetic cost of disorder (domain walls) to be large enough to sustain an ordered phase."
```

## Explainer

The Ising model is the simplest possible model of a magnetic material that still captures a phase transition. Each site i on a lattice carries a spin variable σ_i that can take only two values: +1 (up) or −1 (down). The total energy is H = −J Σ_{⟨ij⟩} σ_i σ_j − h Σ_i σ_i, where the first sum runs over nearest-neighbor pairs and J > 0 favors alignment (ferromagnetism). The model discards almost everything real about electrons — continuous position, orbital motion, long-range interactions — and keeps only the binary choice and nearest-neighbor coupling. The remarkable fact is that this caricature still exhibits a genuine phase transition.

To connect to the canonical ensemble you already know: the partition function is Z = Σ_{all spin configs} exp(−βH), where the sum runs over all 2^N configurations of N spins. From Z you can compute every thermodynamic quantity — free energy F = −kT ln Z, magnetization m = (1/N)⟨Σ_i σ_i⟩, susceptibility χ = ∂m/∂h, and specific heat. The challenge is that this sum has 2^N terms, which is astronomically large for any macroscopic system. The competition between energy (J favors alignment) and entropy (many disordered configurations) determines the equilibrium state at each temperature. Low T: energy wins, all spins align, m ≠ 0. High T: entropy wins, spins are random, m = 0. The critical temperature T_c separates these phases.

In one dimension, the Ising model has no phase transition at T > 0 — thermal fluctuations always destroy order. The intuitive reason: a single domain wall between an up-region and a down-region costs energy 2J but gains entropy k ln N (since it can be placed anywhere), so for any T > 0 and large N, domain walls proliferate and destroy order. In **two dimensions**, the balance shifts: domain walls are not single bonds but extended objects whose energy scales with their length, so they cost enough energy to be suppressed at low T. Onsager's 1944 exact solution showed that the 2D Ising model has a sharp transition at kT_c = 2J/ln(1+√2) ≈ 2.269 J. Above T_c, m = 0; below T_c, m ≠ 0. The specific heat diverges logarithmically at T_c — the first exact confirmation that critical behavior involves divergences.

The **mean-field approximation** offers a simpler route to understanding the transition, at the cost of accuracy near T_c. In mean-field theory, you replace the neighbors' spins with their average: σ_j → ⟨σ_j⟩ = m. Then each spin sees an effective field h_eff = Jzm + h, where z is the number of nearest neighbors. The self-consistency equation becomes m = tanh(β(Jzm + h)), a transcendental equation that has m = 0 as its only solution for T > T_c^{MF} = Jz/k, but develops two nonzero solutions (±m_0) for T < T_c^{MF}. Mean-field theory gets the qualitative picture right — there is a transition, m vanishes continuously at T_c, and the susceptibility diverges — but predicts wrong critical exponents (β = 1/2, γ = 1) compared to the exact 2D values (β = 1/8, γ = 7/4). The discrepancy is largest in low dimensions where fluctuations are strongest, exactly where mean-field's assumption that all neighbors look like their average fails most badly.
