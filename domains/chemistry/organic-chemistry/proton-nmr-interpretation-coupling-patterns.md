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

## Questions

```yaml
- question: "A compound shows a signal at δ 9.8 ppm that integrates for 1H and appears as a doublet. Which interpretation is most consistent with these data?"
  type: multiple-choice
  options:
    - "An aldehyde proton with one adjacent CH group"
    - "An aromatic proton with one adjacent ring proton"
    - "An alcohol OH proton coupled to a neighboring CH"
    - "A methyl group next to a carbonyl"
  answer: 0
  explanation: "δ ~9.8 ppm is the hallmark of an aldehyde proton (strongly deshielded by the adjacent C=O). A doublet (n+1 = 2, so n = 1 neighbor) is consistent with a CHO proton next to a single CH group — the classic pattern for a branched aldehyde like isobutyraldehyde. Aromatic protons appear around δ 6.5–8, not δ 9.8. Alcohol OH protons typically appear around δ 1–5 and often exchange rapidly, giving broad singlets rather than clean doublets."

- question: "In ethanol (CH₃CH₂OH), you observe a quartet and a triplet in the ¹H NMR. A student claims the quartet must have 4 times more area (integration) than the triplet. Is the student correct?"
  type: multiple-choice
  options:
    - "No — the quartet arises from the CH₂ group (2H) and the triplet from the CH₃ group (3H), so the triplet integrates for more"
    - "Yes — quartets by definition represent more protons than triplets"
    - "No — the quartet arises from the CH₃ group (3H) and the triplet from the CH₂ group (2H), so the quartet integrates for more"
    - "Integration cannot be determined without knowing the molecular weight"
  answer: 2
  explanation: "Splitting pattern and integration are independent pieces of information. The CH₃ group has 2 CH₂ neighbors → 2+1 = triplet, and represents 3H. The CH₂ group has 3 CH₃ neighbors → 3+1 = quartet, and represents 2H. So the triplet (3H) integrates for MORE than the quartet (2H). The common misconception confuses multiplicity (from coupling) with integration (from proton count) — a bigger multiplet does not mean more protons."

- question: "Integration in ¹H NMR reports the absolute number of hydrogen atoms at each chemical shift."
  type: true-false
  answer: false
  explanation: "Integration gives *relative* ratios, not absolute counts. A signal integrating for '3 units' relative to another at '2 units' tells you the 3:2 ratio — consistent with CH₃ vs. CH₂, or C₂H₆ vs. C₄H₈ at corresponding positions in a larger symmetric molecule. To assign absolute proton counts, you must combine integration ratios with the molecular formula (from mass spectrometry) or another independent constraint."

- question: "The coupling constant (J value) measured in a doublet from proton A must equal the coupling constant measured in the corresponding multiplet of proton B, when A and B are coupled to each other."
  type: true-false
  answer: true
  explanation: "Coupling is mutual: the same J value appears in both coupled partners' signals. If proton A is split into a doublet by B with J = 7 Hz, then proton B's signal will also show a splitting of 7 Hz from A. This matching of J values is a key tool for confirming which protons are neighbors — it provides independent verification beyond chemical shift and integration."

- question: "Why does a proton next to a carbonyl group (like the alpha-H in acetaldehyde, CH₃CHO) appear at a higher δ value than a simple alkyl CH proton?"
  type: short-answer
  answer: "The carbonyl group is strongly electron-withdrawing. It pulls electron density away from the adjacent proton, reducing the local shielding at that nucleus. With less electron density to shield it from the external magnetic field, the proton resonates at a higher δ (is 'deshielded' and appears downfield)."
  explanation: "Chemical shift directly reflects electron density around the proton. Electron-withdrawing groups (carbonyls, halogens, aromatic rings) deshield nearby protons by reducing electron density, shifting signals downfield (higher δ). Electron-donating groups shield protons, shifting signals upfield (lower δ). Understanding this lets you read chemical shift as a direct map of electronic environment and functional group neighborhood."
```

## Explainer

Building on your knowledge of functional groups and the basics of NMR, ¹H NMR spectroscopy gives you three independent pieces of information from a single spectrum — and learning to read all three simultaneously is the key to structural determination. Each signal tells you where protons sit electronically (**chemical shift**), how many neighboring protons they have (**splitting pattern**), and how many protons of that type are present (**integration**). Together, these three readouts can pin down the structure of an unknown organic molecule.

**Chemical shift** (δ, measured in parts per million) reports on the electronic environment around each proton. Electrons shield the nucleus from the external magnetic field, so protons surrounded by electron-donating groups resonate at lower δ values (more shielded, upfield), while protons near electron-withdrawing groups like carbonyls, halogens, or aromatic rings resonate at higher δ values (deshielded, downfield). As a rough map: alkyl CH protons appear around δ 0.8–1.5, protons adjacent to oxygen or nitrogen around δ 3–4, aldehyde protons near δ 9–10, and aromatic protons in the δ 6.5–8 range. With practice, chemical shift alone often tells you which functional group a proton is near.

**Coupling patterns** arise because neighboring protons influence each other through bonds. When a proton has *n* equivalent neighbors three bonds away (vicinal coupling), its signal splits into *n* + 1 peaks — this is the **n+1 rule**. A proton next to two equivalent CH protons appears as a triplet; next to three, a quartet. The spacing between the peaks is the **coupling constant** (J, in Hz), and it is identical in both coupled partners, which helps you match signals that belong to adjacent groups. For example, in ethanol (CH₃CH₂OH), the CH₃ group has two CH₂ neighbors and appears as a triplet, while the CH₂ group has three CH₃ neighbors and appears as a quartet — a classic pattern you will see repeatedly.

**Integration** — the area under each signal — tells you the relative number of protons producing that signal. A signal integrating for 3 relative to another integrating for 2 likely corresponds to a CH₃ and a CH₂ group. Note that integration gives ratios, not absolute counts: a 3:2 ratio could also mean 6:4 protons in a symmetric molecule. The practical workflow is to combine all three types of information: use chemical shifts to narrow down which functional environments are present, use splitting to determine connectivity between adjacent groups, and use integration to confirm how many protons sit at each site. When these three constraints agree, the structure is determined.
