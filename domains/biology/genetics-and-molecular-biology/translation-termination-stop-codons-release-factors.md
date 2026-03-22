---
id: translation-termination-stop-codons-release-factors
title: Translation Termination and Release Factors
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: translation-elongation-elongation-factors
  type: hard
builds-toward:
- post-translational-modifications
tags:
- translation
- termination
- stop-codons
- release-factors
stage: advanced
status: draft
---

# Translation Termination and Release Factors

## Core Idea
Stop codons (UAA, UAG, UGA) are recognized by release factors (RF1, RF2 in prokaryotes; eRF1 in eukaryotes) rather than tRNAs. Release factors catalyze hydrolysis of the peptidyl-tRNA bond, releasing the completed polypeptide. RF3 (prokaryotes) and eRF3 (eukaryotes) are GTPases that facilitate release factor dissociation.

## How It's Best Learned
Compare stop codon recognition with elongation codon recognition. Understand why stop codons have no corresponding tRNAs. Study how release factors recognize stop codons and catalyze hydrolysis instead of aminoacyl transfer.

## Common Misconceptions
- Assuming stop codons are rare or non-essential; they delimit all coding sequences.
- Not recognizing that read-through of stop codons (rare tRNAs with stop-codon anticodons) can extend proteins in specialized genes.
- Thinking the peptide must be released from the ribosome immediately; recycling factors then dissociate the ribosomal subunits and release mRNA.

## Questions

```yaml
- question: "A cell biologist engineers a tRNA with an anticodon complementary to the UGA stop codon. What is the most likely consequence for translation at UGA sites?"
  type: multiple-choice
  options:
    - "UGA would continue to function as a stop codon because the ribosome preferentially recruits release factors over tRNAs at stop codons"
    - "UGA would be decoded as a sense codon — the tRNA would deliver an amino acid instead of triggering termination, extending the polypeptide"
    - "Translation would terminate faster at UGA sites because tRNA binding is more rapid than release factor binding"
    - "UGA would still cause termination, but with an additional amino acid appended to the C-terminus of the polypeptide"
  answer: 1
  explanation: "This is how natural suppressor tRNAs work. Stop codons are recognized by release factors precisely because no normal tRNA has a complementary anticodon. If a tRNA with a UGA anticodon is present, it competes with the release factor for the A site. When the tRNA wins, peptidyl transfer occurs (not hydrolysis), extending the polypeptide rather than releasing it — UGA is 'read through' as a sense codon. This suppression is exploited in biotechnology (e.g., incorporating non-canonical amino acids) and occurs naturally in some organisms for specific proteins like selenoproteins."

- question: "What distinguishes the chemical reaction catalyzed in the peptidyl transferase center when a release factor is in the A site, compared to when an aminoacyl-tRNA is in the A site during elongation?"
  type: multiple-choice
  options:
    - "With a release factor, a water molecule attacks the ester bond linking the polypeptide to the P-site tRNA; during elongation, the alpha-amino group of an incoming amino acid attacks that bond"
    - "With a release factor, the alpha-amino group of a special termination amino acid attacks the bond; during elongation, water performs the hydrolysis"
    - "Both reactions involve amino group attack, but release factors use glutamine as the nucleophile while elongation uses the incoming amino acid"
    - "Release factors use GTP hydrolysis to directly break the peptide bond, while elongation is GTP-independent"
  answer: 0
  explanation: "During elongation, the nucleophile is the alpha-amino group of the incoming aminoacyl-tRNA — this forms a new peptide bond and extends the chain. With a release factor occupying the A site, the nucleophile is instead a water molecule: this hydrolyzes the ester bond between the polypeptide and the P-site tRNA, releasing the completed polypeptide as a free chain. The release factor positions a critical glutamine residue in the peptidyl transferase center to facilitate this switch from aminoacyl transfer to hydrolysis."

- question: "In eukaryotes, a single release factor (eRF1) recognizes all three stop codons (UAA, UAG, UGA), whereas in prokaryotes two release factors (RF1 and RF2) divide stop codon recognition between them — with RF1 recognizing UAA and UAG, and RF2 recognizing UAA and UGA."
  type: true-false
  answer: true
  explanation: "This split is genuine and explains why UAA is the most common stop codon in prokaryotes — it is recognized by both RF1 and RF2, making termination at UAA especially reliable. Eukaryotes converged on a single omnibus release factor (eRF1) that handles all three. Both systems use a separate GTPase (RF3 in prokaryotes, eRF3 in eukaryotes) to facilitate release factor dissociation after the polypeptide is released."

- question: "Stop codons have no corresponding tRNAs because their nucleotide sequences are chemically incompatible with forming anticodon-codon base pairs."
  type: true-false
  answer: false
  explanation: "This is false — the absence of cognate tRNAs for stop codons is functional and evolutionary, not chemical. Suppressor tRNAs (naturally occurring mutant tRNAs with anticodons complementary to UAG, UAA, or UGA) demonstrate that standard Watson-Crick base pairing at stop codons is perfectly possible. The lack of normal tRNAs for stop codons is maintained by selection: if a tRNA decoded stop codons, translation would read through and produce abnormally long, likely non-functional proteins. Release factors evolved to occupy this niche instead, coupling stop codon recognition to hydrolysis rather than chain extension."

- question: "Why do stop codons recruit release factor proteins rather than tRNAs, and how does this difference produce termination instead of elongation?"
  type: short-answer
  answer: "No normal tRNA in any organism has an anticodon complementary to UAA, UAG, or UGA — this niche is occupied by release factor proteins instead. When a release factor occupies the ribosomal A site at a stop codon, it positions its active site in the peptidyl transferase center but presents no amino group for peptide bond formation. Instead, it facilitates nucleophilic attack by water on the ester bond linking the polypeptide to the P-site tRNA. Hydrolysis releases the completed polypeptide as a free chain. If a tRNA occupied the A site, its amino group would attack instead, extending the chain — elongation, not termination."
  explanation: "The critical contrast is nucleophile: aminoacyl-tRNA → amino group → new peptide bond (elongation); release factor → water → hydrolysis of existing ester bond (termination). The identity of what sits in the A site controls which reaction the peptidyl transferase center performs."
```

## Explainer

You have followed a polypeptide through translation elongation — watching aminoacyl-tRNAs deliver amino acids to the ribosomal A site, peptide bonds form in the peptidyl transferase center, and the ribosome translocate along the mRNA one codon at a time. But this cycle cannot continue forever. The cell needs a signal that says "the protein is complete, stop here." That signal is a **stop codon** — one of three triplets (UAA, UAG, or UGA) that encode no amino acid and instead trigger the release of the finished polypeptide.

The key difference between stop codons and sense codons is what occupies the A site when the ribosome encounters them. During elongation, each sense codon is recognized by an aminoacyl-tRNA whose anticodon is complementary. But no tRNA in any organism has an anticodon for UAA, UAG, or UGA. Instead, proteins called **release factors** recognize stop codons directly. In prokaryotes, **RF1** recognizes UAA and UAG, while **RF2** recognizes UAA and UGA — note that UAA is recognized by both, which is one reason it is the most common stop codon. In eukaryotes, a single factor called **eRF1** recognizes all three stop codons. These release factors are shaped roughly like a tRNA, allowing them to fit into the A site, but instead of delivering an amino acid they position a critical glutamine residue in the peptidyl transferase center.

Once a release factor is seated in the A site, it triggers **hydrolysis** rather than peptide bond formation. Instead of an amino group from a new amino acid attacking the ester bond linking the polypeptide to the P-site tRNA, a water molecule performs the attack. This breaks the bond between the completed polypeptide and the final tRNA, releasing the protein from the ribosome. A GTPase — **RF3** in prokaryotes, **eRF3** in eukaryotes — then uses GTP hydrolysis to dissociate the release factor from the ribosome.

After termination, the ribosome is still sitting on the mRNA with a deacylated tRNA in the P site. **Ribosome recycling factor** (RRF) and EF-G in prokaryotes, or ABCE1 in eukaryotes, split the ribosome into its large and small subunits so they can be reused. The entire process — from stop codon recognition through polypeptide release to ribosome disassembly — takes only a fraction of a second, yet errors here have outsized consequences. A failure to terminate produces an abnormally long protein that is usually non-functional and potentially toxic, which is why quality control mechanisms like nonsense-mediated mRNA decay exist to catch mRNAs with premature stop codons and aberrant termination events.
