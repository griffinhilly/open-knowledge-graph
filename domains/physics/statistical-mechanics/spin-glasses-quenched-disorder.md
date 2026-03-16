---
id: spin-glasses-quenched-disorder
title: Spin Glasses and Quenched Disorder
domain: physics
course: statistical-mechanics
prerequisites:
- id: ising-model-statmech
  type: hard
- id: ergodicity-breaking
  type: soft
tags:
- disorder
- frustration
- glassy
stage: advanced
status: draft
---

# Spin Glasses and Quenched Disorder

## Core Idea
Spin glasses are disordered magnetic systems where competing interactions create frustration, leading to a complex energy landscape with many local minima. They exhibit ergodicity breaking, slow relaxation, memory effects, and remain disordered even at zero temperature with only short-range correlations.

## Explainer

The Ising model you know assigns each spin an interaction Jᵢⱼ with its neighbors, where J > 0 favors alignment (ferromagnet) and J < 0 favors anti-alignment (antiferromagnet). In a **spin glass**, the couplings Jᵢⱼ are random — some positive, some negative — frozen in place by the structural disorder of the material. "Frozen" is the key word: **quenched disorder** means the randomness is static, locked into the system as it was formed (by rapid cooling or impurity substitution), not averaging out over time like thermal fluctuations. The spins can fluctuate; the couplings cannot. This distinction between annealed disorder (which thermalizes) and quenched disorder (which does not) is fundamental to the physics.

Frozen random couplings create **frustration**: a condition where no single spin configuration can simultaneously satisfy all interactions. Imagine three spins on a triangle with all antiferromagnetic couplings. Any two-spin pair would prefer to be anti-aligned, but you cannot have all three pairs anti-aligned simultaneously. If spin 1 is up and spin 2 is down, both are satisfied with each other — but they disagree about what spin 3 should be. The triangle is frustrated: whichever direction spin 3 points, at least one bond is unsatisfied. In a macroscopic spin glass, frustration is pervasive throughout the lattice, creating an **energy landscape** with an exponentially large number of local minima all lying at nearly the same energy. The system cannot easily find a global minimum — it gets trapped in whichever local minimum it falls into during cooling.

The phenomenological signatures of spin glasses reflect this landscape complexity. When cooled below the **glass transition temperature** Tg, the system freezes into one local minimum that depends on its thermal history — different cooling protocols land in different minima. This is **ergodicity breaking**: the time average no longer equals the ensemble average because the system cannot explore all of its accessible low-energy configurations in any reasonable time. The system also shows **memory effects**: its frozen configuration retains information about the magnetic field that was applied during cooling. It exhibits slow, non-exponential (**aging**) relaxation — even thousands of seconds after cooling, the magnetization continues to drift as the system explores nearby configurations in its rugged landscape. All of these behaviors contrast sharply with a ferromagnet, which has a single ordered minimum, and a paramagnet, which thermalizes quickly.

Unlike ferromagnets (long-range order) or paramagnets (disordered but ergodic), spin glasses occupy a distinct thermodynamic phase. Individual spins freeze in fixed directions — ⟨σᵢ⟩ ≠ 0 for each site — but those directions are random and different at each site, so ⟨σᵢ⟩ averaged over disorder realizations is zero: there is no conventional long-range order. The correct order parameter for the spin glass phase is the **Edwards-Anderson parameter** qEA = [⟨σᵢ⟩²]_disorder: it measures whether spins freeze locally even though the frozen directions are globally random. A non-zero qEA signals the spin glass phase. This subtle order parameter — frozen local moments without global magnetic order — makes spin glasses a paradigm for systems with complex energy landscapes, with applications extending from structural glasses and protein folding to combinatorial optimization and neural network models.
