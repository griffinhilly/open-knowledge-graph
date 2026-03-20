---
id: bacterial-metabolism-overview
title: Bacterial Metabolism Overview
domain: biology
course: microbiology
prerequisites:
- id: bacterial-cell-structure
  type: hard
- id: cellular-respiration-overview
  type: soft
- id: oxidation-reduction-reactions
  type: hard
- id: thermochemistry-heat-and-energy
  type: soft
builds-toward:
- microbial-fermentation
- antibiotic-resistance-mechanisms
- nitrogen-fixation-microbiology
tags:
- metabolism
- aerobic
- anaerobic
- heterotroph
- autotroph
- chemotroph
stage: advanced
status: validated
---

# Bacterial Metabolism Overview

## Core Idea
Bacteria exhibit extraordinary metabolic diversity — far more than eukaryotes. They are classified by energy source (phototrophs use light, chemotrophs use chemical reactions), carbon source (autotrophs fix CO₂, heterotrophs consume organic molecules), and electron acceptor (aerobes use O₂, anaerobes use alternatives like nitrate, sulfate, or organic molecules). Aerobic respiration yields the most ATP via the electron transport chain, but many bacteria thrive in oxygen-free environments using anaerobic respiration or fermentation. Some bacteria are obligate aerobes (require O₂), others are obligate anaerobes (killed by O₂), and facultative anaerobes can switch between aerobic and anaerobic pathways depending on oxygen availability.

## How It's Best Learned
Start with the familiar framework of cellular respiration (glycolysis, Krebs cycle, ETC) and show how bacteria modify each step. Use a classification matrix — energy source vs. carbon source — to organize the diversity rather than memorizing species individually. Concrete examples anchor each category: E. coli as a facultative anaerobe, cyanobacteria as photoautotrophs, Clostridium as an obligate anaerobe. Compare ATP yields across pathways to build intuition about why aerobic respiration dominates when oxygen is available.

## Common Misconceptions
- Thinking all bacteria need oxygen — many thrive without it, and some are killed by it.
- Assuming anaerobic metabolism is primitive or inferior — it's an adaptation to specific ecological niches, not a deficiency.
- Confusing fermentation with anaerobic respiration — fermentation lacks an electron transport chain entirely, while anaerobic respiration uses one with a non-oxygen terminal acceptor.
- Believing autotrophy requires sunlight — chemoautotrophs (like deep-sea vent bacteria) derive energy purely from inorganic chemical reactions.

## Questions

```yaml
- question: "A bacterium living near a deep-sea hydrothermal vent oxidizes hydrogen sulfide (H₂S) as its energy source and uses CO₂ as its sole carbon source. How is it correctly classified?"
  type: multiple-choice
  options: ["Photoautotroph", "Photoheterotroph", "Chemoheterotroph", "Chemoautotroph"]
  answer: 3
  explanation: "Energy from an inorganic chemical reaction (H₂S oxidation) = chemotroph. Carbon from CO₂ fixation = autotroph. Combining these gives chemoautotroph. This is distinct from photoautotrophs like plants and cyanobacteria, which use light energy rather than chemical energy. The deep-sea example is important because it demonstrates that autotrophy does not require sunlight."

- question: "Fermentation is a type of anaerobic respiration because both processes occur without oxygen."
  type: true-false
  answer: false
  explanation: "Both fermentation and anaerobic respiration occur without O₂, but they are mechanistically distinct. Anaerobic respiration uses an electron transport chain with a non-oxygen terminal electron acceptor (e.g., nitrate, sulfate). Fermentation has no electron transport chain at all — it regenerates NAD+ by transferring electrons to an organic molecule (like pyruvate), yielding only 2 ATP per glucose. Sharing the absence of O₂ does not make them the same process."

- question: "Why do facultative anaerobes preferentially perform aerobic respiration when oxygen is available, even though they are capable of surviving without it?"
  type: short-answer
  answer: "Aerobic respiration via the electron transport chain yields approximately 30-32 ATP per glucose, compared to only 2 ATP from fermentation, giving cells a strong energetic advantage and faster growth rate when O₂ is present."
  explanation: "The vast difference in ATP yield comes from the electron transport chain and oxidative phosphorylation, which are only possible when a high-energy terminal electron acceptor (O₂) is available. Fermentation short-circuits the process, recovering energy only from substrate-level phosphorylation. Natural selection favors using the more efficient pathway when conditions allow it."
```

## Explainer

When you learned cellular respiration, you studied one pathway — aerobic respiration using oxygen — because that is the dominant strategy in eukaryotes. Bacteria are far more metabolically creative. Understanding bacterial metabolism requires a classification system built on three independent questions: Where does the energy come from? Where does the carbon come from? What accepts electrons at the end of the pathway?

The energy-source axis divides organisms into phototrophs (energy from light) and chemotrophs (energy from chemical reactions). The carbon-source axis divides them into autotrophs (fix CO₂ into organic molecules) and heterotrophs (consume pre-made organic molecules). Combining these gives four categories. Most familiar eukaryotes are either photoautotrophs (plants) or chemoheterotrophs (animals and fungi). Bacteria fill all four quadrants, including photoheterotrophs (use light but consume organic carbon) and chemoautotrophs (oxidize inorganic molecules for energy and fix CO₂). Deep-sea vent communities run entirely on chemoautotrophy — no sunlight required.

The third axis is the electron acceptor, which determines which version of respiration is possible. Oxygen is the most energetically favorable electron acceptor, which is why aerobic respiration produces ~30-32 ATP per glucose via the full electron transport chain. In the absence of O₂, bacteria have options: use an alternative inorganic acceptor like nitrate (NO₃⁻) or sulfate (SO₄²⁻) in anaerobic respiration (still uses an ETC, still relatively efficient), or abandon the ETC entirely and ferment. Fermentation regenerates NAD⁺ by dumping electrons onto an organic molecule like pyruvate — yielding only 2 ATP but requiring no external acceptor at all.

The obligate/facultative distinction matters enormously in medicine and ecology. Obligate aerobes (like Mycobacterium tuberculosis) concentrate in well-oxygenated tissues like the lung apex. Obligate anaerobes (like Clostridium species) are found in deep wounds, intestinal microbiomes, and anoxic sediments — and can cause serious infections precisely in oxygen-deprived wounds. Facultative anaerobes like E. coli thrive in both environments, making them highly adaptable colonizers. When you take antibiotics that disrupt aerobic gut bacteria, you create niche space that anaerobes rapidly fill, which is why antibiotic-associated diarrhea is common and *C. difficile* overgrowth is a serious complication.
