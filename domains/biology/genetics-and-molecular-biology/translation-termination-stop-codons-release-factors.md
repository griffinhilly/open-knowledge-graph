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

## Explainer

You have followed a polypeptide through translation elongation — watching aminoacyl-tRNAs deliver amino acids to the ribosomal A site, peptide bonds form in the peptidyl transferase center, and the ribosome translocate along the mRNA one codon at a time. But this cycle cannot continue forever. The cell needs a signal that says "the protein is complete, stop here." That signal is a **stop codon** — one of three triplets (UAA, UAG, or UGA) that encode no amino acid and instead trigger the release of the finished polypeptide.

The key difference between stop codons and sense codons is what occupies the A site when the ribosome encounters them. During elongation, each sense codon is recognized by an aminoacyl-tRNA whose anticodon is complementary. But no tRNA in any organism has an anticodon for UAA, UAG, or UGA. Instead, proteins called **release factors** recognize stop codons directly. In prokaryotes, **RF1** recognizes UAA and UAG, while **RF2** recognizes UAA and UGA — note that UAA is recognized by both, which is one reason it is the most common stop codon. In eukaryotes, a single factor called **eRF1** recognizes all three stop codons. These release factors are shaped roughly like a tRNA, allowing them to fit into the A site, but instead of delivering an amino acid they position a critical glutamine residue in the peptidyl transferase center.

Once a release factor is seated in the A site, it triggers **hydrolysis** rather than peptide bond formation. Instead of an amino group from a new amino acid attacking the ester bond linking the polypeptide to the P-site tRNA, a water molecule performs the attack. This breaks the bond between the completed polypeptide and the final tRNA, releasing the protein from the ribosome. A GTPase — **RF3** in prokaryotes, **eRF3** in eukaryotes — then uses GTP hydrolysis to dissociate the release factor from the ribosome.

After termination, the ribosome is still sitting on the mRNA with a deacylated tRNA in the P site. **Ribosome recycling factor** (RRF) and EF-G in prokaryotes, or ABCE1 in eukaryotes, split the ribosome into its large and small subunits so they can be reused. The entire process — from stop codon recognition through polypeptide release to ribosome disassembly — takes only a fraction of a second, yet errors here have outsized consequences. A failure to terminate produces an abnormally long protein that is usually non-functional and potentially toxic, which is why quality control mechanisms like nonsense-mediated mRNA decay exist to catch mRNAs with premature stop codons and aberrant termination events.
