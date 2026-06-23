---
id: translation-initiation-and-elongation
title: 'Translation: Initiation and Elongation'
domain: biology
course: biochemistry
prerequisites:
- id: translation
  type: hard
- id: ribosomes-and-protein-synthesis-intro
  type: soft
- id: rna-types-and-structure
  type: soft
- id: ribosome-protein-synthesis-factory
  type: hard
builds-toward:
- post-translational-modifications
tags:
- translation
- ribosome
- tRNA
- initiation factors
- elongation factors
stage: formal-systems
status: validated
---

# Translation: Initiation and Elongation

## Core Idea
Translation is the synthesis of proteins from mRNA on the ribosome using tRNAs as adaptor molecules. Initiation requires recognition of the start codon (AUG) by the initiator tRNA (fMet-tRNA in bacteria, Met-tRNAi in eukaryotes) and assembly of the ribosome initiation complex with initiation factors (IF1/2/3 in bacteria, eIF1-5 in eukaryotes). Elongation proceeds through three steps (cognate tRNA selection, peptide bond formation, translocation) catalyzed by elongation factors (EF-Tu/G in bacteria, eEF1A/eEF2 in eukaryotes). Termination occurs upon recognition of stop codons (UAA/UAG/UGA) by release factors.

## Questions

```yaml
- question: "A drug blocks EF-Tu's GTPase activity in bacteria. Which step of the elongation cycle would be most directly disrupted?"
  type: multiple-choice
  options:
    - "Peptide bond formation — EF-Tu catalyzes the transfer of the amino acid to the growing chain"
    - "Translocation — EF-Tu powers the movement of the ribosome along the mRNA"
    - "Aminoacyl-tRNA selection and delivery to the A site — EF-Tu uses GTP hydrolysis to verify correct codon-anticodon matching before releasing the tRNA"
    - "Termination — EF-Tu recognizes stop codons and recruits release factors"
  answer: 2
  explanation: "EF-Tu (eEF1A in eukaryotes) delivers aminoacyl-tRNA to the A site and uses GTP hydrolysis as an accuracy checkpoint: if the tRNA's anticodon matches the mRNA codon, GTP hydrolysis proceeds and the tRNA is accepted; if not, the tRNA is rejected before incorporation. Blocking GTPase activity would prevent this proofreading step, jamming tRNA delivery. Translocation is driven by EF-G (not EF-Tu), and peptide bond formation is catalyzed by the ribosomal RNA itself, not EF-Tu."

- question: "At the end of initiation, in which ribosomal site does the initiator tRNA sit, and what is the significance of this position?"
  type: multiple-choice
  options:
    - "The A site — this positions it to immediately accept a peptide bond from the incoming aminoacyl-tRNA"
    - "The P site — this positions the initiator tRNA (carrying the first amino acid) to donate to the first incoming aminoacyl-tRNA in the A site, beginning elongation"
    - "The E site — the initiator tRNA waits here until the large subunit joins"
    - "No specific site — the initiator tRNA floats freely until the first aminoacyl-tRNA arrives"
  answer: 1
  explanation: "After initiation, the initiator tRNA (carrying fMet in bacteria or Met in eukaryotes) occupies the P site (peptidyl site) of the assembled ribosome. This is critical: during elongation, the P site holds the growing polypeptide chain, and peptide bond formation transfers the peptide from the P-site tRNA to the amino acid on the A-site tRNA. Starting in the P site means the first elongation cycle immediately adds a second amino acid to fMet/Met, beginning the polypeptide chain."

- question: "The peptidyl transferase activity that catalyzes peptide bond formation in the ribosome is provided by RNA (specifically the 23S rRNA in bacteria), not by any ribosomal protein."
  type: true-false
  answer: true
  explanation: "This was a major discovery: the ribosome is a ribozyme — its catalytic activity resides in its RNA, not its proteins. The 23S rRNA (28S in eukaryotes) in the large subunit carries the peptidyl transferase center. Ribosomal proteins play structural and regulatory roles but do not directly catalyze the peptide bond. This supports the RNA World hypothesis — that RNA enzymes predated protein enzymes in early life."

- question: "Stop codons (UAA, UAG, UGA) are recognized by specialized tRNA molecules with anticodons complementary to each stop codon, just as sense codons are recognized by aminoacyl-tRNAs."
  type: true-false
  answer: false
  explanation: "Stop codons are recognized by release factors — proteins, not tRNAs. In bacteria, RF1 recognizes UAA and UAG; RF2 recognizes UAA and UGA; RF3 is a GTPase that assists. In eukaryotes, eRF1 recognizes all three stop codons. Release factors mimic the shape of a tRNA but trigger hydrolysis of the polypeptide from the final tRNA rather than peptide bond formation. The absence of aminoacyl-tRNAs for stop codons is why these codons terminate translation rather than incorporating an amino acid."

- question: "Why is initiation the most regulated phase of translation, and what advantage does regulating this step provide to the cell?"
  type: short-answer
  answer: "Initiation determines which mRNAs are translated and at what rate — it is the first committed step of protein synthesis. By regulating initiation factors (especially eIF2 and eIF4 in eukaryotes), cells can rapidly and globally modulate protein production in response to stress, nutrient availability, or developmental signals. Regulating elongation instead would be wasteful: the ribosome would be committed but stalled, tying up resources. Regulating initiation prevents ribosome commitment to unneeded mRNAs in the first place."
  explanation: "This is analogous to transcriptional regulation being preferred over post-transcriptional control when possible — intervening early is more efficient. Global translational shutdown via eIF2α phosphorylation (the integrated stress response) can halt most translation within minutes while allowing stress-response mRNAs with special 5' UTRs to escape the block. This kind of rapid, selective response would be impossible if elongation were the regulated step."
```

## Explainer

You already know that the ribosome reads mRNA to build proteins and that tRNAs serve as adaptor molecules, each carrying a specific amino acid matched to a three-nucleotide anticodon. The details of how this process actually works — how the machinery assembles, reads the message, and builds the chain — fall into three phases: **initiation**, **elongation**, and termination.

**Initiation** is the most regulated phase because it determines which mRNAs get translated and how efficiently. In bacteria, the small ribosomal subunit (30S) binds to a specific sequence on the mRNA called the **Shine-Dalgarno sequence**, which positions the start codon (AUG) in the correct reading frame. The initiator tRNA, carrying **N-formylmethionine (fMet)**, binds directly to this start codon with the help of three initiation factors (IF1, IF2, IF3). Only then does the large subunit (50S) join to form the complete 70S ribosome. In eukaryotes, the process is more elaborate: the small subunit (40S) is loaded with the initiator Met-tRNAᵢ and a suite of eukaryotic initiation factors (eIFs), then scans along the mRNA from the 5' cap until it finds the first AUG in a favorable sequence context (the Kozak sequence). The large subunit (60S) then joins to form the 80S ribosome. In both cases, the result is the same: a complete ribosome positioned at the start codon, with the initiator tRNA sitting in the **P site** (peptidyl site), ready for elongation.

**Elongation** is the repetitive heart of translation — a three-step cycle that adds one amino acid per round. First, an aminoacyl-tRNA (charged with the correct amino acid) is delivered to the **A site** (aminoacyl site) by elongation factor EF-Tu (bacteria) or eEF1A (eukaryotes), which uses GTP hydrolysis to ensure that only the tRNA with the correct anticodon is accepted — a **proofreading** step that gives translation its accuracy. Second, the ribosome catalyzes **peptide bond formation**: the amino acid in the P site is transferred onto the amino acid in the A site, extending the growing polypeptide by one residue. This reaction is catalyzed by the large subunit's peptidyl transferase activity, which is actually an RNA enzyme (ribozyme), not a protein. Third, **translocation** shifts the ribosome one codon forward along the mRNA, powered by EF-G (bacteria) or eEF2 (eukaryotes) and another round of GTP hydrolysis. The now-empty tRNA moves to the E site (exit site) and leaves, the peptidyl-tRNA moves from A to P, and a new codon is exposed in the empty A site. This cycle repeats at a rate of roughly 15–20 amino acids per second in bacteria.

The entire process consumes significant energy — two GTP molecules per amino acid added (one for tRNA selection, one for translocation), plus the ATP equivalents used earlier to charge each tRNA with its amino acid. This high energy cost buys accuracy and speed. The ribosome's error rate is approximately one wrong amino acid per 10,000 incorporated — remarkable given that it must discriminate between 20 different aminoacyl-tRNAs at each position using only three base pairs of codon-anticodon interaction. Translation continues until a **stop codon** (UAA, UAG, or UGA) enters the A site, where it is recognized not by a tRNA but by **release factors** that trigger hydrolysis of the completed polypeptide from the final tRNA, followed by disassembly of the ribosomal complex.
