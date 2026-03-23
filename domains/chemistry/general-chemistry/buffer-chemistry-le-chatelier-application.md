---
id: buffer-chemistry-le-chatelier-application
title: Buffer Systems and pH Control
domain: chemistry
course: general-chemistry
prerequisites:
- id: buffer-solutions
  type: soft
- id: acid-base-strength-ka-kb-calculations
  type: hard
- id: le-chatelier-principle-applications
  type: soft
- id: logarithm-properties
  type: hard
builds-toward:
- acid-base-titration
tags:
- buffer
- pH
- henderson-hasselbalch
- acid-base
stage: formal-systems
status: validated
---

# Buffer Systems and pH Control

## Core Idea
A buffer solution resists pH change when small amounts of acid or base are added. Effective buffers contain a weak acid and its conjugate base (or weak base and its conjugate acid) in roughly equal amounts. The Henderson-Hasselbalch equation relates pH to buffer composition: pH = pKa + log([A−]/[HA]). Buffers work via Le Chatelier shifts.

## Questions

```yaml
- question: "A buffer is prepared with 0.10 M acetic acid and 0.10 M sodium acetate (pKa = 4.76). A small amount of HCl is added. What happens to the pH?"
  type: multiple-choice
  options:
    - "pH stays exactly at 4.76 — the buffer is at its sweet spot and completely neutralizes the acid"
    - "pH drops below 3 immediately, because HCl is a strong acid"
    - "pH drops slightly as acetate ions react with added H⁺, converting some conjugate base to weak acid"
    - "pH increases because the buffer absorbs the added acid"
  answer: 2
  explanation: "Buffers resist pH change but do not prevent it entirely. The added H⁺ reacts with acetate (A⁻) via Le Chatelier shift, consuming some conjugate base and producing more acetic acid — so pH drops slightly. Option A is the most common misconception: pH = pKa only when [A⁻]/[HA] = 1, but adding acid shifts that ratio, causing a small but real pH decrease."

- question: "A researcher needs a buffer with twice the capacity of their current 0.10 M acetate buffer at pH 4.76. They prepare a new buffer at the same pH ratio but with 0.20 M concentrations of both components. How does the new buffer compare?"
  type: multiple-choice
  options:
    - "Same capacity — pH and ratio are identical, so resistance to change is the same"
    - "Greater capacity — it can absorb twice as much added acid or base before the buffering fails"
    - "Lesser capacity — higher concentrations shift the equilibrium away from the optimal ratio"
    - "Greater capacity, but only for added acid, not added base"
  answer: 1
  explanation: "Buffer capacity depends on the absolute concentrations of weak acid and conjugate base, not just their ratio. Both buffers have the same pH (ratio determines pH via Henderson-Hasselbalch), but the 0.20 M buffer has twice the moles of each component available to absorb added acid or base before being overwhelmed."

- question: "A buffer prepared with a weak acid and its conjugate base at a 10:1 ratio (more weak acid than conjugate base) will have a pH below the pKa of the weak acid."
  type: true-false
  answer: true
  explanation: "pH = pKa + log([A⁻]/[HA]). With [A⁻]/[HA] = 1/10, log(1/10) = −1, so pH = pKa − 1. More weak acid than conjugate base pushes pH below pKa. This also means the buffer has less capacity to absorb added acid (conjugate base is nearly depleted in that direction)."

- question: "Two buffer solutions with the same weak acid/conjugate base ratio will resist pH change equally well, regardless of their absolute concentrations."
  type: true-false
  answer: false
  explanation: "The ratio determines pH via Henderson-Hasselbalch, but the absolute concentrations determine buffer capacity — how much acid or base can be absorbed before the buffer fails. A 1.0 M acetate buffer and a 0.01 M acetate buffer at the same ratio have identical pH but the former can absorb 100 times more added acid or base before being exhausted."

- question: "Why must an effective buffer contain significant amounts of both the weak acid and its conjugate base, rather than having one component greatly exceed the other?"
  type: short-answer
  answer: "With both components present in comparable amounts, the buffer has capacity in both directions: conjugate base absorbs added H⁺ (Le Chatelier shifts equilibrium toward HA), and weak acid donates H⁺ to absorb added OH⁻ (shifts toward A⁻). If one component is nearly depleted, the system loses the ability to resist changes in that direction. Maximum buffering capacity and pH stability occur at the 1:1 ratio (pH = pKa) because the system has equal reserves in both directions."
  explanation: "This is the mechanistic heart of buffering. The Henderson-Hasselbalch equation quantifies it: the buffer works best within ±1 pH unit of pKa, where neither component is below ~10% of the other. Outside that range, one reservoir is so small that adding even a little acid or base overwhelms it, and pH changes rapidly."
```

## Explainer

From your study of acid-base equilibria, you know that weak acids only partially dissociate in water — an acetic acid solution establishes an equilibrium between HA and A⁻. And from Le Chatelier's principle, you know that stressing an equilibrium pushes it to counteract the change. A **buffer solution** is the deliberate exploitation of both ideas: by having large reservoirs of both the weak acid and its conjugate base present simultaneously, the system can absorb added H⁺ or OH⁻ without significant pH change.

Here is the mechanism in concrete terms. Consider an acetic acid/sodium acetate buffer. If you add a small amount of strong acid (H⁺), the acetate ions (A⁻) react with the added H⁺ to form acetic acid (HA). The added protons are consumed, and pH barely moves. If you instead add strong base (OH⁻), the acetic acid molecules donate protons to neutralize the OH⁻, converting HA into A⁻. Again, the pH changes only slightly because the equilibrium has shifted to absorb the disturbance. Le Chatelier's principle predicts exactly these shifts — added product (H⁺) drives the equilibrium toward reactants, and vice versa.

The **Henderson-Hasselbalch equation** — pH = pKa + log([A⁻]/[HA]) — gives you quantitative control. When the concentrations of acid and conjugate base are equal, the log term is zero and pH = pKa. This is the buffer's sweet spot: maximum resistance to pH change in both directions. As the ratio shifts away from 1:1, buffering capacity drops. In practice, buffers work effectively within about ±1 pH unit of the pKa. This is why choosing the right weak acid matters — to buffer at pH 4.75, you pick acetic acid (pKa = 4.76); to buffer at pH 7.2, you pick dihydrogen phosphate (pKa₂ = 7.21). The logarithm you studied in your math prerequisites is doing real work here: because the relationship is logarithmic, even a tenfold change in the ratio only shifts pH by one unit.

**Buffer capacity** — the amount of acid or base a buffer can absorb before the pH changes significantly — depends on the absolute concentrations. A 1.0 M buffer and a 0.01 M buffer at the same pH ratio have the same pH, but the concentrated buffer can absorb 100 times more added acid or base before being overwhelmed. When the buffer is exhausted — when essentially all A⁻ has been converted to HA or vice versa — the pH begins changing rapidly, just as it would in unbuffered water. This is why biological systems like blood maintain buffers at relatively high concentrations: the carbonate buffer system keeps blood pH locked near 7.4, and even small failures in this regulation can be life-threatening.
