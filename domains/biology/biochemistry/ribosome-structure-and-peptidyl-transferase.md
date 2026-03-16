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
status: draft
---

# Ribosome Structure and Peptidyl Transferase Activity

## Core Idea
The ribosome is a ribozyme: the 28S rRNA (in eukaryotes) catalyzes peptide bond formation between the aminoacyl-tRNA (A site) and the peptidyl-tRNA (P site). rRNA is the catalytic center, not protein. The peptidyl transferase mechanism involves deprotonation of the aminoacyl group, nucleophilic attack on the carbonyl carbon, and tetrahedral intermediate formation.

## Explainer

From your introduction to ribosomes, you know that these massive molecular machines read mRNA and assemble proteins. Now we look at the ribosome's architecture and ask a deeper question: which part of the ribosome actually catalyzes the peptide bond? The surprising answer — one of the most important discoveries in modern biochemistry — is that it is **RNA, not protein**, that performs the catalysis. The ribosome is a **ribozyme**: an RNA enzyme.

The ribosome consists of two subunits. In eukaryotes, the **large subunit (60S)** contains 28S, 5.8S, and 5S rRNA plus ~49 proteins, while the **small subunit (40S)** contains 18S rRNA plus ~33 proteins. (In prokaryotes, the corresponding subunits are 50S and 30S.) The small subunit handles **decoding** — matching each mRNA codon to the correct aminoacyl-tRNA anticodon. The large subunit contains the **peptidyl transferase center (PTC)**, where the actual chemistry of peptide bond formation occurs. Three functionally important sites span both subunits: the **A site** (aminoacyl), where the incoming charged tRNA binds; the **P site** (peptidyl), which holds the tRNA carrying the growing polypeptide chain; and the **E site** (exit), where deacylated tRNA leaves after donating its amino acid.

The peptidyl transferase reaction is a nucleophilic substitution. The **α-amino group** of the aminoacyl-tRNA in the A site is deprotonated and acts as a nucleophile, attacking the **carbonyl carbon** of the ester bond linking the growing peptide to the P-site tRNA. This forms a tetrahedral intermediate that resolves by breaking the ester bond, transferring the entire polypeptide chain to the A-site tRNA and leaving a deacylated tRNA in the P site. The ribosome then translocates one codon forward (driven by EF-G and GTP hydrolysis), moving the peptidyl-tRNA from A to P and the deacylated tRNA from P to E.

The critical evidence that rRNA is the catalyst came from high-resolution crystal structures (Thomas Steitz, Ada Yonath, and Venkatraman Ramakrishnan, Nobel Prize 2009) showing that **no ribosomal protein is within 18 Å of the active site**. The PTC is entirely surrounded by 23S/28S rRNA. The ribosomal proteins serve structural and regulatory roles — stabilizing rRNA folds, facilitating subunit assembly, and assisting factor binding — but the chemistry is RNA's job. This finding strongly supports the **RNA world hypothesis**: if the most fundamental reaction in biology (making proteins) is catalyzed by RNA, then RNA likely preceded proteins as the original catalyst of life. Understanding the PTC also explains why many antibiotics (chloramphenicol, erythromycin, linezolid) work by binding the bacterial PTC and blocking peptide bond formation — they exploit structural differences between bacterial and eukaryotic rRNA to selectively poison bacterial translation.
