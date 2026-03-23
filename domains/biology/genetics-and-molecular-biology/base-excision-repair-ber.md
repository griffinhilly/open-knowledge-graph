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
stage: formal-systems
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

## Questions

```yaml
- question: "A cell's DNA contains an 8-oxoguanine residue resulting from oxidative damage. In the base excision repair (BER) pathway, which enzymatic event must occur FIRST?"
  type: multiple-choice
  options:
    - "AP endonuclease cleaves the DNA backbone at the position of the damaged base"
    - "A specific DNA glycosylase recognizes and removes the 8-oxoguanine base, creating an AP site"
    - "DNA polymerase β fills in the one-nucleotide gap using the complementary strand as template"
    - "DNA ligase III seals the nick in the backbone to restore the continuous double helix"
  answer: 1
  explanation: "BER proceeds in a strict sequence: (1) glycosylase removes the damaged base, creating an AP site; (2) AP endonuclease cleaves the backbone at the AP site; (3) DNA polymerase β fills in the gap; (4) ligase seals the nick. The glycosylase step must come first because the AP site it creates is the substrate for AP endonuclease. Understanding this order matters clinically — tumors deficient in specific glycosylases accumulate particular mutation patterns that reveal which glycosylase is compromised."

- question: "Why does base excision repair use multiple different DNA glycosylases rather than a single enzyme capable of recognizing all damaged bases?"
  type: multiple-choice
  options:
    - "Different glycosylases operate at different pH levels, allowing BER to function across different cellular compartments"
    - "Each glycosylase is structurally adapted — through its active site geometry — to recognize and excise a specific type of chemically altered base"
    - "Multiple glycosylases increase overall repair speed through redundancy, ensuring no lesion is missed"
    - "Specialized glycosylases are only expressed in tissues at highest risk for each specific type of damage"
  answer: 1
  explanation: "Each DNA glycosylase has evolved a specific active site architecture that recognizes the distortion or chemical alteration of a particular damaged base — 8-oxoguanine glycosylase (OGG1) recognizes the oxidized guanine, MUTYH removes adenine mispaired with 8-oxoguanine, UNG removes uracil from DNA. This specialization is necessary because each lesion presents a distinct chemical structure. A single glycosylase capable of recognizing all damaged bases would require an implausibly flexible active site. The multiplicity of glycosylases is what allows BER to handle the wide variety of small, non-helix-distorting lesions that accumulate from oxidative stress, spontaneous deamination, and alkylation."

- question: "An AP (apurinic/apyrimidinic) site — a position in the DNA strand that retains the sugar-phosphate backbone but has no base — is a normal, intentionally created intermediate in the BER pathway."
  type: true-false
  answer: true
  explanation: "Correct. The AP site is not a secondary damage event; it is the product of the first repair step. DNA glycosylase intentionally cleaves the N-glycosidic bond between the damaged base and the deoxyribose sugar, removing the base and leaving the AP site. The AP site then serves as the substrate for AP endonuclease, which cleaves the backbone. This staged approach — removing the damaged base first, then dealing with the backbone — is what distinguishes BER from NER and allows BER to operate with minimal disruption to the double helix."

- question: "Base excision repair (BER) and nucleotide excision repair (NER) are functionally redundant pathways that handle the same spectrum of DNA lesions, providing backup when one pathway is compromised."
  type: true-false
  answer: false
  explanation: "BER and NER are complementary, not redundant — they handle different classes of damage. BER handles small, chemically subtle lesions that do not significantly distort the DNA helix: oxidized bases (8-oxoguanine), deaminated bases (uracil, hypoxanthine), and alkylated bases. It replaces 1-10 nucleotides. NER handles bulky, helix-distorting lesions like UV-induced cyclobutane pyrimidine dimers, cisplatin-induced intrastrand crosslinks, and large chemical adducts; it excises an ~25-nucleotide single-stranded patch. Their substrates rarely overlap, which is why deficiency in one does not generally upregulate the other."

- question: "Explain why BER removes the damaged base before cutting the backbone, rather than excising a stretch of nucleotides around the lesion as NER does, and what advantage this strategy provides."
  type: short-answer
  answer: "BER removes only the damaged base first (via glycosylase), then cuts the backbone specifically at the resulting AP site, replacing just 1 nucleotide. This minimizes the amount of DNA that must be resynthesized and reduces the risk of introducing errors. NER excises ~25 nucleotides because bulky helix-distorting lesions require this larger excision to release the lesion. BER's more surgical approach works precisely because its substrates are small lesions that do not distort the helix — the glycosylase can access and remove the individual damaged base without needing to clear a large surrounding segment."
  explanation: "The evolutionary logic is efficiency: oxidative damage occurs thousands of times per cell per day, so BER must be fast, accurate, and low-cost. Replacing one nucleotide is cheaper than replacing 25, requires less error-prone gap-filling, and minimizes the risk of single-strand breaks accumulating (multiple simultaneous single-strand breaks in close proximity can be converted to a double-strand break during replication, which is far more dangerous). BER's minimalism is matched to the frequency and nature of its substrates."
```

## Explainer

From your study of DNA repair mechanisms, you know that cells face constant DNA damage and have evolved multiple repair pathways to deal with different types of lesions. **Base excision repair (BER)** is the pathway specialized for small, chemically subtle lesions — damaged bases that don't dramatically distort the DNA helix but would cause mutations if left unrepaired. The most common of these are oxidative lesions like **8-oxoguanine** (produced thousands of times per cell per day by reactive oxygen species) and **deaminated bases** like uracil (produced when cytosine spontaneously loses its amino group).

The BER pathway works like a surgical extraction in four steps. First, a **DNA glycosylase** recognizes and removes the damaged base by cleaving the bond between the base and the sugar, leaving the sugar-phosphate backbone intact. This creates an **apurinic/apyrimidinic (AP) site** — a position in the DNA that has a sugar and phosphate but no base. Think of it as pulling a rotten tooth but leaving the socket. There are at least 11 different glycosylases in human cells, each specialized for recognizing specific types of base damage — this specificity is what allows BER to handle a wide variety of small lesions. Second, **AP endonuclease** (APE1 in humans) cleaves the backbone at the AP site, creating a single-strand nick with a free 3'-OH end. Third, **DNA polymerase β** fills in the one-nucleotide gap with the correct base using the undamaged complementary strand as a template. Finally, **DNA ligase III** (working with its partner XRCC1) seals the remaining nick, restoring the continuous double helix.

This "short-patch" pathway replaces just a single nucleotide and handles the vast majority of BER events. However, some lesions produce modified sugar residues that polymerase β cannot process. In these cases, cells switch to **long-patch BER**, where a replicative polymerase (Pol δ or Pol ε) displaces a flap of 2-10 nucleotides, FEN1 endonuclease trims the flap, and DNA ligase I seals the result. Long-patch BER is more complex but handles the edge cases that short-patch cannot.

The clinical significance of BER is substantial. Because oxidative damage is relentless — a byproduct of normal aerobic metabolism — any weakness in BER leads to mutation accumulation. Variants in BER genes (particularly MUTYH, a glycosylase that removes adenine mispaired with 8-oxoguanine) are associated with colorectal cancer predisposition. Understanding BER also clarifies why it differs from nucleotide excision repair (NER): BER removes the damaged *base* first and then deals with the backbone, replacing just 1-10 nucleotides, while NER excises an entire ~25-nucleotide stretch of the strand containing the lesion. BER handles small, non-distorting damage; NER handles bulky, helix-distorting lesions. The two pathways are complementary, not redundant.
