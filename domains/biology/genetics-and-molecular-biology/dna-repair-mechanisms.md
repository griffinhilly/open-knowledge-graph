---
id: dna-repair-mechanisms
title: DNA Repair Mechanisms
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: dna-mutations
  type: hard
- id: dna-replication
  type: hard
- id: enzyme-structure-and-function
  type: soft
builds-toward:
- genomics-overview
tags:
- DNA repair
- mismatch repair
- base excision
- nucleotide excision
- homologous recombination
stage: advanced
status: validated
---

# DNA Repair Mechanisms

## Core Idea
Cells possess multiple repair pathways to correct DNA damage before it becomes a permanent mutation. Mismatch repair (MMR) corrects base-pairing errors introduced during replication. Base excision repair (BER) removes small damaged bases, while nucleotide excision repair (NER) handles bulky lesions such as UV-induced thymine dimers. Double-strand breaks — the most dangerous lesion — are repaired by homologous recombination (high-fidelity, uses sister chromatid) or non-homologous end joining (error-prone). Defects in repair genes underlie many hereditary cancer predispositions, including Lynch syndrome (MMR) and xeroderma pigmentosum (NER).

## How It's Best Learned
Compare the substrates, enzymes, and fidelity of each major repair pathway in a table. Connect repair defects to cancer syndromes to appreciate the clinical relevance.

## Common Misconceptions
- Repair is not perfect; low-fidelity repair (NHEJ) can introduce mutations while fixing the break.
- UV light causes thymine dimers, not directly strand breaks; this requires NER for correction.

## Questions

```yaml
- question: "Which DNA repair pathway specifically recognizes and removes UV-induced thymine dimers?"
  type: multiple-choice
  options: ["Mismatch repair (MMR)", "Base excision repair (BER)", "Nucleotide excision repair (NER)", "Non-homologous end joining (NHEJ)"]
  answer: 2
  explanation: "Thymine dimers are bulky helix-distorting lesions caused by UV cross-linking of adjacent thymines. NER recognizes helix distortion rather than specific chemical damage, cuts out a ~25-30 nucleotide patch surrounding the lesion, and resynthesizes using the complementary strand. Xeroderma pigmentosum results from NER defects."

- question: "Non-homologous end joining (NHEJ) is a high-fidelity repair mechanism that perfectly restores the original DNA sequence at a double-strand break."
  type: true-false
  answer: false
  explanation: "NHEJ is error-prone: it ligates broken ends directly without a homologous template, often introducing small insertions or deletions at the junction. Unlike homologous recombination, which uses the sister chromatid as a high-fidelity guide, NHEJ trades accuracy for availability — it operates throughout the cell cycle but at the cost of sequence integrity."

- question: "Why is homologous recombination considered higher-fidelity repair than non-homologous end joining for double-strand breaks?"
  type: short-answer
  answer: "Homologous recombination uses the intact sister chromatid as a template, allowing the broken sequence to be copied back accurately. NHEJ ligates broken ends without a template, so small insertions or deletions at the join are common."
  explanation: "The fidelity of HR comes from copying information from an identical intact molecule. NHEJ has no such reference, so it re-joins whatever ends are available — sometimes imprecisely. This is why HR is preferred in S/G2 phase when sister chromatids are available, while NHEJ is the fallback in G1."
```

## Explainer

Every day, the DNA in each of your cells is damaged thousands of times by metabolic byproducts, UV radiation, and replication errors. If even a fraction of these lesions became permanent mutations, cancer and cellular dysfunction would be far more frequent than they are. The reason they are not is a layered triage system of repair pathways, each specialized for a particular category of damage and each trading off speed, accuracy, and cellular cost.

The most elegant pathway is mismatch repair (MMR), which catches errors left by the replication machinery after it has already finished. The replication polymerase makes roughly one uncorrected error per billion base pairs copied — already impressively rare — but MMR reduces this further by scanning newly synthesized DNA for base-pair mismatches. A key challenge is distinguishing the newly synthesized (potentially erroneous) strand from the template (correct) strand; in bacteria, methylation marks the older strand. In humans, strand discrimination relies on nicks and other signals at the replication fork. Inherited defects in MMR genes such as MLH1 and MSH2 cause Lynch syndrome, dramatically raising lifetime colorectal cancer risk.

For individual damaged bases, base excision repair (BER) provides a precise scalpel: a DNA glycosylase enzyme recognizes the specific chemically altered base, flips it out of the helix, and clips the glycosidic bond. The resulting abasic site is then processed by an AP endonuclease, and DNA polymerase fills in the single-nucleotide gap. Nucleotide excision repair (NER) handles larger, helix-distorting lesions that BER cannot manage — most importantly, the thymine dimers caused by UV light, where two adjacent thymines on the same strand become covalently cross-linked. Rather than removing one base, NER excises a patch of 25–30 nucleotides and resynthesizes the region using the undamaged complementary strand as a template. The disease xeroderma pigmentosum — where patients develop skin cancers at extreme rates after even minimal sun exposure — results from inherited NER defects.

Double-strand breaks are the most dangerous lesion because no intact complementary strand exists at the break site to guide repair. Homologous recombination (HR) resolves this by searching the genome for a nearly identical sequence on the sister chromatid (available after S phase) and using it as a template for high-fidelity repair. Non-homologous end joining (NHEJ) provides a faster but riskier alternative: it simply ligates the two broken ends together, often introducing small insertions or deletions at the junction. NHEJ operates throughout the cell cycle and handles the majority of double-strand breaks, but its error-proneness means it can generate chromosomal rearrangements — a common early step in cancer development. The broader lesson is that repair is not a single perfect system but a collection of specialized, imperfect pathways that collectively keep mutation rates low enough for complex life to function.

