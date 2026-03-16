---
id: solid-phase-extraction-practice
title: Solid-Phase Extraction Practice and Applications
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: solid-phase-extraction
  type: hard
tags:
- SPE
- sample preparation
- extraction
stage: advanced
status: draft
---

# Solid-Phase Extraction Practice and Applications

## Core Idea
Solid-phase extraction uses sorbent cartridges to isolate analytes from complex matrices through selective adsorption and elution. SPE is faster and generates less solvent waste than traditional liquid-liquid extraction for many applications.

## Explainer

You already understand the theory of solid-phase extraction — how analytes selectively adsorb onto a sorbent and are eluted with an appropriate solvent. Putting SPE into practice means mastering the four-step workflow and learning to troubleshoot when real-world samples behave differently from textbook examples. The four steps are **conditioning**, **loading**, **washing**, and **elution**, and each one has specific failure modes that you need to anticipate.

**Conditioning** prepares the sorbent by wetting it with solvent (typically methanol for reversed-phase cartridges) followed by a buffer or water that matches your sample matrix. If the sorbent dries out between conditioning and loading, the surface chemistry resets and retention drops dramatically — this is the single most common SPE failure in practice. Think of conditioning as activating the sorbent's binding sites; skipping it is like trying to stick a Post-it note to a dusty wall.

During **loading**, your sample passes through the cartridge and analytes adsorb while most of the matrix flows through. Flow rate matters: too fast and analytes don't have time to interact with the sorbent, leading to breakthrough. A good rule of thumb is 1–2 mL per minute for a standard 3 mL cartridge. After loading, the **wash** step removes loosely bound interferences using a solvent that is strong enough to displace contaminants but too weak to strip your analytes. Choosing the right wash solvent requires understanding your analyte's affinity for the sorbent relative to the interferences — this is where your knowledge of polarity and intermolecular interactions pays off.

Finally, **elution** uses a strong solvent to release the analytes from the sorbent into a clean collection vessel. The goal is to collect your analytes in the smallest possible volume to maximize concentration. In practice, you optimize SPE by adjusting sorbent chemistry (C18 for nonpolar analytes, strong cation exchange for basic compounds, mixed-mode for complex samples), wash solvent strength, and elution volume. Method development typically involves spiking a known amount of analyte into a clean matrix, running the SPE procedure, and measuring recovery — aiming for 80–120% recovery with good reproducibility across replicates.
