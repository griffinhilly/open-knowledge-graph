---
id: bacterial-ribosomes-and-translation-prokaryotes
title: Bacterial Ribosomes and Protein Synthesis
domain: biology
course: microbiology
prerequisites:
- id: ribosome-structure-and-peptidyl-transferase
  type: hard
- id: translation
  type: hard
builds-toward:
- aminoglycoside-ribosome-inhibition
- bacterial-protein-secretion-pathways
tags:
- ribosomes
- translation
- 70s
stage: formal-systems
status: draft
---

# Bacterial Ribosomes and Protein Synthesis

## Core Idea
Bacterial ribosomes are 70S (smaller than eukaryotic 80S) and consist of 30S and 50S subunits. This structural difference allows selective inhibition by antibiotics like tetracycline and streptomycin, which bind prokaryotic but not eukaryotic ribosomes. Bacteria couple transcription and translation, allowing rapid protein synthesis.

## Explainer

You already understand the general mechanism of translation from your biochemistry prerequisites — ribosomes read mRNA codons and catalyze peptide bond formation between amino acids delivered by tRNA. The bacterial ribosome performs this same fundamental chemistry, but its structure differs from the eukaryotic ribosome in ways that have profound consequences for medicine.

The bacterial ribosome sediments at **70S** (Svedberg units, a measure of size and shape during centrifugation) and is composed of two subunits: the **30S small subunit** (containing 16S rRNA and 21 proteins) and the **50S large subunit** (containing 23S rRNA, 5S rRNA, and 31 proteins). Compare this to the eukaryotic **80S** ribosome with its 40S and 60S subunits. The "S" values do not add up because sedimentation depends on shape as well as mass. What matters is that the structural differences between 70S and 80S ribosomes — particularly in their rRNA sequences and binding pockets — allow antibiotics to target bacterial ribosomes without poisoning the patient's own protein synthesis machinery. This principle of **selective toxicity** is the foundation of antibiotic therapy.

Multiple antibiotic classes exploit these structural differences. **Aminoglycosides** (like streptomycin and gentamicin) bind the 30S subunit's decoding site, causing misreading of mRNA codons — the ribosome inserts wrong amino acids, producing nonfunctional or toxic proteins. **Tetracyclines** also target the 30S subunit but block the A site, preventing aminoacyl-tRNA from binding. **Macrolides** (like erythromycin) and **chloramphenicol** bind the 50S subunit near the peptidyl transferase center, blocking peptide bond formation or translocation. Each drug exploits a specific pocket or interaction surface that differs between prokaryotic and eukaryotic ribosomes.

Another critical difference is that bacteria lack a nuclear envelope, so **transcription and translation are coupled** — ribosomes begin translating an mRNA while RNA polymerase is still transcribing it. This coupling allows extraordinarily rapid gene expression: a bacterium can go from environmental signal to functional protein in minutes. It also means that regulation mechanisms differ fundamentally from eukaryotes. Bacterial operons, riboswitches, and attenuation all exploit this coupling. Understanding these structural and organizational differences is not just an academic exercise — it explains why we can treat bacterial infections with antibiotics, why mitochondrial ribosomes (which are also 70S, reflecting their bacterial ancestry) can be affected by certain antibiotics as a side effect, and why resistance mutations in ribosomal RNA genes can render entire drug classes ineffective.
