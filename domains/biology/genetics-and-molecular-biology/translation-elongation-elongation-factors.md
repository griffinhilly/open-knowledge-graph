---
id: translation-elongation-elongation-factors
title: Translation Elongation and Elongation Factors
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: ribosomal-initiation-factors-tRNA
  type: hard
builds-toward:
- translation-termination-stop-codons-release-factors
tags:
- translation
- elongation-factors
- ribosome
- protein-synthesis
stage: advanced
status: draft
---

# Translation Elongation and Elongation Factors

## Core Idea
During elongation, EF-Tu (prokaryotes) or eEF1A (eukaryotes) delivers aminoacyl-tRNA to the ribosomal A site in a GTP-dependent manner. GTP hydrolysis occurs upon correct codon-anticodon pairing (proofreading step). EF-G (prokaryotes) or eEF2 (eukaryotes) then catalyzes translocation of tRNAs and mRNA, advancing the ribosome by one codon.

## How It's Best Learned
Use cryo-EM structures or animations to visualize the three-site model of the ribosome (A, P, E). Trace the movement of tRNAs and mRNA through successive cycles. Understand how GTP hydrolysis provides energy and ensures fidelity.

## Common Misconceptions
- Assuming elongation is a single step when it involves multiple distinct phases (A/T binding, proofreading, translocation).
- Not recognizing that the ribosome actively discriminates against cognate codons through induced-fit proofreading.
- Thinking elongation factors bind permanently to the ribosome when they associate and dissociate with each cycle.

## Explainer

From your study of translation initiation, you know that the ribosome assembles on the mRNA with the initiator tRNA positioned in the **P site** (peptidyl site), base-paired with the start codon. The A site (aminoacyl site) is empty and ready to accept the next aminoacyl-tRNA. Elongation is the repetitive cycle that builds the polypeptide chain one amino acid at a time, and it proceeds through three distinct steps: codon-directed binding, peptide bond formation, and translocation.

In the first step, an aminoacyl-tRNA does not simply float into the A site on its own. Instead, the elongation factor **EF-Tu** (in prokaryotes) or **eEF1A** (in eukaryotes) delivers it in a complex with GTP. Think of EF-Tu as an escort with a security clearance — it brings the charged tRNA to the ribosome and holds it in position while the ribosome checks whether the anticodon matches the codon in the A site. If the match is correct, the geometry of the codon-anticodon interaction triggers a conformational change in the ribosome that stimulates **GTP hydrolysis** on EF-Tu. This is the proofreading step: the energy of GTP hydrolysis is used not to form the peptide bond itself, but to introduce a kinetic delay that gives incorrectly matched tRNAs time to dissociate before the irreversible step. Only after GTP hydrolysis and EF-Tu release is the aminoacyl-tRNA fully accommodated into the A site.

Once the correct aminoacyl-tRNA is in the A site, **peptidyl transferase** — an activity of the ribosomal RNA itself (making the ribosome a ribozyme) — catalyzes formation of a peptide bond between the amino acid on the A-site tRNA and the growing polypeptide chain attached to the P-site tRNA. The polypeptide is transferred from the P-site tRNA to the A-site tRNA, leaving a deacylated (empty) tRNA in the P site. At this point, the ribosome is in a hybrid state — the tRNAs have shifted relative to the large subunit but not yet relative to the small subunit.

The final step of each cycle is **translocation**, driven by the elongation factor **EF-G** (prokaryotes) or **eEF2** (eukaryotes). EF-G binds the ribosome with GTP and, upon hydrolysis, physically moves the ribosome one codon down the mRNA. The deacylated tRNA shifts from the P site to the **E site** (exit site) and is released, the peptidyl-tRNA moves from A to P, and a new codon is exposed in the empty A site. The entire cycle then repeats — at a remarkable rate of about 15–20 amino acids per second in bacteria. Each elongation factor participates transiently: EF-Tu and EF-G bind, do their work, and dissociate within each cycle. EF-Tu is recharged by the exchange factor **EF-Ts**, which swaps GDP for GTP, readying EF-Tu for another round of tRNA delivery.
