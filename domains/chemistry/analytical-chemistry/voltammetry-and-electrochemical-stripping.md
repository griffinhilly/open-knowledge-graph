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
tags:
- voltammetry
- stripping-analysis
- electrochemistry
- trace-metals
stage: advanced
status: draft
---

# Voltammetry and Electrochemical Stripping Analysis

## Core Idea
Voltammetry and stripping methods apply controlled-potential electrochemistry to measure electroactive analytes. Anodic/cathodic stripping analysis provides trace metal determination (ppb to ppt levels) by concentrating the analyte through electrodeposition followed by stripping at a controlled potential while measuring current, dramatically improving sensitivity.

## Explainer

In standard voltammetry, you scan the potential applied to a working electrode and measure the resulting current as analytes are oxidized or reduced. The current-potential curve (a **voltammogram**) reveals both the identity (from the potential at which current flows) and the concentration (from the magnitude of the current) of electroactive species. This is the foundation you already have from prerequisite voltammetry. Stripping analysis takes this principle and adds an ingenious preconcentration step that pushes detection limits orders of magnitude lower.

The technique works in two phases. During the **deposition step**, you hold the electrode at a potential that forces the analyte to accumulate on or in the electrode surface — for example, reducing dissolved metal ions to metallic deposits on a mercury film or a bismuth electrode. This step might last several minutes, during which trace metals from a large volume of solution are concentrated into a tiny electrode. It is essentially an electrochemical sponge, soaking up analyte. During the **stripping step**, you sweep the potential in the reverse direction, oxidizing (or reducing) the accumulated material back into solution. The concentrated deposit produces a much larger current signal than the original dissolved analyte ever could, which is why detection limits reach parts per trillion.

**Anodic stripping voltammetry (ASV)** deposits metal cations by reduction and then strips them by anodic (oxidizing) sweep — ideal for metals like lead, cadmium, copper, and zinc. **Cathodic stripping voltammetry (CSV)** works in reverse, depositing an insoluble compound on the electrode surface during oxidation and stripping it cathodically — useful for anions like halides and sulfide. The choice depends on the electrochemistry of the target analyte. In both cases, the stripping peak potential identifies the metal, and the peak area or height is proportional to its concentration.

Practical considerations connect to electrochemical kinetics. Deposition time, stirring rate, electrode material, and solution composition all affect how efficiently analyte accumulates. Longer deposition times improve sensitivity but can lead to electrode saturation or intermetallic compound formation when multiple metals co-deposit. Modern variants like **square-wave** and **differential-pulse stripping** further enhance sensitivity by discriminating against capacitive background current. The result is one of the most sensitive methods available for trace metal analysis — routinely achieving detection limits that rival or exceed those of ICP-MS, using equipment that is portable and inexpensive.
