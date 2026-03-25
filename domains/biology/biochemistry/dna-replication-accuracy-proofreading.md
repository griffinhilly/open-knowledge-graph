---
id: dna-replication-accuracy-proofreading
title: DNA Replication Accuracy and Proofreading
domain: biology
course: biochemistry
prerequisites:
- id: dna-replication-machinery
  type: hard
builds-toward:
- dna-repair-mechanisms
tags:
- fidelity
- 3' to 5' exonuclease
- mismatch repair
- error rate
stage: formal-systems
status: validated
---

# DNA Replication Accuracy and Proofreading

## Core Idea
DNA polymerases achieve extraordinary accuracy (~1 error per 10¹⁰ nucleotides) through two mechanisms: nucleotide selection (discrimination at insertion) and 3'→5' exonuclease activity (proofreading, removing mismatched bases). Polymerase selectivity for correct base pairs relies on geometry: correct Watson-Crick pairs fit optimally in the polymerase active site, while mismatches are poorly accommodated. Mismatch repair proteins (MutS, MutL, MutH in bacteria; MSH, MLH in eukaryotes) provide a third level of accuracy by detecting and removing errors on the newly synthesized strand.

## Questions

```yaml
- question: "A mutation disables only the 3'→5' exonuclease proofreading activity of DNA polymerase, leaving nucleotide selectivity and mismatch repair fully intact. What would you predict about the organism's overall mutation rate?"
  type: multiple-choice
  options:
    - "No change — the remaining two layers compensate entirely for the loss of proofreading"
    - "A moderate increase of roughly 100-fold, since one of three multiplicative error-correction layers is lost"
    - "An immediately lethal increase in mutations, since proofreading is the essential checkpoint"
    - "A decrease in mutation rate, since removing exonuclease activity prevents deletion errors"
  answer: 1
  explanation: "The three layers — nucleotide selectivity, proofreading, and mismatch repair — each improve fidelity by roughly 100-fold and operate in series. Losing proofreading removes its ~100-fold contribution, raising the overall error rate from ~1 in 10⁹ to ~1 in 10⁷. The remaining two layers still function, so the increase is not catastrophic. This 'layered redundancy' design means each layer is necessary but not solely responsible for genomic stability."

- question: "What is the primary physical basis for DNA polymerase's nucleotide selectivity — its ability to favor correctly matched bases over mismatches?"
  type: multiple-choice
  options:
    - "Hydrogen bonding strength: correct base pairs form more hydrogen bonds than mismatches"
    - "The precise geometric fit of a correct Watson-Crick base pair in the polymerase active site"
    - "Electrostatic repulsion between mismatched bases and the template backbone"
    - "Recognition of a specific chemical signature on the incoming nucleotide's sugar moiety"
  answer: 1
  explanation: "DNA polymerase uses geometric discrimination, not just hydrogen bonding strength. A correct Watson-Crick pair (A-T or G-C) has a precise shape that fits snugly into the active site, positioning the 3'-OH for efficient catalysis. A mismatch distorts this geometry, dramatically slowing the chemical reaction even if some hydrogen bonds still form. This is why G-T wobble pairs, which can form two hydrogen bonds, are still strongly discriminated against — the geometry is wrong even if the bonding is partial."

- question: "The 3'→5' exonuclease proofreading activity that corrects mismatches during DNA replication is located within the same enzyme molecule as the polymerase active site."
  type: true-false
  answer: true
  explanation: "In DNA polymerases I and III (and their eukaryotic counterparts), the 3'→5' exonuclease domain is a physically separate but integral part of the same polypeptide or holoenzyme complex. When a mismatch is detected — signaled by the distorted geometry at the 3' end of the growing strand — the mismatched end is shifted into the exonuclease domain, the error is excised, and synthesis resumes. This 'built-in backspace' function allows immediate correction without requiring a separate enzyme to find and fix the mistake."

- question: "Mismatch repair in bacteria identifies the newly synthesized strand (rather than the template) for correction by detecting nicks and cuts in the new DNA."
  type: true-false
  answer: false
  explanation: "In bacteria, the newly synthesized strand is identified by the absence of methylation. The template strand is methylated at GATC sequences by Dam methylase; the new strand is not yet methylated immediately after synthesis. MutH recognizes this hemimethylated state and cuts the unmethylated (new) strand, directing excision to the correct strand. Eukaryotes use strand discontinuities (nicks) rather than methylation for this purpose. Confusing the two organisms' mechanisms is a common error."

- question: "Why are three successive error-correction layers necessary for DNA replication fidelity, rather than simply engineering a more accurate polymerase active site?"
  type: short-answer
  answer: "Each successive layer catches errors that escaped the previous one, and the layers multiply their effects. Nucleotide selectivity alone achieves about 1 error per 10⁵ nucleotides — impressive but still far too high for a billion-base genome. Proofreading adds another ~100-fold improvement to reach ~1 in 10⁷. Mismatch repair adds a further 100–1000-fold to reach ~1 in 10⁹–10¹⁰. No single mechanism can achieve this level of accuracy on its own because each approach has fundamental physical and kinetic limits. The layered architecture exploits redundancy: rare errors slipping through each layer are caught by the next."
  explanation: "This principle of layered quality control appears throughout biology. Each mechanism operates via a different physical principle — geometric discrimination, exonuclease excision, and post-replication scanning — so their failure modes are largely independent. Losing any one layer still permits the others to function, while combining all three achieves an extraordinary overall fidelity that no single mechanism could approach."
```

## Explainer

From your study of DNA replication machinery, you know that DNA polymerase synthesizes a new strand by adding nucleotides complementary to the template. But consider the scale of the challenge: the human genome contains roughly 6.4 billion base pairs, and every cell division must copy all of them. If the error rate were even one in a million, each division would introduce thousands of mutations — far too many for a complex organism to survive. The cell solves this through three successive layers of error correction, each catching mistakes the previous layer missed.

The first layer is **nucleotide selectivity** at the polymerase active site. DNA polymerase does not simply match bases by hydrogen bonding — it uses the geometry of the entire base pair. A correct Watson-Crick pair (A-T or G-C) has a precise shape that fits snugly into the active site, like a key in a lock. A mismatch distorts this geometry, and the polymerase responds by dramatically slowing the catalytic reaction. This selectivity alone reduces the error rate to roughly one mistake per 10⁵ nucleotides — impressive, but still far too high for a billion-base genome.

The second layer is **3'→5' exonuclease proofreading**. When a mismatched nucleotide is incorporated, the distorted base pair sits poorly in the active site and the polymerase stalls. The mismatched 3' end of the growing strand is then shuttled to a separate exonuclease domain within the same enzyme, which clips off the incorrect nucleotide. The polymerase then re-attempts insertion with the correct base. Think of it as a built-in backspace key — the polymerase can detect its own typo, erase it, and try again. This step improves fidelity by another factor of about 100, bringing the error rate down to roughly one per 10⁷ nucleotides.

The third layer is **mismatch repair (MMR)**, which operates after replication is complete. Specialized proteins scan the newly synthesized DNA for remaining mismatches. In bacteria, MutS recognizes the distortion caused by a mismatch, MutL coordinates the repair, and MutH distinguishes the new strand from the template by detecting methylation patterns (the template strand is methylated, the new strand is not yet). The mismatch is excised from the new strand and resynthesized correctly. Eukaryotes use homologous proteins (MSH and MLH families) and distinguish strands by the presence of nicks in the newly synthesized strand. This final checkpoint reduces the error rate by another factor of 100–1000, achieving the extraordinary overall fidelity of approximately one error per 10⁹ to 10¹⁰ base pairs copied.

Together, these three mechanisms form a hierarchy of quality control: selectivity prevents most errors, proofreading catches the ones that slip through, and mismatch repair sweeps up the rest. When any layer fails — as when MMR genes are mutated in hereditary nonpolyposis colorectal cancer (Lynch syndrome) — mutation rates climb dramatically, illustrating how essential each layer is to genomic stability.
