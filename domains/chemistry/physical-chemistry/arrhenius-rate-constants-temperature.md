---
id: arrhenius-rate-constants-temperature
title: Arrhenius Equation and Temperature Dependence of Rate Constants
domain: chemistry
course: physical-chemistry
prerequisites: []
builds-toward:
- pre-exponential-factor-collision-theory
- transition-state-theory
tags:
- arrhenius
- kinetics
- rate-constant
- temperature
stage: formal-systems
status: draft
---

# Arrhenius Equation and Temperature Dependence of Rate Constants

## Core Idea
The Arrhenius equation k = A exp(-Eₐ/RT) quantitatively relates rate constants to temperature through activation energy Eₐ. The pre-exponential factor A accounts for proper orientation and collision frequency. Plotting ln(k) vs 1/T gives a straight line, allowing experimental determination of Eₐ and A from kinetic data. Small changes in temperature cause exponential changes in rate constant, explaining how catalysts and temperature control reaction rates.

## Questions

```yaml
- question: "An enzyme lowers the activation energy of a reaction from 80 kJ/mol to 50 kJ/mol at 310 K. The rate constant increases dramatically because:"
  type: multiple-choice
  options:
    - "Lowering Eₐ increases the frequency of molecular collisions, so more reactions occur per second"
    - "Eₐ appears in the exponent of the Arrhenius equation, so even a moderate reduction in Eₐ produces an exponential increase in k"
    - "The enzyme raises the temperature of the local reaction environment, effectively increasing RT"
    - "Lowering Eₐ changes the thermodynamics of the reaction, making the products more stable"
  answer: 1
  explanation: "The Arrhenius equation k = A·exp(−Eₐ/RT) places Eₐ in the exponent. At 310 K (body temperature), RT ≈ 2.58 kJ/mol. A reduction of 30 kJ/mol in Eₐ changes the exponent by 30/2.58 ≈ 11.6 units. Since exp(11.6) ≈ 110,000, the rate constant increases by roughly five orders of magnitude — not because collisions are more frequent, but because a vastly larger fraction of collisions now have sufficient energy to overcome the barrier. Critically, the enzyme does not change ΔG (the thermodynamics are unchanged); it only lowers the kinetic barrier. This exponential sensitivity to Eₐ is why enzymes are so spectacularly effective."

- question: "On an Arrhenius plot (ln k vs 1/T), Reaction A has a steeper negative slope than Reaction B. This means:"
  type: multiple-choice
  options:
    - "Reaction A is faster than Reaction B at all temperatures"
    - "Reaction A has a higher activation energy than Reaction B"
    - "Reaction A is more temperature-sensitive at low temperatures, but less so at high temperatures"
    - "Reaction A has a smaller pre-exponential factor A than Reaction B"
  answer: 1
  explanation: "The slope of the Arrhenius plot is −Eₐ/R. A steeper (more negative) slope means a larger Eₐ/R ratio, hence higher activation energy. A higher Eₐ means the rate constant changes more dramatically per degree of temperature change — the reaction is more temperature-sensitive. Note that slope tells you nothing about which reaction is faster at any given temperature (that also depends on the pre-exponential factor A); two reactions can have different slopes but the same rate at some temperature. The Arrhenius plot cleanly separates the two contributions: slope gives Eₐ, y-intercept gives ln(A)."

- question: "A catalyst increases the rate of a reaction without being consumed, and it does so by lowering the activation energy without changing the overall thermodynamics (ΔG) of the reaction."
  type: true-false
  answer: true
  explanation: "This is the precise mechanistic definition of catalysis. A catalyst provides an alternative reaction pathway with a lower Eₐ, so more collisions carry enough energy to proceed — increasing k exponentially. However, ΔG = ΔH − TΔS for the overall reaction is set by the reactant and product identities, which the catalyst does not change. The equilibrium constant K is related to ΔG (not to the kinetics), so the catalyst does not shift the equilibrium position — it only reaches it faster. A catalyst speeds the forward and reverse reactions equally, leaving Keq unchanged. This is why a catalyst cannot cause a thermodynamically unfavorable reaction to proceed — it can only accelerate thermodynamically allowed reactions."

- question: "Doubling the absolute temperature of a reaction always approximately doubles the rate constant."
  type: true-false
  answer: false
  explanation: "The relationship is exponential, not linear. Doubling T from 300 K to 600 K changes exp(−Eₐ/RT) from exp(−Eₐ/300R) to exp(−Eₐ/600R). For a typical Eₐ of 60 kJ/mol, this changes the exponent from −24 to −12 — increasing k by exp(12) ≈ 160,000-fold, far more than doubling. For a smaller Eₐ or a smaller temperature jump, the factor is smaller. The common empirical rule of thumb that a 10°C rise roughly doubles the rate works for reactions with Eₐ ≈ 50–80 kJ/mol near room temperature, but it is an approximation that breaks down at other temperatures and activation energies."

- question: "Why does the Arrhenius plot (ln k versus 1/T) yield a straight line, and what information can be extracted from its slope and intercept?"
  type: short-answer
  answer: "Taking the natural log of k = A·exp(−Eₐ/RT) gives ln(k) = ln(A) − Eₐ/(RT). Written as ln(k) = ln(A) − (Eₐ/R)·(1/T), this is in the form y = b + mx, a linear equation where y = ln(k), x = 1/T, slope m = −Eₐ/R, and intercept b = ln(A). A straight line results because the log transformation converts the exponential relationship into a linear one. The slope gives the activation energy (Eₐ = −slope × R), and the y-intercept gives ln(A), from which the pre-exponential factor A can be extracted."
  explanation: "The Arrhenius plot is the standard experimental method for determining activation energies. Rate constants are measured at several temperatures, plotted as ln(k) vs 1/T, and the best-fit line is drawn. A curved Arrhenius plot signals that the mechanism changes with temperature (e.g., a different rate-limiting step dominates at high vs. low T), which is diagnostically important. The linearity assumption underlies most kinetic analyses, so curvature is always worth investigating rather than dismissing."
```

## Explainer

Every chemical reaction has a speed, and that speed changes dramatically with temperature. The **Arrhenius equation** — k = A exp(−Eₐ/RT) — captures this relationship in a single expression. Here, k is the rate constant, A is the **pre-exponential factor** (related to how often molecules collide with the right orientation), Eₐ is the **activation energy** (the minimum energy barrier reactants must overcome), R is the gas constant, and T is absolute temperature in Kelvin. The equation says that the rate constant grows exponentially as temperature rises or as activation energy falls.

The intuition behind the equation comes from thinking about molecular collisions. Not every collision between reactant molecules leads to a reaction — only those with enough kinetic energy to surmount the activation energy barrier and with the correct geometric orientation. At higher temperatures, molecules move faster, so a larger fraction of collisions carry enough energy to clear the barrier. The exponential term exp(−Eₐ/RT) represents exactly this fraction: it is the probability that a given collision has energy ≥ Eₐ. Because this fraction sits inside an exponential, even a modest temperature increase — say 10°C — can double or triple the rate constant for a reaction with a typical Eₐ of 50–100 kJ/mol.

The most practical tool derived from the Arrhenius equation is the **Arrhenius plot**. Taking the natural logarithm of both sides gives ln(k) = ln(A) − Eₐ/(RT), which has the form y = b + mx with y = ln(k) and x = 1/T. A plot of ln(k) versus 1/T should yield a straight line with slope −Eₐ/R and y-intercept ln(A). This means you can determine activation energy experimentally by measuring rate constants at several temperatures, plotting the data, and reading Eₐ directly from the slope. Steeper slopes mean higher activation energies; shallow slopes mean the reaction is relatively insensitive to temperature.

Understanding the Arrhenius equation also explains how **catalysts** work at a quantitative level. A catalyst provides an alternative reaction pathway with a lower Eₐ. Because Eₐ appears in the exponent, even a small reduction in activation energy produces a large increase in the rate constant. For example, reducing Eₐ by just 10 kJ/mol at 300 K increases the rate constant by roughly a factor of 50. This exponential sensitivity is why enzymes and industrial catalysts are so effective — they do not change the thermodynamics of the reaction (ΔG is unchanged), but by lowering the kinetic barrier, they make the reaction proceed fast enough to be useful.
