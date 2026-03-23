---
id: integrated-rate-laws
title: Integrated Rate Laws
domain: chemistry
course: general-chemistry
prerequisites:
- id: chemical-kinetics
  type: hard
- id: exponential-functions-and-graphs
  type: soft
- id: antiderivatives
  type: soft
- id: differential-equations-intro
  type: soft
builds-toward:
- arrhenius-equation
tags:
- zero-order
- first-order
- second-order
- half-life
- integrated-rate-law
- graphical-method
- concentration-vs-time
stage: formal-systems
status: validated
---
# Integrated Rate Laws

## Core Idea
Integrated rate laws relate concentration to time, enabling prediction of how much reactant remains after a given period. For a reaction A → products: zero order gives [A] = [A]₀ − kt (linear in [A] vs t); first order gives ln[A] = ln[A]₀ − kt (linear in ln[A] vs t, half-life t₁/₂ = 0.693/k); second order gives 1/[A] = 1/[A]₀ + kt (linear in 1/[A] vs t). The graphical method determines order experimentally: plot [A], ln[A], and 1/[A] against time, and whichever gives a straight line reveals the order. Half-life for first-order reactions is uniquely concentration-independent.

## How It's Best Learned
Memorize the three integrated forms and their corresponding straight-line plots. Practice determining order from graphical data — the linear plot identifies the order, the slope gives k (with appropriate sign). Work half-life problems for each order and notice how only first-order half-life is constant (radioactive decay is the classic example).

## Common Misconceptions
- Half-life is constant only for first-order reactions. For zero-order reactions, half-life decreases as concentration drops; for second-order, half-life increases as concentration drops.
- The integrated rate law describes concentration change over time for a single reactant. For reactions with multiple reactants, the pseudo-first-order approach (flooding one reactant in excess) is needed to isolate the dependence on one concentration.

## Questions

```yaml
- question: "A medication is eliminated from the body with a constant half-life of 6 hours. A patient takes a 400 mg dose. How much remains after 18 hours, and what does the constant half-life reveal about the elimination kinetics?"
  type: multiple-choice
  options:
    - "200 mg; a constant half-life indicates zero-order elimination at a fixed rate"
    - "50 mg; a half-life that is constant regardless of dose indicates first-order elimination kinetics"
    - "0 mg; all drug is eliminated exactly by the third half-life"
    - "100 mg; successive half-lives are additive, so 18 hours leaves 25% of the dose"
  answer: 1
  explanation: "After 18 hours (3 half-lives): 400 → 200 → 100 → 50 mg. A half-life that remains constant regardless of how much drug remains is the definitive signature of first-order kinetics. In first-order elimination, rate is proportional to concentration (rate = k[drug]), so the same fraction (50%) is eliminated per half-life regardless of starting amount. Zero-order elimination proceeds at a fixed mg/hour regardless of concentration, so its half-life depends on starting dose and shortens over time. Option C is wrong — exponential decay approaches but never mathematically reaches zero."

- question: "A chemist measures the concentration of reactant A over time and plots [A] vs. t, ln[A] vs. t, and 1/[A] vs. t. Only the 1/[A] vs. t plot is a straight line. What can she conclude?"
  type: multiple-choice
  options:
    - "The reaction is first-order; k equals the negative of the slope of the 1/[A] plot"
    - "The reaction is zero-order; k equals the slope of the 1/[A] plot"
    - "The reaction is second-order; k equals the slope of the 1/[A] vs. t line"
    - "No conclusion is possible from graphical methods alone — a kinetic model must be assumed first"
  answer: 2
  explanation: "This is exactly the graphical method in action. The integrated rate law for second-order kinetics is 1/[A] = 1/[A]₀ + kt — a linear equation in 1/[A] with slope +k (positive). If [A] vs. t were linear, the reaction would be zero-order (slope = −k). If ln[A] vs. t were linear, it would be first-order (slope = −k). Whichever linearization gives a straight line reveals the order, and the slope directly gives k. Option D is wrong — this graphical method IS the standard experimental approach to determining reaction order, requiring no prior assumption."

- question: "For a zero-order reaction, successive half-lives are all equal, because the constant reaction rate ensures that the same fraction of reactant is consumed in each time interval."
  type: true-false
  answer: false
  explanation: "Constant half-lives are the exclusive property of first-order reactions, not zero-order. For a zero-order reaction, rate = k (constant, independent of concentration), so a fixed amount of reactant depletes per unit time — not a fixed fraction. The half-life is t₁/₂ = [A]₀/2k, which depends on starting concentration, so each successive half-life is shorter (each 'half' starts with less material, and a constant rate depletes it faster). Only first-order kinetics produce a concentration-independent half-life."

- question: "The first-order integrated rate law predicts that reactant concentration decays exponentially and theoretically never reaches exactly zero at any finite time."
  type: true-false
  answer: true
  explanation: "First-order integrated rate law: [A] = [A]₀e⁻ᵏᵗ. Since e⁻ᵏᵗ > 0 for all finite t, the concentration asymptotically approaches zero without ever reaching it — this is the mathematical nature of exponential decay. Each half-life halves the remaining amount, but halving a positive number always leaves a positive number. In practice, once concentrations fall below detection limits we say the reaction is 'complete,' but mathematically the curve approaches the axis asymptotically. Radioactive decay follows the same mathematics for the same reason."

- question: "Explain why the constant half-life property is unique to first-order reactions and does not hold for zero-order or second-order reactions."
  type: short-answer
  answer: "For a first-order reaction, rate = k[A], so the rate decreases proportionally as concentration decreases. The fraction consumed per unit time remains constant, and the half-life t₁/₂ = 0.693/k contains no concentration term — it is independent of how much reactant remains. For zero-order reactions, rate = k (constant amount depleted per time), so the time to consume half the remaining material shortens as less material is present — half-lives decrease. For second-order reactions, rate = k[A]², so the rate drops dramatically as [A] falls and successive half-lives grow longer."
  explanation: "The mathematical signature is in the integrated forms. Only first-order [A] = [A]₀e⁻ᵏᵗ produces a t₁/₂ formula (0.693/k) with no [A]₀ term. Zero-order: t₁/₂ = [A]₀/2k (shorter each half-life). Second-order: t₁/₂ = 1/(k[A]₀) (longer each half-life). This distinction has clinical relevance: drugs following first-order kinetics (most common) reach steady-state in a predictable number of half-lives regardless of dose, while zero-order drugs (like alcohol at saturation of alcohol dehydrogenase) have dose-dependent kinetics that can lead to dangerous accumulation."
```

## Explainer

From chemical kinetics, you know that rate laws express how reaction speed depends on concentration: rate = k[A]ⁿ, where n is the reaction order. But rate laws in that form tell you the instantaneous speed at a given moment — they don't directly answer the practical question "how much reactant is left after 30 minutes?" That's what **integrated rate laws** answer. They are the mathematical result of integrating the differential rate law over time, converting a statement about speed into a statement about concentration as a function of time.

For a **zero-order** reaction (rate = k, independent of concentration), integration gives [A] = [A]₀ − kt. Concentration decreases linearly with time, like a faucet draining at a constant rate regardless of how much water remains. The half-life is t₁/₂ = [A]₀/2k — it depends on starting concentration, so each successive half-life is shorter. For a **first-order** reaction (rate = k[A]), integration gives ln[A] = ln[A]₀ − kt, or equivalently [A] = [A]₀e⁻ᵏᵗ. This is exponential decay — the same mathematics that governs radioactive decay, which is why radioactive half-life is constant: t₁/₂ = 0.693/k, independent of how much material remains. For a **second-order** reaction (rate = k[A]²), integration gives 1/[A] = 1/[A]₀ + kt. The reaction slows dramatically as concentration drops, and the half-life t₁/₂ = 1/(k[A]₀) increases with each successive halving.

The **graphical method** is the experimental technique for determining reaction order. You measure concentration at several time points, then make three plots: [A] vs t, ln[A] vs t, and 1/[A] vs t. Whichever plot gives a straight line reveals the order — linear in [A] means zero-order, linear in ln[A] means first-order, linear in 1/[A] means second-order. The slope of the straight-line plot gives you the rate constant k (negative slope for zero and first order, positive for second order). This is why the integrated rate laws are written in y = mx + b form: they are designed to be linearized for graphical analysis.

A practical detail worth internalizing: first-order kinetics are by far the most common in chemistry and biology. Drug metabolism, radioactive decay, and many decomposition reactions follow first-order kinetics. The constant half-life property makes first-order processes especially intuitive — if a drug's half-life is 4 hours, then after 4 hours half remains, after 8 hours a quarter remains, after 12 hours an eighth remains, regardless of the initial dose. When a reaction involves multiple reactants, the **pseudo-first-order** technique simplifies analysis: flood one reactant in large excess so its concentration barely changes, and the rate law reduces to a first-order dependence on the other reactant.
