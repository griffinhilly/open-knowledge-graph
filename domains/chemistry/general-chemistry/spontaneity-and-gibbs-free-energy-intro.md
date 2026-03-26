---
id: spontaneity-and-gibbs-free-energy-intro
title: Spontaneity and ΔG
domain: chemistry
course: general-chemistry
prerequisites:
- id: entropy-and-disorder
  type: hard
- id: thermochemistry-enthalpy
  type: hard
builds-toward:
- gibbs-free-energy-spontaneity
- electrochemistry-basics
tags:
- spontaneity
- Gibbs free energy
- ΔG
stage: formal-systems
status: validated
---

# Spontaneity and ΔG

## Core Idea
The Gibbs free energy change (ΔG = ΔH - TΔS) combines enthalpy and entropy to predict spontaneity. A negative ΔG indicates a spontaneous process; positive ΔG indicates non-spontaneous.

## Questions

```yaml
- question: "A reaction has ΔH = +80 kJ/mol and ΔS = +200 J/(mol·K). At 25°C (298 K), ΔG is positive and the reaction is non-spontaneous. At what temperature does it become spontaneous?"
  type: multiple-choice
  options:
    - "It is never spontaneous because ΔH is positive"
    - "Above approximately 400 K, where TΔS exceeds ΔH"
    - "Below 298 K, where the entropy contribution decreases"
    - "Only at absolute zero, where entropy has no effect"
  answer: 1
  explanation: "Spontaneity switches when ΔG = 0, which occurs at T = ΔH/ΔS = 80,000 J / 200 J·K⁻¹ = 400 K. Above this temperature, TΔS > ΔH and ΔG becomes negative. This is the mixed-sign case (positive ΔH, positive ΔS) where temperature is the deciding factor — the entropy contribution grows with T until it overwhelms the unfavorable enthalpy. Option A is a common misconception: endothermic reactions CAN be spontaneous at high enough temperatures."

- question: "Ice melts spontaneously at 25°C but does not melt spontaneously at −25°C. Which explanation correctly applies the Gibbs equation?"
  type: multiple-choice
  options:
    - "At 25°C, ΔH becomes negative because of the warmer surroundings"
    - "At −25°C, entropy decreases when ice melts, making ΔS negative"
    - "At 25°C, TΔS exceeds ΔH, making ΔG negative; at −25°C, ΔH dominates and ΔG is positive"
    - "Spontaneity depends only on enthalpy; at 25°C there is more energy available to break bonds"
  answer: 2
  explanation: "Melting ice has positive ΔH (energy absorbed to break hydrogen bonds) and positive ΔS (liquid is more disordered than solid). At low temperatures, ΔG = ΔH − TΔS is positive because TΔS is small. At high temperatures, TΔS grows until it exceeds ΔH and ΔG turns negative. The crossover is the melting point. Option D is incorrect because ΔH does not change with temperature in this simplified treatment — it is T that acts as the switch through the TΔS term."

- question: "A reaction that releases heat (negative ΔH) is typically spontaneous under standard conditions."
  type: true-false
  answer: false
  explanation: "Exothermic reactions are spontaneous at all temperatures only when ΔS is also positive. If ΔH is negative but ΔS is also negative, ΔG = ΔH − TΔS becomes positive at high temperatures (where the −TΔS term, which is positive when ΔS is negative, becomes large enough to outweigh ΔH). Spontaneity requires ΔG < 0, which depends on the combination of both ΔH and ΔS, weighted by temperature."

- question: "For a reaction with both negative ΔH and negative ΔS, increasing temperature makes the reaction less likely to be spontaneous."
  type: true-false
  answer: true
  explanation: "When both ΔH < 0 and ΔS < 0, ΔG = ΔH − TΔS = (negative) − T(negative) = (negative) + T|ΔS|. As T increases, the positive T|ΔS| term grows, eventually making ΔG positive and the reaction non-spontaneous. The entropy term, which opposes spontaneity here, becomes more influential at higher temperatures. This is why some reactions that are favorable at low temperatures become unfavorable when heated."

- question: "Why does temperature act as a 'switch' for spontaneity in reactions where ΔH and ΔS have opposite signs, but not in reactions where they have the same sign?"
  type: short-answer
  answer: "When ΔH and ΔS have opposite signs, the two terms in ΔG = ΔH − TΔS work against each other — one favors spontaneity while the other opposes it. Temperature controls the weight given to the entropy term (TΔS), so at some critical temperature the balance tips: ΔG switches sign. When ΔH and ΔS have the same sign, both terms favor the same outcome (or both oppose it), so no temperature can reverse the sign of ΔG — the reaction is spontaneous at all temperatures or non-spontaneous at all temperatures."
  explanation: "The equation ΔG = ΔH − TΔS makes this mechanical: if ΔH < 0 and ΔS > 0, both terms make ΔG negative regardless of T — always spontaneous. If ΔH > 0 and ΔS < 0, both terms make ΔG positive — never spontaneous. The mixed cases (+/− or −/+) pit the two thermodynamic drives against each other, and temperature determines which wins."
```

## Explainer

You have already learned two separate ways to think about whether a reaction "wants" to happen. From thermochemistry, you know that exothermic reactions (negative ΔH) release energy and tend to be favorable. From entropy, you know that processes increasing disorder (positive ΔS) also tend to be favorable. But these two drives can conflict — an endothermic reaction can be spontaneous if it creates enough disorder, and a highly ordered product can form if enough energy is released. **Gibbs free energy** is the single quantity that settles this tug-of-war.

The equation **ΔG = ΔH − TΔS** combines both factors into one number. Think of it as a balance sheet: ΔH represents the enthalpy "cost" or "payment" of the reaction, while TΔS represents the entropy contribution scaled by temperature. When ΔG is negative, the combination of energy release and entropy increase (or one overwhelming the other) makes the process spontaneous — it can proceed without external input. When ΔG is positive, the process is non-spontaneous as written, though the reverse reaction would be spontaneous.

The temperature term is crucial and often underappreciated. Notice that T multiplies ΔS, not ΔH. This means entropy becomes more influential at higher temperatures. Consider ice melting: ΔH is positive (you must add heat to break hydrogen bonds) and ΔS is positive (liquid water is more disordered than ice). At low temperatures, the positive ΔH dominates and ΔG is positive — ice does not melt. At high temperatures, TΔS overwhelms ΔH and ΔG becomes negative — ice melts spontaneously. The crossover temperature where ΔG = 0 is exactly the melting point: T = ΔH/ΔS. This framework lets you predict not just *whether* a process is spontaneous but *at what temperature* it becomes spontaneous.

There are four possible sign combinations for ΔH and ΔS, and understanding them provides a powerful diagnostic tool. If ΔH is negative and ΔS is positive, ΔG is always negative — the reaction is spontaneous at every temperature (combustion reactions are a classic example). If ΔH is positive and ΔS is negative, ΔG is always positive — the reaction is never spontaneous under standard conditions. The interesting cases are the mixed signs, where temperature acts as the switch. Recognizing which case you are in lets you immediately predict how temperature will affect spontaneity without doing any arithmetic.
