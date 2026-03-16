---
id: proton-nmr-interpretation-coupling-patterns
title: '¹H NMR Spectroscopy: Chemical Shift and Coupling Patterns'
domain: chemistry
course: organic-chemistry
prerequisites:
- id: nmr-spectroscopy-basics
  type: soft
- id: functional-groups-overview
  type: hard
builds-toward:
- c-13-nmr-and-ir-structural-determination
tags:
- nmr
- proton-nmr
- chemical-shift
- coupling
- spectroscopy
stage: formal-systems
status: draft
---

# ¹H NMR Spectroscopy: Chemical Shift and Coupling Patterns

## Core Idea
¹H NMR chemical shifts (δ, in ppm) reflect electronic environment: electron-donating groups shield protons (lower δ), electron-withdrawing groups deshield (higher δ). Coupling between vicinal protons (³J, three bonds apart) causes multiplet splitting; the n+1 rule predicts multiplicity from the number of neighboring protons. Integration indicates the ratio of protons at each site.

## How It's Best Learned
Assign protons in structures to observed peaks based on chemical shift and multiplicity. Predict coupling patterns and integration from structures.

## Common Misconceptions
- Confusing peak height with integration; peak area (not height due to line width) represents the number of protons.
- Assuming equivalent protons always show identical chemical shift; rapid exchange (e.g., OH, NH) can cause apparent equivalence.

## Explainer

Building on your knowledge of functional groups and the basics of NMR, ¹H NMR spectroscopy gives you three independent pieces of information from a single spectrum — and learning to read all three simultaneously is the key to structural determination. Each signal tells you where protons sit electronically (**chemical shift**), how many neighboring protons they have (**splitting pattern**), and how many protons of that type are present (**integration**). Together, these three readouts can pin down the structure of an unknown organic molecule.

**Chemical shift** (δ, measured in parts per million) reports on the electronic environment around each proton. Electrons shield the nucleus from the external magnetic field, so protons surrounded by electron-donating groups resonate at lower δ values (more shielded, upfield), while protons near electron-withdrawing groups like carbonyls, halogens, or aromatic rings resonate at higher δ values (deshielded, downfield). As a rough map: alkyl CH protons appear around δ 0.8–1.5, protons adjacent to oxygen or nitrogen around δ 3–4, aldehyde protons near δ 9–10, and aromatic protons in the δ 6.5–8 range. With practice, chemical shift alone often tells you which functional group a proton is near.

**Coupling patterns** arise because neighboring protons influence each other through bonds. When a proton has *n* equivalent neighbors three bonds away (vicinal coupling), its signal splits into *n* + 1 peaks — this is the **n+1 rule**. A proton next to two equivalent CH protons appears as a triplet; next to three, a quartet. The spacing between the peaks is the **coupling constant** (J, in Hz), and it is identical in both coupled partners, which helps you match signals that belong to adjacent groups. For example, in ethanol (CH₃CH₂OH), the CH₃ group has two CH₂ neighbors and appears as a triplet, while the CH₂ group has three CH₃ neighbors and appears as a quartet — a classic pattern you will see repeatedly.

**Integration** — the area under each signal — tells you the relative number of protons producing that signal. A signal integrating for 3 relative to another integrating for 2 likely corresponds to a CH₃ and a CH₂ group. Note that integration gives ratios, not absolute counts: a 3:2 ratio could also mean 6:4 protons in a symmetric molecule. The practical workflow is to combine all three types of information: use chemical shifts to narrow down which functional environments are present, use splitting to determine connectivity between adjacent groups, and use integration to confirm how many protons sit at each site. When these three constraints agree, the structure is determined.
