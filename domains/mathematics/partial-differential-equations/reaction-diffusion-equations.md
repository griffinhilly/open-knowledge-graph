---
id: reaction-diffusion-equations
title: Reaction-Diffusion Equations
domain: mathematics
course: partial-differential-equations
prerequisites:
- id: parabolic-pde-theory
  type: hard
- id: nonlinear-pdes-introduction
  type: hard
- id: maximum-principles-pdes
  type: soft
tags: [pde, reaction-diffusion, pattern-formation, traveling-wave, turing]
stage: expert
status: validated
---
# Reaction-Diffusion Equations

## Core Idea
Reaction-diffusion equations u_t = DΔu + f(u) combine spatial diffusion with local nonlinear reaction kinetics, modeling phenomena where substances spread and interact: chemical reactions, population dynamics, nerve impulse propagation, and morphogenesis. The interplay between diffusion (which homogenizes) and reaction (which can amplify differences) produces rich behavior including traveling wave fronts (Fisher-KPP equation), Turing patterns (diffusion-driven instability in systems), and blow-up. The mathematical theory draws on parabolic regularity, comparison principles, and dynamical systems methods.

## Questions
```yaml
- question: "The Fisher-KPP equation u_t = u_xx + u(1-u) models:"
  type: multiple-choice
  options:
    - "Spread of an advantageous gene or population invasion with logistic growth"
    - "Heat conduction in a metal bar"
    - "Vibration of a string"
    - "Electrostatic potential"
  answer: 0
  explanation: "Fisher (1937) introduced this equation to model the spatial spread of a favorable allele in a population. The diffusion term u_xx models spatial migration, and u(1-u) is logistic growth. It admits traveling wave solutions u(x,t) = φ(x - ct) connecting the states u = 0 (uninvaded) and u = 1 (invaded)."
- question: "Turing instability occurs when diffusion destabilizes a spatially homogeneous steady state."
  type: true-false
  answer: true
  explanation: "Turing's remarkable insight (1952) was that in a system of two reacting-diffusing species with different diffusion rates, a steady state that is stable without diffusion can become unstable when diffusion is added. The faster-diffusing inhibitor cannot keep up with the slower-diffusing activator, leading to spatial pattern formation."
- question: "What is a traveling wave solution of a reaction-diffusion equation?"
  type: short-answer
  answer: "A solution of the form u(x,t) = φ(x - ct) that maintains a fixed profile φ while moving at constant speed c"
  explanation: "Substituting u = φ(ξ) with ξ = x - ct into u_t = u_xx + f(u) gives the ODE -cφ' = φ'' + f(φ). Traveling wave analysis reduces the PDE to an ODE boundary value problem, which can be studied using phase plane methods. The minimum wave speed is a key quantity."
- question: "For the reaction-diffusion equation u_t = Δu + u^p with p > 1, solutions with large initial data can blow up in finite time."
  type: true-false
  answer: true
  explanation: "The reaction term u^p with p > 1 is superlinear, and for large enough initial data, the reaction overwhelms diffusion and drives the solution to infinity in finite time. The critical exponent p = 1 + 2/n (Fujita exponent) separates regimes: for p below this threshold, ALL nontrivial positive solutions blow up."
```

## Explainer
Reaction-diffusion equations are among the most important nonlinear PDEs in applied mathematics, describing spatial processes where substances or populations simultaneously spread through diffusion and undergo local reactions. The scalar equation u_t = DΔu + f(u) already exhibits fascinating behavior: when f has two stable zeros (bistable case, e.g., f(u) = u(1-u)(u-a)), the equation admits traveling wave solutions that connect the two stable states, modeling phase transitions, flame fronts, and population invasions.

The Fisher-KPP equation u_t = u_xx + u(1-u) is the prototype for population invasion. It admits traveling waves u = φ(x - ct) for all speeds c ≥ 2 (the minimum speed, determined by the linearization at u = 0). The remarkable result of Kolmogorov, Petrovsky, and Piskunov (1937) shows that compactly supported initial data evolves into a wave moving at the minimum speed c* = 2. The proof uses comparison principles—sub- and super-solutions trap the actual solution—combined with the asymptotic analysis of the linearized equation ahead of the front.

Turing's theory of morphogenesis (1952) is one of the most influential applications of reaction-diffusion systems. Consider two species u, v satisfying u_t = D_u Δu + f(u,v) and v_t = D_v Δv + g(u,v). If the homogeneous equilibrium is stable without diffusion, Turing showed it can become unstable when D_v >> D_u—the inhibitor v diffuses much faster than the activator u. This diffusion-driven instability leads to stationary spatial patterns (spots, stripes) with a characteristic wavelength selected by the dispersion relation. Turing patterns appear in animal coat markings, shell patterns, and chemical reactions (the Belousov-Zhabotinsky reaction).

The mathematical theory of reaction-diffusion equations draws on the full range of PDE techniques. Existence of solutions follows from parabolic theory (semigroup methods or Galerkin approximation). Maximum principles and comparison theorems provide L^∞ bounds and monotonicity. Traveling wave analysis connects to dynamical systems theory (heteroclinic connections in the phase plane). Blow-up theory studies the critical exponents and blow-up profiles. Bifurcation theory and center manifold reduction describe pattern formation near instability thresholds. The field remains extremely active, with current research on cross-diffusion systems, nonlocal reaction-diffusion models, and pattern formation in growing domains.
