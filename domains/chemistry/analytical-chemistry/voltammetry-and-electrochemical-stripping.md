---
id: voltammetry-and-electrochemical-stripping
title: Voltammetry and Electrochemical Stripping Analysis
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: voltammetry
  type: hard
- id: electrochemical-kinetics
  type: soft
- id: electroanalytical-overview
  type: soft
tags:
- voltammetry
- stripping-analysis
- electrochemistry
- trace-metals
stage: advanced
status: validated
---
# Voltammetry and Electrochemical Stripping Analysis

## Core Idea
Voltammetry and stripping methods apply controlled-potential electrochemistry to measure electroactive analytes. Anodic/cathodic stripping analysis provides trace metal determination (ppb to ppt levels) by concentrating the analyte through electrodeposition followed by stripping at a controlled potential while measuring current, dramatically improving sensitivity.

## Questions

```yaml
- question: "Why does stripping analysis achieve far lower detection limits than standard voltammetry applied to the same sample?"
  type: multiple-choice
  options:
    - "A more selective electrode material is used that reacts only with trace metals"
    - "The analyte is concentrated at the electrode during a deposition step before the measurement is made"
    - "A slower scan rate gives more time for current to flow at trace concentrations"
    - "Differential-pulse waveforms are applied instead of linear sweeps"
  answer: 1
  explanation: "The key innovation of stripping analysis is the preconcentration step: trace analyte from a large solution volume is electrodeposited onto a tiny electrode surface, then stripped in a single burst. This concentration effect amplifies the signal by orders of magnitude. Differential-pulse waveforms (option D) also improve sensitivity, but they are an enhancement layered on top of the preconcentration — standard voltammetry with a differential-pulse waveform still cannot approach the detection limits of stripping analysis without the deposition step."

- question: "In anodic stripping voltammetry (ASV), which sequence of events correctly describes the two-phase measurement?"
  type: multiple-choice
  options:
    - "First, metal deposits are cathodically stripped into solution; then, fresh metal is oxidized from solution onto the electrode"
    - "First, metal ions are reduced and deposited onto the electrode; then, the electrode potential is swept anodically to oxidize and dissolve the deposit"
    - "First, the solution is stirred vigorously to accumulate metal at the electrode surface; then, current is measured at open circuit"
    - "First, an oxidizing potential dissolves surface contaminants; then, a reducing potential plates the analyte"
  answer: 1
  explanation: "ASV works in two phases: (1) deposition — holding a sufficiently negative potential reduces dissolved metal cations (e.g., Pb²⁺ → Pb⁰) and plates them onto the electrode; (2) stripping — sweeping the potential in the positive (anodic) direction oxidizes the deposited metal back into solution. The resulting oxidation current peak identifies the metal (via its characteristic stripping potential) and quantifies it (via peak height or area)."

- question: "A longer deposition time in stripping analysis generally improves sensitivity because more analyte accumulates on the electrode."
  type: true-false
  answer: false
  explanation: "While longer deposition time does increase analyte accumulation — improving sensitivity — it can also lead to electrode saturation or, when multiple metals are present, to intermetallic compound formation between co-deposited metals. Intermetallics shift or distort stripping peaks, degrading selectivity. In practice, deposition time must be optimized rather than simply maximized."

- question: "In stripping analysis, the potential at which the stripping current peak occurs identifies which metal analyte is present."
  type: true-false
  answer: true
  explanation: "Different metals strip (re-oxidize or re-reduce) at characteristic potentials determined by their standard reduction potentials. Just as in standard voltammetry, the position of the current peak on the potential axis is a qualitative identifier, while the peak magnitude or area provides quantitative information about concentration."

- question: "Explain why anodic stripping voltammetry can detect metals at parts-per-trillion levels while standard voltammetry on the same sample cannot."
  type: short-answer
  answer: "In standard voltammetry, you measure the small current from analyte dissolved at trace concentration directly. In ASV, a long deposition step accumulates trace metal from a large volume of solution onto a tiny electrode surface — essentially running an electrochemical preconcentration. When the concentrated deposit is then stripped, it produces a current signal many orders of magnitude larger than the original dissolved analyte could generate, pushing detection limits from ppb (standard voltammetry) down to ppt."
  explanation: "The principle is analogous to concentrating a dilute solution before measuring it: the measurement itself has not changed, but the amount of analyte being measured has increased enormously. Detection limit is ultimately governed by how well the signal can be distinguished from background noise; by amplifying the signal through preconcentration, stripping analysis clears this bar for concentrations that would otherwise be unmeasurable."
```

## Explainer

In standard voltammetry, you scan the potential applied to a working electrode and measure the resulting current as analytes are oxidized or reduced. The current-potential curve (a **voltammogram**) reveals both the identity (from the potential at which current flows) and the concentration (from the magnitude of the current) of electroactive species. This is the foundation you already have from prerequisite voltammetry. Stripping analysis takes this principle and adds an ingenious preconcentration step that pushes detection limits orders of magnitude lower.

The technique works in two phases. During the **deposition step**, you hold the electrode at a potential that forces the analyte to accumulate on or in the electrode surface — for example, reducing dissolved metal ions to metallic deposits on a mercury film or a bismuth electrode. This step might last several minutes, during which trace metals from a large volume of solution are concentrated into a tiny electrode. It is essentially an electrochemical sponge, soaking up analyte. During the **stripping step**, you sweep the potential in the reverse direction, oxidizing (or reducing) the accumulated material back into solution. The concentrated deposit produces a much larger current signal than the original dissolved analyte ever could, which is why detection limits reach parts per trillion.

**Anodic stripping voltammetry (ASV)** deposits metal cations by reduction and then strips them by anodic (oxidizing) sweep — ideal for metals like lead, cadmium, copper, and zinc. **Cathodic stripping voltammetry (CSV)** works in reverse, depositing an insoluble compound on the electrode surface during oxidation and stripping it cathodically — useful for anions like halides and sulfide. The choice depends on the electrochemistry of the target analyte. In both cases, the stripping peak potential identifies the metal, and the peak area or height is proportional to its concentration.

Practical considerations connect to electrochemical kinetics. Deposition time, stirring rate, electrode material, and solution composition all affect how efficiently analyte accumulates. Longer deposition times improve sensitivity but can lead to electrode saturation or intermetallic compound formation when multiple metals co-deposit. Modern variants like **square-wave** and **differential-pulse stripping** further enhance sensitivity by discriminating against capacitive background current. The result is one of the most sensitive methods available for trace metal analysis — routinely achieving detection limits that rival or exceed those of ICP-MS, using equipment that is portable and inexpensive.
