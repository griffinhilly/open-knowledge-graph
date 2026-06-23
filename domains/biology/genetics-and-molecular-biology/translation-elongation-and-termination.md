---
id: translation-elongation-and-termination
title: 'Translation Elongation and Termination: Peptide Bond Formation'
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: translation-initiation-and-elongation
  type: hard
- id: ribosomal-rna-and-ribosome-assembly
  type: soft
- id: genetic-code-reading-frame-wobble
  type: soft
- id: translation-initiation-start-codon
  type: hard
builds-toward:
- post-translational-modifications
tags:
- elongation-factors
- peptidyl-transferase
- translocase
- release-factors
- stop-codons
stage: formal-systems
status: validated
---

# Translation Elongation and Termination: Peptide Bond Formation

## Core Idea
During translation elongation, aminoacyl-tRNAs are delivered to the A (acceptor) site of the ribosome by elongation factors EF-Tu (prokaryotes) or eEF1A (eukaryotes) in a GTP-dependent manner, with proofreading ensuring accuracy. The peptidyl transferase activity of the ribosome (catalyzed by 23S rRNA in prokaryotes, 28S rRNA in eukaryotes) catalyzes peptide bond formation between the carboxyl group of the P-site peptidyl-tRNA and the amino group of the A-site aminoacyl-tRNA. Elongation factors EF-G (prokaryotes) or eEF2 (eukaryotes) promote translocation, moving tRNAs and mRNA by three nucleotides (one codon), using GTP hydrolysis. Termination occurs when a stop codon (UAA, UAG, or UGA) enters the A site, recognized by release factors (RF1/RF2 in prokaryotes, eRF1/eRF3 in eukaryotes), triggering hydrolysis of the ester bond linking the polypeptide to the tRNA and dissociation of the ribosome from mRNA.

## Questions

```yaml
- question: "A drug blocks peptide bond formation during translation without affecting tRNA delivery, GTP hydrolysis, or translocation. What is the drug's most likely target?"
  type: multiple-choice
  options:
    - "EF-Tu, the elongation factor that delivers aminoacyl-tRNAs to the A site"
    - "The peptidyl transferase center — specifically the 23S (or 28S) rRNA that catalyzes the reaction"
    - "EF-G, the translocase that moves tRNAs and mRNA by one codon"
    - "A ribosomal protein enzyme in the large subunit that stabilizes the transition state"
  answer: 1
  explanation: "Peptide bond formation is catalyzed by the peptidyl transferase center of the large ribosomal subunit, and this activity resides in the 23S rRNA (prokaryotes) or 28S rRNA (eukaryotes) — making the ribosome a ribozyme. There is no dedicated protein enzyme for this step. A drug targeting peptide bond formation without affecting delivery or translocation would have to act on this RNA-based catalytic center. Option D is the most tempting wrong answer — many students assume there must be a protein enzyme."

- question: "What is the function of GTP hydrolysis by EF-Tu during aminoacyl-tRNA delivery, and why does it improve accuracy beyond what base pairing alone achieves?"
  type: multiple-choice
  options:
    - "GTP hydrolysis provides energy to force the aminoacyl-tRNA into the A site against electrostatic repulsion"
    - "GTP hydrolysis triggers a conformational change that releases EF-Tu only after correct codon-anticodon pairing is verified, allowing incorrect tRNAs to dissociate before accommodation — kinetic proofreading"
    - "GTP hydrolysis powers translocation of the ribosome by one codon after delivery is complete"
    - "GTP hydrolysis activates the aminoacyl-tRNA by phosphorylating the amino acid before peptide bond formation"
  answer: 1
  explanation: "This is kinetic proofreading. EF-Tu holds the charged tRNA in a configuration that cannot participate in peptide bond formation. Correct codon-anticodon pairing triggers a conformational change in the ribosome that stimulates GTP hydrolysis by EF-Tu, releasing the factor and allowing the tRNA to fully accommodate in the A site. Incorrect tRNAs lack the geometric fit needed to trigger this change and dissociate before GTP hydrolysis — a second selection step on top of base pairing. This two-stage discrimination achieves ~1 error per 10,000 amino acids, far better than the ~1 in 100 that base pairing alone would produce."

- question: "When a stop codon enters the A site of the ribosome, termination is triggered by a release factor that structurally mimics a tRNA."
  type: true-false
  answer: true
  explanation: "Release factors (RF1/RF2 in prokaryotes, eRF1 in eukaryotes) have an overall shape that resembles a tRNA, allowing them to fit into the A site. This molecular mimicry positions the factor's catalytic domain near the peptidyl transferase center, where it triggers hydrolysis of the ester bond connecting the completed polypeptide to the final tRNA — releasing the finished protein. This is an elegant example of structural mimicry: a protein solution to a problem first 'solved' by RNA."

- question: "Peptide bond formation in the ribosome is catalyzed by a protein enzyme called peptidyl transferase, which is encoded by a ribosomal protein gene."
  type: true-false
  answer: false
  explanation: "Peptide bond formation is catalyzed by the ribosomal RNA itself — specifically the 23S rRNA in prokaryotes and 28S rRNA in eukaryotes — making the ribosome a ribozyme. There is no protein enzyme responsible for this reaction. This was a major discovery confirming the RNA World hypothesis: the most fundamental step in protein synthesis is catalyzed by RNA, not protein. Ribosomal proteins play structural and regulatory roles but are not the catalytic component for peptide bond formation."

- question: "Explain how kinetic proofreading by EF-Tu achieves an error rate far lower than codon-anticodon base pairing alone could provide."
  type: short-answer
  answer: "Codon-anticodon base pairing provides one level of discrimination between correct and incorrect tRNAs, but the free energy difference between correct (Watson-Crick) and near-cognate base pairs is not large enough to achieve 1 error in 10,000 by thermodynamics alone. EF-Tu adds a second, kinetically independent discrimination step: it holds the aminoacyl-tRNA in a pre-accommodation state where peptide bond formation cannot occur. Only correct codon-anticodon pairing triggers a ribosomal conformational change that stimulates GTP hydrolysis by EF-Tu, releasing the factor and allowing tRNA accommodation. Incorrect tRNAs dissociate before this conformational change — they have had two independent opportunities to be rejected. The product of two sequential error rates (each ~1 in 100) gives ~1 in 10,000."
  explanation: "Kinetic proofreading is a general principle that appears wherever cells need accuracy beyond what equilibrium chemistry provides: it inserts irreversible steps (GTP hydrolysis) that allow incorrect intermediates to be discarded before the reaction is committed, at the cost of energy expenditure."
```

## Explainer

From your study of translation initiation, you know that the ribosome assembles on mRNA with the initiator tRNA positioned in the P site, ready to begin reading codons. Elongation is the repetitive cycle that builds the polypeptide chain one amino acid at a time, and it runs with striking speed and precision — roughly 15–20 amino acids per second in bacteria. The cycle has three steps that repeat for every codon: **delivery**, **peptide bond formation**, and **translocation**.

In the **delivery** step, each new aminoacyl-tRNA arrives at the ribosome's A site as a ternary complex with the elongation factor **EF-Tu** (or **eEF1A** in eukaryotes) and GTP. Think of EF-Tu as a quality-control chaperone: it holds the charged tRNA and allows it to sample the codon in the A site. If the anticodon-codon match is correct, complementary base pairing triggers a conformational change in the ribosome that stimulates GTP hydrolysis by EF-Tu. This is the **kinetic proofreading** step — incorrect tRNAs dissociate before GTP hydrolysis occurs, because they lack the geometric fit needed to trigger the conformational change. The result is an error rate of roughly one misincorporation per 10,000 amino acids, far better than codon-anticodon base pairing alone could achieve.

Once the correct aminoacyl-tRNA is locked into the A site, the **peptidyl transferase** reaction forms the peptide bond. This is catalyzed not by a protein enzyme but by the ribosomal RNA itself — specifically the 23S rRNA (28S in eukaryotes) — making the ribosome a **ribozyme**. The reaction transfers the growing polypeptide chain from the P-site tRNA to the amino group of the A-site aminoacyl-tRNA, extending the chain by one residue. After peptide bond formation, the P site holds a now-empty (deacylated) tRNA and the A site holds the peptidyl-tRNA bearing the entire growing chain. The elongation factor **EF-G** (or **eEF2**) then drives **translocation**: using the energy of GTP hydrolysis, it ratchets the ribosome forward by exactly one codon (three nucleotides), shifting the deacylated tRNA to the E (exit) site and the peptidyl-tRNA to the P site, leaving the A site open for the next incoming aminoacyl-tRNA.

**Termination** breaks this cycle. When a stop codon — **UAA**, **UAG**, or **UGA** — enters the A site, no aminoacyl-tRNA recognizes it. Instead, protein **release factors** bind: in prokaryotes, RF1 recognizes UAA and UAG while RF2 recognizes UAA and UGA; in eukaryotes, a single factor **eRF1** recognizes all three stop codons. The release factor mimics the shape of a tRNA, fitting into the A site and positioning a catalytic domain near the peptidyl transferase center. This triggers hydrolysis of the ester bond connecting the completed polypeptide to the final tRNA, freeing the finished protein. The ribosome then disassembles with help from **ribosome recycling factor** and EF-G (prokaryotes) or from eRF3 and ABCE1 (eukaryotes), releasing the mRNA and ribosomal subunits for reuse. The entire process — from initiation through hundreds or thousands of elongation cycles to termination — produces one complete polypeptide, ready for folding and post-translational modification.
