---
id: nucleotide-synthesis
title: Nucleotide Synthesis Pathways (De Novo and Salvage)
domain: biology
course: biochemistry
prerequisites:
- id: organic-chemistry-intro
  type: hard
builds-toward:
- dna-replication-machinery
- transcription-initiation-and-regulation
tags:
- nucleotide synthesis
- purine
- pyrimidine
- de novo
- salvage pathway
stage: formal-systems
status: validated
---

# Nucleotide Synthesis Pathways (De Novo and Salvage)

## Core Idea
Nucleotides are synthesized through two pathways: de novo synthesis (building the base and ribose ring from simpler precursors) and salvage pathways (recycling bases and nucleosides from degraded nucleic acids). De novo purine synthesis begins with PRPP and constructs the purine ring while attached to ribose, producing IMP, then AMP and GMP. De novo pyrimidine synthesis first completes the pyrimidine ring as orotate, then attaches to PRPP, producing UMP, then CTP and dTTP. Both pathways are tightly regulated by feedback inhibition and require multiple vitamin cofactors (folate, B12).

## Questions

```yaml
- question: "A patient has a complete deficiency of HGPRT. Which statement best explains why this causes neurological damage despite cells retaining intact de novo synthesis?"
  type: multiple-choice
  options:
    - "HGPRT is required for de novo purine synthesis, so its loss blocks all purine production in neurons"
    - "The brain relies heavily on salvage pathways to recycle purines because neurons have very low de novo synthesis capacity; without HGPRT, hypoxanthine and guanine cannot be recycled and neurons are starved of purines"
    - "HGPRT deficiency causes excess pyrimidines to accumulate, which are neurotoxic at high concentrations"
    - "De novo synthesis is only active during cell division; non-dividing neurons depend entirely on salvage for all nucleotide production"
  answer: 1
  explanation: "The key insight is tissue-specific dependence on salvage. The brain has unusually high purine demand (for ATP, cAMP, signaling) but low de novo synthesis activity, making neurons disproportionately dependent on HGPRT to recycle hypoxanthine and guanine from nucleic acid turnover. When HGPRT is absent, the brain cannot compensate through de novo synthesis at the required rate, leading to purine depletion in neurons and the devastating neurological symptoms of Lesch-Nyhan syndrome. Option D overstates the case — non-dividing cells can perform de novo synthesis, just at rates insufficient to compensate in the brain."

- question: "Which statement correctly describes the fundamental architectural difference between de novo purine and de novo pyrimidine synthesis?"
  type: multiple-choice
  options:
    - "Purines are synthesized from a single amino acid precursor; pyrimidines require three different amino acids"
    - "Purine synthesis builds the ring step-by-step while attached to PRPP (ribose-first); pyrimidine synthesis builds the ring as a free base (orotate) and only then attaches to PRPP"
    - "Purines are assembled as free bases and then attached to ribose, while pyrimidines are assembled directly on ribose from the start"
    - "Both pathways build the base as a free molecule first, but purines require GTP for the final attachment while pyrimidines require ATP"
  answer: 1
  explanation: "This architectural reversal is the central organizational fact of nucleotide synthesis. In purine de novo synthesis, PRPP serves as the starting scaffold — atoms from glutamine, glycine, aspartate, CO₂, and formyl-THF are added piece by piece to the ribose-phosphate backbone, ultimately building IMP. In pyrimidine synthesis, the ring is completed first as orotate (from carbamoyl phosphate and aspartate), and only afterward is it attached to PRPP to form orotidylate, which is then decarboxylated to UMP. Option C has the two pathways exactly reversed."

- question: "Salvage pathways produce nucleotides by assembling purines or pyrimidines from small precursor molecules like CO₂ and amino acids, making them the energetically preferred alternative to de novo synthesis."
  type: true-false
  answer: false
  explanation: "Salvage pathways do not build bases from small precursors — that is de novo synthesis. Salvage pathways *recycle* preformed bases (hypoxanthine, guanine, adenine) that have been released during normal nucleic acid degradation, reattaching them to PRPP in a single enzymatic step. This is energetically cheaper than de novo synthesis precisely because the complex ring structures have already been built. The distinction is critical: de novo synthesis = build from scratch using amino acids, CO₂, folate; salvage = recycle existing bases using PRPP."

- question: "The de novo synthesis of purines requires folate derivatives (formyl-THF) as carbon donors, which is why drugs blocking folate metabolism (like methotrexate) preferentially kill rapidly dividing cells."
  type: true-false
  answer: true
  explanation: "Formyl-THF donates carbons at two steps in purine de novo synthesis, and thymidylate synthase requires a folate coenzyme to convert dUMP to dTMP (the specific thymidine nucleotide needed for DNA). Rapidly dividing cells (cancer cells, immune cells) require enormous amounts of new nucleotides for DNA replication and cannot rely solely on recycled bases — they are highly dependent on de novo synthesis pathways that require folate. Methotrexate blocks dihydrofolate reductase, depleting active folate cofactors and starving dividing cells of the purines and thymidylate they need. Normal slow-dividing cells are much less affected because their demand for de novo synthesis is lower."

- question: "Why do chemotherapy drugs like 5-fluorouracil and methotrexate preferentially kill rapidly dividing cancer cells rather than non-dividing normal cells?"
  type: short-answer
  answer: "Rapidly dividing cells require massive amounts of new nucleotides to replicate their DNA during each cell cycle. They cannot meet this demand through salvage alone and depend heavily on de novo synthesis pathways. 5-Fluorouracil inhibits thymidylate synthase (blocking dTMP production needed for DNA), and methotrexate blocks dihydrofolate reductase (depleting the folate coenzymes required for purine synthesis and dTMP synthesis). Without these nucleotides, cells cannot replicate their DNA and are forced into arrest or apoptosis. Non-dividing normal cells have low nucleotide demands that can be partially met through salvage pathways and have time to compensate, making them less sensitive to these targeted blocks."
  explanation: "The mechanistic logic applies broadly: any drug that blocks a committed step in de novo nucleotide synthesis will disproportionately harm cells that divide rapidly and therefore have the highest demand for newly synthesized nucleotides. This selectivity is partial — some normal dividing tissues (gut epithelium, bone marrow) are also affected, explaining common chemotherapy side effects like mucositis and myelosuppression."
```

## Explainer

Every time a cell divides, it must duplicate its entire genome — billions of nucleotides assembled with precision. Nucleotides are also the currency of energy transfer (ATP, GTP), signaling (cAMP, cGMP), and coenzyme function (NAD⁺, FAD, CoA). Given your foundation in organic chemistry, you can appreciate that building these complex molecules from scratch is no small feat. Cells solve this challenge through two complementary strategies: **de novo synthesis** (building nucleotides from simple precursors) and **salvage pathways** (recycling bases from degraded nucleic acids).

De novo **purine** synthesis is distinctive because the purine ring is assembled piece by piece *while already attached to ribose-5-phosphate*. The starting material is **PRPP** (5-phosphoribosyl-1-pyrophosphate), and atoms from glutamine, glycine, aspartate, CO₂, and N¹⁰-formyl-THF (a folate derivative) are added in a ten-step sequence to build the first complete purine nucleotide: **IMP** (inosine monophosphate). IMP sits at a branch point — it can be converted to AMP (via aspartate addition) or GMP (via oxidation and amination). Notably, AMP synthesis requires GTP, and GMP synthesis requires ATP, creating a built-in balancing mechanism that keeps purine pools in proportion.

De novo **pyrimidine** synthesis takes the opposite approach: the ring is built first as a free base, and sugar is attached afterward. Carbamoyl phosphate (from glutamine and CO₂) condenses with aspartate to begin ring construction, ultimately producing **orotate** — the completed pyrimidine ring. Only then does orotate react with PRPP to become orotidylate, which is decarboxylated to **UMP**. From UMP, cells produce CTP (by amination of UTP) and the deoxythymidylate (dTMP) needed for DNA synthesis. The enzyme **thymidylate synthase**, which converts dUMP to dTMP using a folate cofactor, is a critical drug target — chemotherapy agents like 5-fluorouracil and methotrexate block this step, starving rapidly dividing cancer cells of the thymidine they need to replicate DNA.

**Salvage pathways** are energetically cheaper alternatives that reclaim free bases (hypoxanthine, guanine, adenine) released during normal nucleic acid turnover and reattach them to PRPP. The enzyme **HGPRT** (hypoxanthine-guanine phosphoribosyltransferase) is the best-known salvage enzyme; its complete deficiency causes Lesch-Nyhan syndrome, a devastating neurological disorder that reveals how dependent the brain is on purine recycling. Both de novo and salvage pathways are regulated by **feedback inhibition** — the end products (AMP, GMP, UMP, CTP) inhibit early committed steps in their own synthesis, ensuring that nucleotide pools stay balanced without overproduction.
