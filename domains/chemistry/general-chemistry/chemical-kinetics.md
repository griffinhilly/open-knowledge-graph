---
id: chemical-kinetics
title: Chemical Kinetics
domain: chemistry
course: general-chemistry
prerequisites:
- id: stoichiometry-calculations
  type: soft
- id: chemical-equilibrium
  type: soft
- id: derivative-as-slope-of-tangent
  type: soft
- id: natural-logarithm-and-e
  type: soft
- id: differential-equations-intro
  type: soft
- id: exponential-growth-and-decay
  type: hard
- id: exponential-functions-and-graphs
  type: soft
builds-toward:
- arrhenius-equation
tags:
- reaction-rate
- rate-law
- rate-constant
- reaction-order
- half-life
- integrated-rate-law
stage: formal-systems
status: validated
---

# Chemical Kinetics

## Core Idea
Chemical kinetics studies how fast reactions proceed and what factors control reaction rates. The rate law — rate = k[A]ⁿ[B]ᵐ — expresses rate as a function of reactant concentrations with experimentally determined orders (n, m) and a temperature-dependent rate constant k. Reaction order must be determined from experimental data, not inferred from stoichiometric coefficients (except for elementary steps). The half-life of a first-order reaction, t₁/₂ = ln(2)/k, is constant and independent of initial concentration — a key diagnostic.

## How It's Best Learned
Determine rate laws from initial rate experiments by comparing pairs of experiments where one concentration is varied while others are held constant. Practice integrated rate laws by plotting concentration data three ways (ln[A] vs. t, 1/[A] vs. t, [A] vs. t) and identifying which is linear to determine reaction order.

## Common Misconceptions
- Reaction order cannot be read from the balanced equation — it must be measured experimentally. The equation 2NO₂ → 2NO + O₂ is not necessarily second order in NO₂.
- A thermodynamically favorable reaction (large K, negative ΔG) can still be extremely slow if the activation energy is high — kinetics and thermodynamics are independent.

## Questions

```yaml
- question: "For the reaction 2NO(g) + O₂(g) → 2NO₂(g), an experiment finds the rate law is rate = k[NO]²[O₂]. What can you conclude?"
  type: multiple-choice
  options: ["The reaction proceeds in a single elementary step because the rate law matches the stoichiometry", "The reaction order was determined experimentally; the mechanism may involve multiple steps", "The rate constant k has units of M⁻¹s⁻¹ for this reaction", "The reaction is first order overall"]
  answer: 1
  explanation: "Rate laws must be determined experimentally. Even when exponents match stoichiometric coefficients — as they happen to here — you cannot conclude the reaction is a single elementary step. The mechanism may be more complex, and this must be verified separately. Option C is also wrong: for this third-order reaction, k has units of M⁻²s⁻¹. Option D is wrong; the overall order is 2 + 1 = 3."

- question: "For a first-order reaction, the half-life is the same regardless of the initial concentration of the reactant."
  type: true-false
  answer: true
  explanation: "For a first-order reaction, t₁/₂ = ln(2)/k. Since k is a constant at a given temperature, the half-life is fixed — independent of [A]₀. This is a diagnostic: if the half-life remains constant as the reaction proceeds, the reaction is first-order. By contrast, for a second-order reaction t₁/₂ = 1/(k[A]₀), so successive half-lives get longer as the reactant is consumed."

- question: "A reaction has a large negative ΔG (very thermodynamically favorable) but proceeds imperceptibly slowly at room temperature. How is this possible?"
  type: short-answer
  answer: "ΔG determines thermodynamic spontaneity — whether the reaction is energetically downhill — but says nothing about the rate. Rate depends on the activation energy Ea, the energy barrier reactants must surmount to reach the transition state. A reaction can be thermodynamically favorable but kinetically blocked by a high activation energy barrier. Thermodynamics governs where a reaction goes; kinetics governs how fast it gets there."
  explanation: "Diamond converting to graphite is thermodynamically spontaneous but kinetically inert at room temperature because the activation energy is enormous. Catalysts lower Ea without changing ΔG — they accelerate the approach to equilibrium without changing where equilibrium lies. This separation between thermodynamic and kinetic control is one of the most important conceptual distinctions in chemistry."
```

## Explainer

Chemical equilibrium tells you where a reaction ends up; chemical kinetics tells you how fast it gets there. These are completely independent. A reaction can have a large negative ΔG — strongly thermodynamically favored — yet proceed so slowly at room temperature that it is practically inert. Diamond converting to graphite is the paradigmatic example: thermodynamically spontaneous, but it essentially never happens because the activation energy barrier is enormous. Kinetics and thermodynamics must both be understood to predict what will actually happen in a chemical system.

The rate law, rate = k[A]ⁿ[B]ᵐ, summarizes how reaction rate depends on concentrations. The exponents n and m are the reaction orders with respect to each reactant; the sum n + m is the overall order. These exponents must be determined experimentally by measuring how rate changes when concentrations are varied one at a time. They cannot be read from the balanced equation — stoichiometric coefficients and rate law exponents are unrelated for multistep mechanisms. The rate constant k encodes temperature dependence and has units that depend on the overall order.

The integrated rate laws link the rate law to observable concentration changes over time. For a first-order reaction, [A] decays exponentially: [A] = [A]₀ e^(−kt), and a plot of ln[A] versus t is linear with slope −k. For a second-order reaction, 1/[A] versus t is linear. For zero-order, [A] versus t is linear. This graphical diagnostic — testing all three plots to see which one is linear — is how reaction order is determined from concentration-time data in practice.

The half-life is a useful shorthand for how quickly a reaction proceeds. For first-order reactions, t₁/₂ = ln(2)/k is constant regardless of the starting concentration — each successive half-life removes exactly half of what remains. This constant half-life is the diagnostic signature of first-order kinetics and underlies all of radioactive decay. For second-order reactions, t₁/₂ = 1/(k[A]₀) depends on the initial concentration, so half-lives lengthen as the reaction proceeds.

Temperature has a profound effect on rate through its influence on k. The Arrhenius equation — the next topic — quantifies this: k = A e^(−Ea/RT). A catalyst works by providing an alternative reaction pathway with lower activation energy Ea, which exponentially increases k at a given temperature. Crucially, the catalyst lowers the energy barrier for both the forward and reverse reactions equally, so the equilibrium constant (and ΔG) is unchanged — the reaction reaches the same equilibrium, just faster.
