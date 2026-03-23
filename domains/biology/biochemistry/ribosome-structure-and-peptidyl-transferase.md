---
id: ribosome-structure-and-peptidyl-transferase
title: Ribosome Structure and Peptidyl Transferase Activity
domain: biology
course: biochemistry
prerequisites:
- id: ribosomes-and-protein-synthesis-intro
  type: hard
- id: translation-initiation-and-elongation
  type: soft
tags:
- ribosome
- rRNA
- peptidyl-transferase
stage: advanced
status: validated
---

# Ribosome Structure and Peptidyl Transferase Activity

## Core Idea
The ribosome is a ribozyme: the 28S rRNA (in eukaryotes) catalyzes peptide bond formation between the aminoacyl-tRNA (A site) and the peptidyl-tRNA (P site). rRNA is the catalytic center, not protein. The peptidyl transferase mechanism involves deprotonation of the aminoacyl group, nucleophilic attack on the carbonyl carbon, and tetrahedral intermediate formation.

## Questions

```yaml
- question: "What is the strongest evidence that rRNA — not ribosomal proteins — catalyzes peptide bond formation?"
  type: multiple-choice
  options:
    - "rRNA is more abundant by mass than ribosomal proteins in the large subunit"
    - "High-resolution crystal structures show no ribosomal protein within 18 Å of the peptidyl transferase center"
    - "Ribosomal proteins can be completely removed without stopping translation"
    - "rRNA sequences are more evolutionarily conserved than ribosomal protein sequences"
  answer: 1
  explanation: "Crystal structures solved by Steitz, Yonath, and Ramakrishnan (Nobel 2009) placed every atom in the ribosome and showed that the active site is entirely surrounded by 23S/28S rRNA — no protein is close enough to contact the reacting groups. This structural evidence directly shows rRNA is the catalyst. The other options are partially true but not the decisive evidence: ribosomal proteins stabilize rRNA folds and assist factor binding, but they cannot be fully stripped without disrupting the ribosome's structure."

- question: "A researcher treats ribosomes with a drug that specifically cross-links and inactivates all ribosomal proteins, leaving rRNA intact. What would you predict about peptide bond formation?"
  type: multiple-choice
  options:
    - "Peptide bond formation stops entirely, because the proteins are the enzymes"
    - "Peptide bond formation continues, because the catalytic activity resides in the rRNA of the peptidyl transferase center"
    - "Peptide bond formation slows by about half, because proteins enhance rRNA catalysis"
    - "Peptide bond formation accelerates, because the proteins were inhibiting rRNA activity"
  answer: 1
  explanation: "The peptidyl transferase center (PTC) is a ribozyme — RNA does the chemistry. Ribosomal proteins serve structural and regulatory roles (stabilizing rRNA folds, facilitating factor binding, assisting subunit assembly) but are not within catalytic distance of the active site. This is a direct application of the ribosome-as-ribozyme concept. Option C is the most tempting wrong answer, implying a protein-rRNA partnership, but the crystal structure evidence shows proteins are not needed for catalysis."

- question: "The peptidyl transferase center is located in the small (40S) ribosomal subunit, which is responsible for decoding mRNA and catalyzing peptide bond formation."
  type: true-false
  answer: false
  explanation: "The small subunit (40S in eukaryotes, 30S in prokaryotes) handles decoding — matching mRNA codons to aminoacyl-tRNA anticodons. The peptidyl transferase center resides in the large subunit (60S in eukaryotes, 50S in prokaryotes), which contains the A, P, and E sites for tRNA binding and where the 28S/23S rRNA catalyzes peptide bond formation."

- question: "The discovery that the ribosome is a ribozyme provides support for the RNA world hypothesis, because it demonstrates that RNA can catalyze the central biochemical reaction of protein synthesis."
  type: true-false
  answer: true
  explanation: "If RNA catalyzes the most fundamental biosynthetic reaction in all of biology — making proteins — then RNA likely preceded proteins as the original catalyst of life. Proteins require ribosomes (RNA) to be made, but ribosomes do not require proteins for their catalytic function. This chicken-and-egg relationship is dissolved if RNA came first: an RNA world could have developed ribozyme-based protein synthesis before protein enzymes took over most other catalytic roles."

- question: "Describe the mechanism of peptide bond formation at the peptidyl transferase center: what acts as the nucleophile, what is the electrophile, and what is the chemical outcome?"
  type: short-answer
  answer: "The α-amino group of the aminoacyl-tRNA in the A site is the nucleophile (after deprotonation by the rRNA). The electrophile is the carbonyl carbon of the ester bond linking the growing polypeptide chain to the P-site tRNA. Nucleophilic attack forms a tetrahedral intermediate that resolves by breaking the P-site ester bond, transferring the entire polypeptide to the A-site tRNA. The P-site tRNA is left deacylated; the A-site tRNA now carries the elongated peptide chain."
  explanation: "This is a nucleophilic acyl substitution: the ester bond between the peptide and the P-site tRNA is replaced by an amide bond (peptide bond) between the last amino acid of the growing chain and the new amino acid on the A-site tRNA. The ribosome then translocates, moving the peptidyl-tRNA from A to P and the deacylated tRNA from P to E, ready for the next elongation cycle."
```

## Explainer

From your introduction to ribosomes, you know that these massive molecular machines read mRNA and assemble proteins. Now we look at the ribosome's architecture and ask a deeper question: which part of the ribosome actually catalyzes the peptide bond? The surprising answer — one of the most important discoveries in modern biochemistry — is that it is **RNA, not protein**, that performs the catalysis. The ribosome is a **ribozyme**: an RNA enzyme.

The ribosome consists of two subunits. In eukaryotes, the **large subunit (60S)** contains 28S, 5.8S, and 5S rRNA plus ~49 proteins, while the **small subunit (40S)** contains 18S rRNA plus ~33 proteins. (In prokaryotes, the corresponding subunits are 50S and 30S.) The small subunit handles **decoding** — matching each mRNA codon to the correct aminoacyl-tRNA anticodon. The large subunit contains the **peptidyl transferase center (PTC)**, where the actual chemistry of peptide bond formation occurs. Three functionally important sites span both subunits: the **A site** (aminoacyl), where the incoming charged tRNA binds; the **P site** (peptidyl), which holds the tRNA carrying the growing polypeptide chain; and the **E site** (exit), where deacylated tRNA leaves after donating its amino acid.

The peptidyl transferase reaction is a nucleophilic substitution. The **α-amino group** of the aminoacyl-tRNA in the A site is deprotonated and acts as a nucleophile, attacking the **carbonyl carbon** of the ester bond linking the growing peptide to the P-site tRNA. This forms a tetrahedral intermediate that resolves by breaking the ester bond, transferring the entire polypeptide chain to the A-site tRNA and leaving a deacylated tRNA in the P site. The ribosome then translocates one codon forward (driven by EF-G and GTP hydrolysis), moving the peptidyl-tRNA from A to P and the deacylated tRNA from P to E.

The critical evidence that rRNA is the catalyst came from high-resolution crystal structures (Thomas Steitz, Ada Yonath, and Venkatraman Ramakrishnan, Nobel Prize 2009) showing that **no ribosomal protein is within 18 Å of the active site**. The PTC is entirely surrounded by 23S/28S rRNA. The ribosomal proteins serve structural and regulatory roles — stabilizing rRNA folds, facilitating subunit assembly, and assisting factor binding — but the chemistry is RNA's job. This finding strongly supports the **RNA world hypothesis**: if the most fundamental reaction in biology (making proteins) is catalyzed by RNA, then RNA likely preceded proteins as the original catalyst of life. Understanding the PTC also explains why many antibiotics (chloramphenicol, erythromycin, linezolid) work by binding the bacterial PTC and blocking peptide bond formation — they exploit structural differences between bacterial and eukaryotic rRNA to selectively poison bacterial translation.
