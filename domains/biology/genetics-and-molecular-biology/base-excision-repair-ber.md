---
id: base-excision-repair-ber
title: Base Excision Repair (BER) for Oxidative Damage
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: dna-repair-mechanisms
  type: hard
builds-toward:
- mismatch-repair-mlh-msh
tags:
- dna-repair
- base-excision-repair
- ber
- oxidative-damage
stage: advanced
status: draft
---

# Base Excision Repair (BER) for Oxidative Damage

## Core Idea
BER removes small lesions such as oxidized bases (e.g., 8-oxoguanine) and spontaneous deamination products. DNA glycosylase recognizes and removes the damaged base, creating an apurinic/apyrimidinic (AP) site. AP endonuclease then cleaves the backbone, and the gap is filled by polymerase and sealed by ligase.

## How It's Best Learned
Learn the series of enzymatic steps: glycosylase excision, AP site processing, gap fill-in, and ligation. Understand how multiple glycosylases recognize different base lesions. Consider the evolutionary advantage of removing bases vs. nucleotides (BER vs. NER).

## Common Misconceptions
- Assuming BER handles only oxidative damage when it also processes spontaneous deamination and other lesions.
- Not recognizing that single-strand breaks, if abundant, can be converted to double-strand breaks during replication.
- Thinking all BER is faithful; some variants use error-prone polymerases for translesion synthesis.

## Explainer

From your study of DNA repair mechanisms, you know that cells face constant DNA damage and have evolved multiple repair pathways to deal with different types of lesions. **Base excision repair (BER)** is the pathway specialized for small, chemically subtle lesions — damaged bases that don't dramatically distort the DNA helix but would cause mutations if left unrepaired. The most common of these are oxidative lesions like **8-oxoguanine** (produced thousands of times per cell per day by reactive oxygen species) and **deaminated bases** like uracil (produced when cytosine spontaneously loses its amino group).

The BER pathway works like a surgical extraction in four steps. First, a **DNA glycosylase** recognizes and removes the damaged base by cleaving the bond between the base and the sugar, leaving the sugar-phosphate backbone intact. This creates an **apurinic/apyrimidinic (AP) site** — a position in the DNA that has a sugar and phosphate but no base. Think of it as pulling a rotten tooth but leaving the socket. There are at least 11 different glycosylases in human cells, each specialized for recognizing specific types of base damage — this specificity is what allows BER to handle a wide variety of small lesions. Second, **AP endonuclease** (APE1 in humans) cleaves the backbone at the AP site, creating a single-strand nick with a free 3'-OH end. Third, **DNA polymerase β** fills in the one-nucleotide gap with the correct base using the undamaged complementary strand as a template. Finally, **DNA ligase III** (working with its partner XRCC1) seals the remaining nick, restoring the continuous double helix.

This "short-patch" pathway replaces just a single nucleotide and handles the vast majority of BER events. However, some lesions produce modified sugar residues that polymerase β cannot process. In these cases, cells switch to **long-patch BER**, where a replicative polymerase (Pol δ or Pol ε) displaces a flap of 2-10 nucleotides, FEN1 endonuclease trims the flap, and DNA ligase I seals the result. Long-patch BER is more complex but handles the edge cases that short-patch cannot.

The clinical significance of BER is substantial. Because oxidative damage is relentless — a byproduct of normal aerobic metabolism — any weakness in BER leads to mutation accumulation. Variants in BER genes (particularly MUTYH, a glycosylase that removes adenine mispaired with 8-oxoguanine) are associated with colorectal cancer predisposition. Understanding BER also clarifies why it differs from nucleotide excision repair (NER): BER removes the damaged *base* first and then deals with the backbone, replacing just 1-10 nucleotides, while NER excises an entire ~25-nucleotide stretch of the strand containing the lesion. BER handles small, non-distorting damage; NER handles bulky, helix-distorting lesions. The two pathways are complementary, not redundant.
