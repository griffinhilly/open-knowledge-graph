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
stage: expert
status: validated
---

# Spin Glasses and Quenched Disorder

## Core Idea
Spin glasses are disordered magnetic systems where competing interactions create frustration, leading to a complex energy landscape with many local minima. They exhibit ergodicity breaking, slow relaxation, memory effects, and remain disordered even at zero temperature with only short-range correlations.

## Questions

```yaml
- question: "A physicist argues that a spin glass, like a paramagnet, shows no net magnetization, so it must be a special case of the paramagnetic phase. What is wrong with this argument?"
  type: multiple-choice
  options:
    - "Spin glasses do have net magnetization — the Edwards-Anderson parameter is a form of long-range order"
    - "The physicist is correct: any magnetic system without long-range order is by definition paramagnetic"
    - "Although the disorder-averaged magnetization is zero, individual spins in a spin glass freeze into fixed orientations, making the system non-ergodic and producing aging, memory effects, and history-dependence that a paramagnet never exhibits"
    - "Spin glasses are actually frozen ferromagnets — their net magnetization is non-zero when measured in the right reference frame"
  answer: 2
  explanation: "The absence of net magnetization is shared by paramagnets and spin glasses but arises for completely different reasons. A paramagnet has spins that fluctuate rapidly and average to zero — it is fully ergodic and thermalizes quickly. A spin glass has spins that freeze into fixed random orientations: ⟨σᵢ⟩ ≠ 0 for each individual site, but those frozen directions are random across sites, so the spatial average is zero. The spin glass is non-ergodic: it breaks ergodicity below Tg, shows memory effects (its frozen state remembers the cooling field), and exhibits slow aging relaxation. These are thermodynamic signatures of a distinct phase, not a variant of paramagnetism."

- question: "What is the crucial distinction between quenched and annealed disorder, and why does this distinction determine whether a spin glass phase can form?"
  type: multiple-choice
  options:
    - "Quenched disorder means strong random couplings; annealed disorder means weak ones"
    - "Annealed disorder creates frustration; quenched disorder creates long-range ferromagnetic order"
    - "The distinction is thermodynamic: quenched systems are at low temperature, annealed systems are at high temperature"
    - "Quenched disorder is frozen — random couplings are locked in by the material's structure and do not equilibrate with temperature. Annealed disorder thermalizes and averages out. Frozen couplings create static frustration and a rugged energy landscape; if they could equilibrate, the system would not get trapped in local minima"
  answer: 3
  explanation: "In a spin glass, the random couplings Jᵢⱼ were frozen in when the material was formed (by rapid cooling or impurity substitution). The spins can fluctuate with temperature; the couplings cannot. This is quenched disorder. The key consequence: the frustration is static and permanent — no thermal fluctuation can reorganize the coupling network to reduce frustration. If the couplings could thermalize (annealed disorder), they would average out over time and the system would not generate a rugged energy landscape. Quenched disorder is what makes the system permanently frustrated and creates the exponentially large number of nearly-degenerate local minima that defines the spin glass phase."

- question: "A spin glass is essentially a frozen ferromagnet: like a ferromagnet cooled below its Curie temperature, it settles into a single preferred low-energy configuration with frozen spins."
  type: true-false
  answer: false
  explanation: "False. A ferromagnet below Tc has a unique ordered ground state (all or most spins aligned), characterized by non-zero net magnetization and conventional long-range order. A spin glass below Tg freezes into one of an exponentially large number of nearly-degenerate local minima — and which minimum it occupies depends on its thermal history (how it was cooled). Different cooling protocols land in different frozen states. Individual spins have non-zero local averages ⟨σᵢ⟩ ≠ 0, but those values are random across sites with no global alignment. The spin glass has no conventional long-range order and no macroscopic magnetization. The Edwards-Anderson order parameter qEA captures this local freezing without global order — something a ferromagnetic description entirely misses."

- question: "Frustration in a spin glass arises because frozen random couplings (some ferromagnetic, some antiferromagnetic) make it impossible for any single spin configuration to simultaneously satisfy all interactions, leading to many nearly degenerate local minima."
  type: true-false
  answer: true
  explanation: "True. The simple example is three spins on a triangle with antiferromagnetic couplings: any two spins can be anti-aligned (satisfying their bond), but the third spin cannot simultaneously anti-align with both of them. Whatever direction it takes, one bond is unsatisfied — this is a frustrated plaquette. In a macroscopic spin glass with random ferromagnetic and antiferromagnetic couplings throughout the lattice, frustration is pervasive: there is no ground state that satisfies all bonds. The result is an energy landscape with an exponentially large number of local minima all sitting at nearly the same energy, which is what produces the complex dynamical behavior (ergodicity breaking, aging, memory effects) characteristic of spin glasses."

- question: "Explain why a spin glass cannot be described as simply a paramagnet or ferromagnet, using the concept of the Edwards-Anderson order parameter."
  type: short-answer
  answer: "A paramagnet has ⟨σᵢ⟩ = 0 at every site, is fully ergodic, and thermalizes rapidly — the Edwards-Anderson parameter qEA = [⟨σᵢ⟩²]_disorder = 0. A ferromagnet has all spins aligned: both the net magnetization ⟨σᵢ⟩ (averaged over sites) and qEA are non-zero. A spin glass occupies a distinct third phase: each spin freezes into a definite direction (⟨σᵢ⟩ ≠ 0 per site), so qEA = [⟨σᵢ⟩²]_disorder > 0, signaling local freezing. But the frozen directions are random across sites, so the site-averaged magnetization is zero — no conventional long-range order. The system is non-ergodic: it cannot explore all low-energy configurations, so time averages differ from ensemble averages. qEA is non-zero in the spin glass phase and zero in both the paramagnetic and (trivially, in the opposite sense) ferromagnetic descriptions, making it the correct order parameter to distinguish the spin glass from both."
  explanation: "The Edwards-Anderson parameter is the key conceptual advance: it measures frozen local order without requiring global order. This decoupling — local freezing with global disorder — is what makes spin glasses a distinct thermodynamic phase and a paradigm for systems with complex rugged energy landscapes."
```

## Explainer

The Ising model you know assigns each spin an interaction Jᵢⱼ with its neighbors, where J > 0 favors alignment (ferromagnet) and J < 0 favors anti-alignment (antiferromagnet). In a **spin glass**, the couplings Jᵢⱼ are random — some positive, some negative — frozen in place by the structural disorder of the material. "Frozen" is the key word: **quenched disorder** means the randomness is static, locked into the system as it was formed (by rapid cooling or impurity substitution), not averaging out over time like thermal fluctuations. The spins can fluctuate; the couplings cannot. This distinction between annealed disorder (which thermalizes) and quenched disorder (which does not) is fundamental to the physics.

Frozen random couplings create **frustration**: a condition where no single spin configuration can simultaneously satisfy all interactions. Imagine three spins on a triangle with all antiferromagnetic couplings. Any two-spin pair would prefer to be anti-aligned, but you cannot have all three pairs anti-aligned simultaneously. If spin 1 is up and spin 2 is down, both are satisfied with each other — but they disagree about what spin 3 should be. The triangle is frustrated: whichever direction spin 3 points, at least one bond is unsatisfied. In a macroscopic spin glass, frustration is pervasive throughout the lattice, creating an **energy landscape** with an exponentially large number of local minima all lying at nearly the same energy. The system cannot easily find a global minimum — it gets trapped in whichever local minimum it falls into during cooling.

The phenomenological signatures of spin glasses reflect this landscape complexity. When cooled below the **glass transition temperature** Tg, the system freezes into one local minimum that depends on its thermal history — different cooling protocols land in different minima. This is **ergodicity breaking**: the time average no longer equals the ensemble average because the system cannot explore all of its accessible low-energy configurations in any reasonable time. The system also shows **memory effects**: its frozen configuration retains information about the magnetic field that was applied during cooling. It exhibits slow, non-exponential (**aging**) relaxation — even thousands of seconds after cooling, the magnetization continues to drift as the system explores nearby configurations in its rugged landscape. All of these behaviors contrast sharply with a ferromagnet, which has a single ordered minimum, and a paramagnet, which thermalizes quickly.

Unlike ferromagnets (long-range order) or paramagnets (disordered but ergodic), spin glasses occupy a distinct thermodynamic phase. Individual spins freeze in fixed directions — ⟨σᵢ⟩ ≠ 0 for each site — but those directions are random and different at each site, so ⟨σᵢ⟩ averaged over disorder realizations is zero: there is no conventional long-range order. The correct order parameter for the spin glass phase is the **Edwards-Anderson parameter** qEA = [⟨σᵢ⟩²]_disorder: it measures whether spins freeze locally even though the frozen directions are globally random. A non-zero qEA signals the spin glass phase. This subtle order parameter — frozen local moments without global magnetic order — makes spin glasses a paradigm for systems with complex energy landscapes, with applications extending from structural glasses and protein folding to combinatorial optimization and neural network models.
