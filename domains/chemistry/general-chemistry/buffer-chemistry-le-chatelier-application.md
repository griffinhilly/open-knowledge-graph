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
status: draft
---

# Buffer Systems and pH Control

## Core Idea
A buffer solution resists pH change when small amounts of acid or base are added. Effective buffers contain a weak acid and its conjugate base (or weak base and its conjugate acid) in roughly equal amounts. The Henderson-Hasselbalch equation relates pH to buffer composition: pH = pKa + log([A−]/[HA]). Buffers work via Le Chatelier shifts.

## Explainer

From your study of acid-base equilibria, you know that weak acids only partially dissociate in water — an acetic acid solution establishes an equilibrium between HA and A⁻. And from Le Chatelier's principle, you know that stressing an equilibrium pushes it to counteract the change. A **buffer solution** is the deliberate exploitation of both ideas: by having large reservoirs of both the weak acid and its conjugate base present simultaneously, the system can absorb added H⁺ or OH⁻ without significant pH change.

Here is the mechanism in concrete terms. Consider an acetic acid/sodium acetate buffer. If you add a small amount of strong acid (H⁺), the acetate ions (A⁻) react with the added H⁺ to form acetic acid (HA). The added protons are consumed, and pH barely moves. If you instead add strong base (OH⁻), the acetic acid molecules donate protons to neutralize the OH⁻, converting HA into A⁻. Again, the pH changes only slightly because the equilibrium has shifted to absorb the disturbance. Le Chatelier's principle predicts exactly these shifts — added product (H⁺) drives the equilibrium toward reactants, and vice versa.

The **Henderson-Hasselbalch equation** — pH = pKa + log([A⁻]/[HA]) — gives you quantitative control. When the concentrations of acid and conjugate base are equal, the log term is zero and pH = pKa. This is the buffer's sweet spot: maximum resistance to pH change in both directions. As the ratio shifts away from 1:1, buffering capacity drops. In practice, buffers work effectively within about ±1 pH unit of the pKa. This is why choosing the right weak acid matters — to buffer at pH 4.75, you pick acetic acid (pKa = 4.76); to buffer at pH 7.2, you pick dihydrogen phosphate (pKa₂ = 7.21). The logarithm you studied in your math prerequisites is doing real work here: because the relationship is logarithmic, even a tenfold change in the ratio only shifts pH by one unit.

**Buffer capacity** — the amount of acid or base a buffer can absorb before the pH changes significantly — depends on the absolute concentrations. A 1.0 M buffer and a 0.01 M buffer at the same pH ratio have the same pH, but the concentrated buffer can absorb 100 times more added acid or base before being overwhelmed. When the buffer is exhausted — when essentially all A⁻ has been converted to HA or vice versa — the pH begins changing rapidly, just as it would in unbuffered water. This is why biological systems like blood maintain buffers at relatively high concentrations: the carbonate buffer system keeps blood pH locked near 7.4, and even small failures in this regulation can be life-threatening.
