---
id: protein-translocation-and-signal-sequences
title: Protein Translocation and Signal Sequences
domain: biology
course: biochemistry
prerequisites:
- id: protein-targeting-and-subcellular-localization
  type: hard
builds-toward:
- post-translational-modifications
tags:
- signal-sequence
- translocation
- ER
- mitochondria
stage: advanced
status: draft
---

# Protein Translocation and Signal Sequences

## Core Idea
Signal sequences direct nascent polypeptides to their destination during translation. N-terminal signal sequences are recognized by Signal Recognition Particle (SRP), halting translation and directing the ribosome to the ER for co-translational translocation. Mitochondrial targeting sequences and other organellar signals direct post-translational import via translocase complexes.

## Explainer

You already know from protein targeting that cells route newly synthesized proteins to specific compartments — the ER, mitochondria, nucleus, peroxisomes, or the plasma membrane. But how does a protein physically cross a lipid bilayer? Folded proteins are large, hydrophilic objects that cannot passively diffuse through the hydrophobic core of a membrane. The answer lies in **signal sequences** — short stretches of amino acids that act as molecular zip codes — and **translocon channels** that provide a protein-conducting pore through the membrane.

The best-characterized pathway is **co-translational translocation** into the endoplasmic reticulum. It begins while the protein is still being synthesized on the ribosome. As the N-terminal **signal sequence** (typically 16–30 amino acids with a hydrophobic core) emerges from the ribosomal exit tunnel, it is recognized by the **Signal Recognition Particle (SRP)**, a ribonucleoprotein complex. SRP binding does two things simultaneously: it pauses translation (preventing the protein from folding prematurely in the cytosol) and it targets the entire ribosome-mRNA-nascent chain complex to the **SRP receptor** on the ER membrane. Think of SRP as a shuttle bus that recognizes passengers by their boarding pass (the signal sequence) and delivers them to the correct terminal.

Once docked at the ER, the ribosome hands off the nascent chain to the **Sec61 translocon**, a protein-conducting channel embedded in the ER membrane. Translation resumes, and the growing polypeptide is threaded through the channel into the ER lumen as it is synthesized — hence "co-translational." The signal sequence is typically cleaved by **signal peptidase** on the lumenal side, so the mature protein no longer carries its zip code. For transmembrane proteins, hydrophobic **stop-transfer anchor sequences** within the polypeptide cause the translocon to open laterally, releasing transmembrane segments into the lipid bilayer while allowing other segments to remain on the cytosolic or lumenal side.

**Post-translational translocation** operates differently. Proteins destined for mitochondria, chloroplasts, or peroxisomes are synthesized completely on free ribosomes in the cytosol, then imported after translation is finished. Mitochondrial **targeting sequences** (positively charged, amphipathic helices at the N-terminus) are recognized by the **TOM complex** (translocase of the outer membrane) and passed to **TIM complexes** (translocase of the inner membrane). Because the protein must remain unfolded to thread through these channels, cytosolic **chaperones** (particularly Hsp70) keep the polypeptide in an import-competent state. The energy for import comes from ATP hydrolysis by mitochondrial Hsp70 on the matrix side, which ratchets the protein inward. The key conceptual distinction is timing: ER-targeted proteins are translocated as they are made, while organellar proteins are translocated after they are made, requiring chaperone assistance to prevent premature folding.
