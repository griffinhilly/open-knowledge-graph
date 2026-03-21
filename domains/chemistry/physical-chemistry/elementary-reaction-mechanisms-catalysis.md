---
id: elementary-reaction-mechanisms-catalysis
title: Elementary Reaction Mechanisms and Catalysis
domain: chemistry
course: physical-chemistry
prerequisites:
- id: reaction-mechanisms-overview
  type: hard
- id: activation-energy-catalysis-reaction-pathways
  type: hard
builds-toward:
- transition-state-theory-and-kinetics
tags:
- kinetics
- mechanisms
- catalysis
- elementary-steps
stage: advanced
status: draft
---

# Elementary Reaction Mechanisms and Catalysis

## Core Idea
Complex reactions proceed through sequences of elementary steps (unimolecular or bimolecular), each with its own rate constant and activation energy. Rate laws are derived from mechanisms via steady-state or pre-equilibrium approximations. Catalysts lower activation energy by providing alternative paths; enzyme kinetics (Michaelis-Menten), homogeneous catalysis, and heterogeneous catalysis all obey mechanistic principles.

## Questions

```yaml
- question: "A proposed mechanism has two steps: Step 1 (fast, reversible): A + B ⇌ X, and Step 2 (slow): X → C. What is the rate law for the overall reaction?"
  type: multiple-choice
  options:
    - "rate = k[X]"
    - "rate = k[A][B]"
    - "rate = k[A]"
    - "rate = k[A][B][C]"
  answer: 1
  explanation: "Step 2 is the rate-determining step, so rate = k₂[X]. But X is an intermediate — it cannot appear in the observable rate law. Using the pre-equilibrium approximation (Step 1 is fast and reversible), K_eq = [X]/([A][B]), so [X] = K_eq[A][B]. Substituting gives rate = k₂·K_eq·[A][B] = k_obs[A][B]. Option A is wrong because rate laws must be expressed in terms of reactants, not intermediates."

- question: "A catalyst doubles the rate of the forward reaction. What happens to the rate of the reverse reaction?"
  type: multiple-choice
  options:
    - "It stays the same — the catalyst only speeds up the forward direction"
    - "It doubles — the catalyst lowers the activation energy for both directions equally"
    - "It decreases — the catalyst shifts equilibrium toward products"
    - "It increases by more than double — the reverse reaction benefits more from the lowered barrier"
  answer: 1
  explanation: "A catalyst provides an alternative mechanism with a lower activation energy. Because the energy difference between reactants and products (ΔG°) is unchanged, lowering the forward barrier by a given amount lowers the reverse barrier by the same amount. Both rate constants increase by the same factor, leaving the equilibrium constant K = k_f/k_r unchanged. Catalysts change kinetics, never thermodynamics."

- question: "A catalyst can make a thermodynamically unfavorable reaction proceed by lowering the activation energy sufficiently."
  type: true-false
  answer: false
  explanation: "Activation energy determines the rate of a reaction, not whether it is thermodynamically favorable. A catalyst cannot change the Gibbs energy difference between reactants and products (ΔG°), and therefore cannot change the equilibrium constant. If a reaction is thermodynamically unfavorable (ΔG° > 0), it will still favor reactants at equilibrium regardless of the catalyst — it just reaches that equilibrium faster."

- question: "For an elementary reaction step, you can always write the rate law directly from the balanced stoichiometric equation for that step."
  type: true-false
  answer: true
  explanation: "This is the defining property of an elementary step: it occurs in a single molecular event, so the rate law must reflect the actual collision or decomposition. A bimolecular elementary step A + B → products has rate = k[A][B] by definition. This is NOT true for overall (non-elementary) reactions, whose rate laws must be determined experimentally and can have fractional or unexpected orders."

- question: "Why must the rate law for an overall reaction exclude intermediates, and how do chemists eliminate them?"
  type: short-answer
  answer: "Intermediates are transient species that cannot be measured or controlled by the experimenter. To eliminate them, chemists use either the steady-state approximation (set d[intermediate]/dt = 0, since it is consumed as fast as it is formed) or the pre-equilibrium approximation (a fast reversible step establishes an equilibrium before the slow step, allowing expression of [intermediate] in terms of reactant concentrations via the equilibrium constant). Both techniques yield an observable rate law in terms of measurable quantities."
  explanation: "The practical need is measurement: you can only measure and control concentrations of stable reactants, not fleeting intermediates. The steady-state applies when the intermediate's rate of formation is slow relative to its consumption; the pre-equilibrium applies when the fast step truly equilibrates before the slow step proceeds. In either case, the goal is an observable rate law expressed in measurable quantities."
```

## Explainer

You know from your study of reaction mechanisms that overall balanced equations often hide a sequence of simpler steps, and from activation energy concepts that every reaction must cross an energy barrier to proceed. Here we bring those ideas together: every complex reaction is a sequence of **elementary steps**, each involving one molecule (unimolecular) or two molecules (bimolecular) colliding and reacting in a single event. The crucial feature of elementary steps is that their rate laws can be written directly from stoichiometry — a bimolecular elementary step A + B → products has rate = k[A][B], no exceptions. This is not true for overall reactions, which is precisely why we decompose them into elementary steps.

When a mechanism has multiple steps, one is typically the **rate-determining step** — the slowest step that acts as a bottleneck for the overall reaction. The observed rate law reflects this bottleneck. But extracting the rate law from a proposed mechanism requires careful reasoning. The **steady-state approximation** assumes that reactive intermediates (species that form and are consumed during the reaction but do not appear in the overall equation) reach a constant, low concentration quickly, so their rate of formation equals their rate of consumption. The **pre-equilibrium approximation** applies when a fast, reversible step precedes the slow step — the fast step reaches equilibrium, and you can use the equilibrium constant to express intermediate concentrations in terms of reactant concentrations. Both techniques let you eliminate intermediate concentrations from the rate law and express it purely in terms of observable species.

**Catalysts** accelerate reactions by providing an alternative mechanism with a lower activation energy for the rate-determining step. They participate in the mechanism — forming intermediates, appearing in elementary steps — but are regenerated by the end of the catalytic cycle, so they do not appear in the overall stoichiometry. In **homogeneous catalysis**, the catalyst is in the same phase as the reactants (like acid catalysis in solution). In **heterogeneous catalysis**, the catalyst is typically a solid surface where reactants adsorb, react, and desorb — the elementary steps are adsorption, surface reaction, and desorption, and the rate often depends on surface coverage.

The unifying principle is that catalysis does not change thermodynamics — it cannot make an unfavorable reaction favorable or shift the equilibrium position. It only changes kinetics by lowering the barrier. A catalyst that lowers the forward activation energy by the same amount lowers the reverse barrier too, so both forward and reverse rates increase equally. This is why catalysts speed up the approach to equilibrium without changing where that equilibrium lies. Understanding this distinction between kinetic and thermodynamic control is essential for designing catalytic systems, whether industrial (Haber process for ammonia) or biological (enzyme catalysis).
