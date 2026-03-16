---
id: rock-magnetism-hysteresis
title: 'Rock Magnetism: Domains, Hysteresis, and Saturation'
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: earths-magnetic-dipole-field-basics
  type: hard
- id: paleomagnetism-and-reversals
  type: soft
tags:
- magnetism
- rock-magnetism
- domains
- hysteresis
stage: advanced
status: draft
---

# Rock Magnetism: Domains, Hysteresis, and Saturation

## Core Idea
Magnetization in rocks arises from ferromagnetic and antiferromagnetic minerals with magnetic domains. Hysteresis curves (magnetization vs. field) reveal domain size, saturation magnetization, and coercivity; these properties vary with mineralogy, grain size, and temperature.

## Explainer

From your study of Earth's magnetic dipole field and paleomagnetism, you know that certain rocks record the direction of the ambient magnetic field at the time they formed. Rock magnetism explains *how* this recording happens at the mineral scale — and the **hysteresis loop** is the central diagnostic tool for understanding the magnetic behavior of those minerals.

Ferromagnetic minerals like **magnetite** (Fe₃O₄) and **hematite** (Fe₂O₃) contain unpaired electrons whose magnetic moments align cooperatively, producing strong net magnetization. Within a grain, the magnetization organizes into **magnetic domains** — regions of uniform magnetization direction separated by thin domain walls. Large grains (typically >10 μm for magnetite) contain many domains that largely cancel each other out, resulting in weak net magnetization. Smaller grains have fewer domains, and below a critical size (~80 nm for magnetite), the grain becomes **single-domain**: the entire grain is magnetized uniformly in one direction. Single-domain grains are the most stable magnetic recorders because flipping their magnetization requires overcoming a large energy barrier — which is why they are the workhorses of paleomagnetic recording.

The **hysteresis curve** maps out a mineral's magnetic response as you cycle an external field from strong positive to strong negative and back. Starting from zero, magnetization increases as domains align with the applied field until all moments are parallel — this plateau is the **saturation magnetization** (Mₛ), a property of the mineral chemistry itself. When you reduce the field back to zero, the magnetization does not return to zero; the remaining magnetization is the **remanent magnetization** (Mᵣ). The field you must apply in the *opposite* direction to bring the magnetization to zero is the **coercivity** (Hc). The "fatness" of the hysteresis loop — quantified by the ratios Mᵣ/Mₛ and Hcr/Hc — tells you about domain state. Single-domain grains produce fat, square loops (high Mᵣ/Mₛ, near 0.5), while multi-domain grains produce thin, narrow loops (low Mᵣ/Mₛ) because domain walls move easily and magnetization is readily lost.

These properties are not just academic — they determine whether a rock reliably records ancient field directions. A basalt with abundant single-domain magnetite will carry a stable paleomagnetic signal for billions of years, while a coarse-grained gabbro with multi-domain magnetite may have its original signal overprinted by later fields. Temperature matters too: every ferromagnetic mineral has a **Curie temperature** above which thermal energy destroys magnetic order entirely (580°C for magnetite, 675°C for hematite). Heating experiments that track how magnetization changes with temperature help identify which minerals are present and whether the remanence is primary or secondary — essential information for any paleomagnetic study.
